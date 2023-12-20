from fastapi import APIRouter, Depends, HTTPException, Path
from database.database_model import Chatting, Users
from sqlalchemy.orm import Session
from typing_extensions import Annotated
from database.database import SessionLocal
from sqlalchemy import desc

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

@router.post("/chatting/moodtracking")
def create_chatting_moodtracking(db:db_dependency, user_kakaotalk = str, message_first = str,
                                 emotion_one = str, emotion_two = str, emotion_intensity = float):
    try:
        user = get_user(db, user_kakaotalk) 
        #model이 들어갈 부분 
        message_model = user.survey_question_one + user.survey_question_two + user.survey_question_three + user.survey_question_four + message_first + emotion_one + emotion_two + emotion_intensity

        new_chatting = Chatting(
            user_id = user.user_id,
            message_first = message_first,
            message_model = message_model,
            emotion_one = emotion_one,
            emotion_two = emotion_two,
            emotion_intensity = emotion_intensity
        )
        db.add(new_chatting)
        db.commit()
        return{'detail' : 'success to create moodtracking chatting'}
    except:
        return{'detail' : 'fail to create moodtracking chatting'}
    
@router.post("/chatting")
def create_chatting(db: db_dependency, user_kakaotalk = str, message_first = str):
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

