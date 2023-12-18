from pydantic import BaseModel
from datetime import datetime

class moodRecord(BaseModel):
    recordId: str
    userId: str
    date: datetime
    moodDetails: list

class moodTracking(BaseModel):
    trackingId: str
    userId: str
    emotion: str
    category: dict
    intensity: float

class survery(BaseModel):
    surveryId: str
    userId: str
    questions: list
    answers: list

class chatMessage(BaseModel):
    messageId: int
    userId: str
    message: str
    timeStamp: datetime
    moodRecordRef: int