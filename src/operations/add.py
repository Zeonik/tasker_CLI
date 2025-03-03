import typer
import json
from typing import List, Optional

from typing_extensions import Annotated
from task import Task

app = typer.Typer(no_args_is_help=True, rich_markup_mode="rich")


@app.command()
def add(task: Annotated[Optional[List[str]], typer.Argument(help="Enter task")], ):
    """
        Create a new task.
    """
    node = Task(" ".join(task))
    with open("db.json", "r") as JSONfile:
        loaded = json.load(JSONfile)
        loaded.append(node.getObj())
    with open("db.json", "w") as JSONfile:
        json.dump(loaded, JSONfile, indent=4)
