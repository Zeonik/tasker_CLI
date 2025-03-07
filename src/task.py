import json
from datetime import datetime


def add_task(text: str):
    try:
        with open("db.json", "r") as JSONfile:
            data = json.load(JSONfile)
            maxid = max(item["id"] for item in data) if data else 0
            new_task = {"id": maxid + 1,
                        "description": text,
                        "status": "todo",
                        "createdAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        }
            return new_task
    except json.JSONDecodeError as err:
        print(f"Invalid JSON file format. Couldn't create Task: {err}")
