from database.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.sql import func
from datetime import date

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

class Chatting(Base):
    __tablename__ = "chattings"

    chatting_id = Column(Integer, primary_key = True, index = True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    chatting_date = Column(Date, default=func.now())
    message_first = Column(String)
    message_model = Column(String)
    emotion_one = Column(String)
    emotion_two = Column(String)
    emotion_intensity = Column(Float)
