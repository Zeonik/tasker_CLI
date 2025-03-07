import typer
import json
from typing_extensions import Annotated
from datetime import datetime

app = typer.Typer(no_args_is_help=True, rich_markup_mode="rich")


@app.command()
def mark_in_progress(taskid: Annotated[int, typer.Argument(help="Task ID")],):
    """
           Mark task as In Progress
    """

    with open("db.json", "r") as JSONfile:
        loaded = json.load(JSONfile)
        updatedlist = [{**task, "status": "in-progress","updatedAt": datetime.now().strftime("%Y-%m-%d %H:%M:%S")} if task["id"] == taskid else task for task in loaded]

    with open("db.json", "w") as JSONfile:
        json.dump(updatedlist, JSONfile, indent=4)
