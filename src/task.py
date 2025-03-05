import json
from enum import Enum
from datetime import datetime

class Status(str, Enum):
    todo = "todo"
    done = "done"
    in_progress = "in-progress"

def add_task(text: str, status: Status = Status.todo):
    with open("db.json", "r") as JSONfile:
        data = json.load(JSONfile)
        maxid = max(item["id"] for item in data)
    new_task = {"id": maxid + 1,
                "text": text,
                "status": status,
                "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                }
    return new_task



