def record_moodRecords(moodRecords):
    return {
        "recordId": moodRecords["recordId"],
        "userId": moodRecords["userId"],
        "date": moodRecords["date"],
        "moodDetails": moodRecords["moodDetails"]
    }


