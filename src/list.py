import typer
import json
from typing import List, Optional
from typing_extensions import Annotated
from datetime import datetime
from rich.console import Console
from rich.table import Table

app = typer.Typer(no_args_is_help=True, rich_markup_mode="rich")


@app.command()
def list(status: Annotated[str, typer.Argument(help="Task ID")] = "",):
    """
           List all
    """
    console = Console()
    if status == "":
        with open("db.json", "r") as JSONfile:
            loaded = json.load(JSONfile)
            table = Table("id", "Description", "Status", "Date of creation","Date of modification",)
            for item in loaded:
                table.add_row(str(item["id"]), item["text"], item["status"],item["createdAt"],item["updatedAt"])
            console.print(table)

    elif status == "done":
        with open("db.json", "r") as JSONfile:
            loaded = json.load(JSONfile)
            table = Table("id", "Description", "Status", "Date of creation","Date of modification",)
            for item in [item for item in loaded if item["status"] == "done"]:
                table.add_row(str(item["id"]), item["text"], item["status"],item["createdAt"],item["updatedAt"])
            console.print(table)

    elif status == "todo":
        with open("db.json", "r") as JSONfile:
            loaded = json.load(JSONfile)
            table = Table("id", "Description", "Status", "Date of creation","Date of modification",)
            for item in [item for item in loaded if item["status"] == "todo"]:
                table.add_row(str(item["id"]), item["text"], item["status"],item["createdAt"],item["updatedAt"])
            console.print(table)

    elif status == "in-progress":
        with open("db.json", "r") as JSONfile:
            loaded = json.load(JSONfile)
            table = Table("id", "Description", "Status", "Date of creation","Date of modification",)
            for item in [item for item in loaded if item["status"] == "in-progress"]:
                table.add_row(str(item["id"]), item["text"], item["status"],item["createdAt"],item["updatedAt"])
            console.print(table)