import gluonnlp as nlp
import numpy as np
import torch
from torch import nn
from kobert_tokenizer import KoBERTTokenizer
from transformers import BertModel
from torch.utils.data import Dataset

from classifier import BERTSentenceTransform, BERTClassifier

ctx = "cuda" if torch.cuda.is_available() else "cpu"
device = torch.device(ctx)

tokenizer = KoBERTTokenizer.from_pretrained('skt/kobert-base-v1')
bertmodel = BertModel.from_pretrained('skt/kobert-base-v1', return_dict=False)
vocab = nlp.vocab.BERTVocab.from_sentencepiece(tokenizer.vocab_file, padding_token='[PAD]')
model = BERTClassifier(bertmodel, dr_rate=0.5).to(device)


model.load_state_dict(torch.load('model_state_dict_ver2.pt', map_location=torch.device('cpu')), strict=False)
# model.eval()

class BERTDataset(Dataset):
    def __init__(self, dataset, sent_idx, label_idx, bert_tokenizer, vocab, max_len,
                 pad, pair):
        transform = BERTSentenceTransform(bert_tokenizer, max_seq_length=max_len,vocab=vocab, pad=pad, pair=pair)
        self.sentences = [transform([i[sent_idx]]) for i in dataset]
        self.labels = [np.int32(i[label_idx]) for i in dataset]

    def __getitem__(self, i):
        return (self.sentences[i] + (self.labels[i], ))

    def __len__(self):
        return (len(self.labels))

max_len = 64
batch_size = 64
warmup_ratio = 0.1
num_epochs = 10
max_grad_norm = 1
log_interval = 200
learning_rate =  5e-5

def new_softmax(a) :
    c = np.max(a) 
    exp_a = np.exp(a-c)
    sum_exp_a = np.sum(exp_a)
    y = (exp_a / sum_exp_a) * 100
    return np.round(y, 3)

def predict(predict_sentence):
    data = [predict_sentence, '0']
    dataset_another = [data]

    another_test = BERTDataset(dataset_another, 0, 1, tokenizer, vocab, max_len, True, False)
    test_dataloader = torch.utils.data.DataLoader(another_test, batch_size=batch_size, num_workers=0)

    model.eval()

    for batch_id, (token_ids, valid_length, segment_ids, label) in enumerate(test_dataloader):
        token_ids = token_ids.long().to(device)
        segment_ids = segment_ids.long().to(device)

        valid_length= valid_length
        label = label.long().to(device)

        out = model(token_ids, valid_length, segment_ids)

        test_eval=[]
        for i in out:
            logits=i
            logits = logits.detach().cpu().numpy()
            min_v = min(logits)
            total = 0
            probability = []
            logits = np.round(new_softmax(logits), 3).tolist()
            for logit in logits:
                #print(logit)
                probability.append(np.round(logit, 3))

            if np.argmax(logits) == 0:  emotion = "기쁨"
            elif np.argmax(logits) == 1: emotion = "슬픔"
            elif np.argmax(logits) == 2: emotion = "분노"
            elif np.argmax(logits) == 3: emotion = "불안"

            probability.append(emotion)

    result = probability[-1]
    # print(f"당신의 말에서 {result}의 감정이 느껴집니다.")
    return result

# print(predict('상사한테 혼났어. 일처리를 제대로 하지 못해서 그랬어. 내가 앞으로 회사생활을 잘 할 수 있을지 모르겠어.')) ## 슬픔
# print(predict('오늘 여자친구랑 헤어졌어. 나는 아무리 생각해도 왜 그랬는지 모르겠고 걔가 잘못했다고 생각해.')) ## 분노