import typer
import json
from typing import List, Optional
from typing_extensions import Annotated
from task import Task

app = typer.Typer(no_args_is_help=True, rich_markup_mode="rich")


@app.command()
def update(taskid: Annotated[int, typer.Argument(help="Task ID")],
           task: Annotated[Optional[List[str]], typer.Argument(help="New task text")], ):
    """
           Update task.
    """
    updated = Task(" ".join(task))
    updated.id = taskid
    with open("db.json", "r") as JSONfile:
        loaded = json.load(JSONfile)
        result = [item for item in loaded if item["id"] != taskid]
        result.append(updated.getObj())
    with open("db.json", "w") as JSONfile:
        json.dump(result, JSONfile, indent=4)
