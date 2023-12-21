from fastapi import APIRouter, Depends, HTTPException, Path
from database.database_model import Chatting, Users
from sqlalchemy.orm import Session
from typing_extensions import Annotated
from database.database import SessionLocal
from sqlalchemy import desc
from datetime import date
from openai import OpenAI
from model.moodtracking_model import moodtracking_model

router = APIRouter(
    tags = ["chatting"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

def get_user(db = db_dependency, user_kakaotalk = str):
    user = db.query(Users).filter(Users.user_kakaotalk == user_kakaotalk).first()
    return user

def make_emotion_intensity(emotion_intensity : float) -> str:
    if(float(emotion_intensity) < 0.2): return "아주 조금 "
    elif(float(emotion_intensity) < 0.4): return "조금 "
    elif(float(emotion_intensity) < 0.6): return "보통 "
    elif(float(emotion_intensity) < 0.8): return "많이 "
    else: return "아주 많이 " 

def transform_mood_epression(user_mood):
    mood_transformations = {
        '툴툴대는': '툴툴대고 싶어요',
        '좌절한': '좌절스러워요',
        '짜증나는': '짜증나요',
        '방어적인': '방어적이에요',
        '악의적인': '악의적이에요',
        '안달하는': '안달나요',
        '구역질 나는': '구역질 나요',
        '노여워하는': '노여워요',
        '성가신': '성가셔요',
        '실망한': '실망스러워요',
        '비통한': '비통해요',
        '우울한': '우울해요',
        '마비된': '마비된 것 같아요',
        '염세적인': '염세적이에요',
        '눈물이 나는': '눈물이 나요',
        '낭패한': '낭패감이 들어요',
        '환멸을 느끼는': '환멸을 느껴요',
        '두려운': '두려워요',
        '스트레스 받는': '스트레스 받아요',
        '취약한': '취약해요',
        '헷갈리는': '헷갈려요',
        '당황스러운': '당황스러워요',
        '회의적인': '회의적이에요',
        '걱정스러운': '걱정스러워요',
        '조심스러운': '조심스러워요',
        '신경쓰이는': '신경이 쓰여요',
        '질투하는': '질투나요',
        '배신당한': '배신스러워요',
        '고립된': '고립감을 느껴요',
        '충격 받은': '충격적이에요',
        '궁핍한': '궁핍해요',
        '희생된': '희생된 것 같아요',
        '억울한': '억울해요',
        '괴로워하는': '괴로워요',
        '버려진': '버려진 것 같아요',
        '남의 시선을 의식하는': '남의 시선이 의식돼요',
        '외로운': '외로워요',
        '열등한': '열등감이 들어요',
        '죄책감 드는': '죄책감이 들어요',
        '부끄러운': '부끄러워요',
        '혐오스러운': '혐오스러워요',
        '한심한': '제 자신이 한심해요',
        '감사한': '감사해요',
        '믿는': '믿음직스러워요',
        '편안한': '편안해요',
        '만족한': '만족스러워요',
        '흥분한': '흥분돼요',
        '느긋한': '느긋해요',
        '안도하는': '안도돼요',
        '신난': '신나요',
        '자신감 있는': '자신감 있어요'
    }
    return mood_transformations.get(user_mood)

@router.post("/chatting/moodtracking")
def create_chatting_moodtracking(db:db_dependency, user_kakaotalk = str, emotion_reason = str,
                                 emotion_one = str, emotion_two = str, emotion_intensity = float):
    try:
        user = get_user(db, user_kakaotalk) 
        #model이 들어갈 부분 
        message_prompt =  "저는 지금 " + emotion_reason + " 때문에 "  + make_emotion_intensity(emotion_intensity) + transform_mood_epression(emotion_two)
        message_model = moodtracking_model(message_prompt)
        new_chatting = Chatting(
            user_id = user.user_id,
            message_model = message_model,
            emotion_reason = emotion_reason,
            emotion_one = emotion_one,
            emotion_two = emotion_two,
            emotion_intensity = emotion_intensity
        )
        db.add(new_chatting)
        db.commit()
        return{'detail' : 'success to create moodtracking chatting'}
    except Exception as e:
        return{'detail' : f'fail to create moodtracking chatting{str(e)}'}
    
@router.post("/chatting")
def create_chatting(db: db_dependency, user_kakaotalk : str, message_first : str):
    try: 
        user = get_user(db, user_kakaotalk)
        # model이 들어갈 부분 -------
        message_model = user.survey_question_one + user.survey_question_two + user.survey_question_three + user.survey_question_four + message_first
        #---------------------------
        new_chatting = Chatting(
            user_id = user.user_id,
            message_first = message_first,
            message_model = message_model,
        )
        db.add(new_chatting)
        db.commit()
        return{'detail' : 'success to create chatting'}
    except:
        return{'detail' : 'fail to create chatting'}

@router.get("/chatting/record")
def get_all_chatting(db: db_dependency, user_kakaotalk = str):
    try:
        user = get_user(db, user_kakaotalk)
        return  db.query(Chatting).filter(Chatting.user_id == user.user_id).all()
    except:
        return{'detail' : "fail to get all chatting"}

@router.get("/chatting/record/last")
def get_last_chatting(db: db_dependency, user_kakaotalk = str):
    try:
        user = get_user(db, user_kakaotalk)
        last_chatting = db.query(Chatting).filter(Chatting.user_id == user.user_id).order_by(desc(Chatting.chatting_id)).first()
        return last_chatting
    except:
        return{'detail' : "fail to get last chatting"}

@router.get("/chatting/record/date")
def get_last_chatting(db: db_dependency, user_kakaotalk = str, chatting_date = date):
    try:
        user = get_user(db, user_kakaotalk)
        date_chatting = db.query(Chatting).filter(Chatting.user_id == user.user_id).filter(Chatting.chatting_date == chatting_date).order_by(desc(Chatting.chatting_id)).all()
        return date_chatting
    except:
        return{'detail' : "fail to get date chatting"}

@router.get("/chatting/moodrecord")
def get_moodrecord(db: db_dependency, user_kakaotalk = str):
    try:
        user = get_user(db, user_kakaotalk)
        return  db.query(Chatting).filter(Chatting.user_id == user.user_id).filter(Chatting.emotion_one != None).all()
    except:
        return{'detail' : "fail to get moodrecord"}
    
@router.get("/chatting/record/{chatting_id}")
def get_one_chatting(db: db_dependency, user_kakaotalk = str, chatting_id: int = Path):
    try:
        user = get_user(db, user_kakaotalk)
        return  db.query(Chatting).filter(Chatting.user_id == user.user_id).filter(Chatting.chatting_id == chatting_id).all()
    except:
        return{'detail' : "fail to get chatting"}

