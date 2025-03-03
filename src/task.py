import json


class Task:
    def __init__(self, text: str, status: str = "todo"):
        with open("db.json", "r") as JSONfile:
            data = json.load(JSONfile)
            maxid = max(item["id"] for item in data)
        self.id = maxid + 1
        self.text = text
        self.status: str = status

    def changeStatus(self, newstatus):
        self.status = newstatus

    def getObj(self) -> dict:
        return {"id": self.id, "text": self.text, "status": self.status}
