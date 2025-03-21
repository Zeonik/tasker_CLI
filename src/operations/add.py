import typer
import json
from typing import List, Optional

from typing_extensions import Annotated
from task import add_task

app = typer.Typer(no_args_is_help=True, rich_markup_mode="rich")


@app.command()
def add(task: Annotated[Optional[List[str]], typer.Argument(help="Enter task")], ):
    """
        Create new task.
    """
    node = add_task(" ".join(task))
    try :
        with open("db.json", "r") as JSONfile:
            loaded = json.load(JSONfile)
            loaded.append(node)
        with open("db.json", "w") as JSONfile:
            json.dump(loaded, JSONfile, indent=4)
        print("New task added with ID:"+str(node["id"]))

    except json.JSONDecodeError as err:
        print(f"Invalid JSON file format: {err}")
