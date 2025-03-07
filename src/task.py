import json
from enum import Enum
from datetime import datetime


def add_task(text: str):
    with open("db.json", "r") as JSONfile:
        data = json.load(JSONfile)
        maxid = max(item["id"] for item in data)
    new_task = {"id": maxid + 1,
                "text": text,
                "status": "todo",
                "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
    return new_task
