import typer
import json
from typing_extensions import Annotated

app = typer.Typer(no_args_is_help=True, rich_markup_mode="rich")


@app.command()
def delete(taskid: Annotated[int, typer.Argument(help="Delete task")], ):
    """
           Delete task.
    """
    try:
        with open("db.json", "r") as JSONfile:
            loaded = json.load(JSONfile)
            result = [item for item in loaded if item["id"] != taskid]
        with open("db.json", "w") as JSONfile:
            json.dump(result, JSONfile, indent=4)

        print("Deleted task with ID:" + str(taskid))
    except json.JSONDecodeError as err:
        print(f"Invalid JSON file format: {err}")
