from unittest import TestCase
import task
import datetime

class Test(TestCase):
    def test_add_task(self):
        result = {
            "id": 8,
            "text": "new task done",
            "status": "todo",
            "createdAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "updatedAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        func = task.add_task("new task done", "todo")
        self.assertEqual(func, result)
