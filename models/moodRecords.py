from pydantic import BaseModel
from datetime import datetime

class moodRecord(BaseModel):
    recordId: str
    userId: str
    date: datetime
    moodDetails: list

