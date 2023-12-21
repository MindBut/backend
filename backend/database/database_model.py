from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.sql import func
from datetime import datetime
from pydantic import BaseModel

class Users(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key= True, index = True)
    user_kakaotalk = Column(String)
    user_name = Column(String)
    bot_name = Column(String)
    bot_color = Column(String)
    survey_question_one = Column(String)
    survey_question_two = Column(String)
    survey_question_three = Column(String)
    survey_question_four = Column(String)
    survey_question_five = Column(String)

class Chatting(Base):
    __tablename__ = "chattings"

    chatting_id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    chatting_date = Column(Date, default=datetime.now().date())
    message_prompt = Column(String)
    message_first = Column(String)
    message_model = Column(String)
    emotion_reason = Column(String)
    emotion_one = Column(String)
    emotion_two = Column(String)
    emotion_intensity = Column(Float, default = 0.0) 

class User(BaseModel):
    
    user_id: int
    user_kakaotalk: str
    user_name: str
    bot_name: str
    bot_color: str 
    survey_question_one: str 
    survey_question_two: str
    survey_question_three: str 
    survey_question_four: str
    survey_question_five: str 

class Param_Chatting(BaseModel):

    chatting_id: int
    user_id: int
    chatting_date: datetime 
    message_prompt: str
    message_first: str
    message_model: str 
    emotion_reason: str 
    emotion_one: str 
    emotion_two: str 
    emotion_intensity: float   
