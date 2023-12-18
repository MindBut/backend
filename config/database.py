from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.MindBut_db

moodRecord_collection = db.moodRecord_collection
moodTracking_collection = db.moodTracking
surverys_collection = db.surverys
chatMessages_collection = db.chatMessages
users_collection = db.users
admin_collection = db.admin

