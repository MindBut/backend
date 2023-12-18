from typing import List
from fastapi import APIRouter
from models.models import moodRecord
from config.database import moodRecord_collection
from schema.schemas import record_moodRecords
from bson import ObjectId


router = APIRouter()

@router.get("/moodRecords", response_model=List[moodRecord])
async def get_mood_records():
    # Assuming you're using an asynchronous database driver like Motor
    mood_records_cursor = moodRecord_collection.find()
    mood_records_list = await mood_records_cursor.to_list(length=None)
    return [moodRecord(**record) for record in mood_records_list]

@router.post("/moodRecords", response_model=moodRecord)
async def add_mood_record(moodRecord: moodRecord):
    moodRecord = record_moodRecords(moodRecord)
    moodRecord_collection.insert_one(moodRecord)
    return moodRecord