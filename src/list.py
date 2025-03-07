import typer
import json
from typing_extensions import Annotated
from rich.console import Console
from rich.table import Table
from rich import box

app = typer.Typer(no_args_is_help=True, rich_markup_mode="rich")


@app.command()
def list(status: Annotated[str, typer.Argument(help="Task ID")] = "", ):
    """
           List all
    """
    console = Console()
    if status == "":
        with open("db.json", "r") as JSONfile:
            loaded = json.load(JSONfile)
            table = Table("id", "Description", "Status", "Date of creation", "Date of modification", box=box.ROUNDED,
                          title="List of ALL tasks", title_style="bold black on yellow", style="YELLOW")
            for item in loaded:
                table.add_row(str(item["id"]), item["text"], item["status"], item["createdAt"], item["updatedAt"])
            console.print(table)

    elif status == "done":
        try:
            with open("db.json", "r") as JSONfile:
                loaded = json.load(JSONfile)
                table = Table("id", "Description", "Status", "Date of creation", "Date of modification",
                              box=box.ROUNDED,
                              title="List of DONE tasks", title_style="bold black on green", style="GREEN")
                for item in [item for item in loaded if item["status"] == "done"]:
                    table.add_row(str(item["id"]), item["description"], item["status"], item["createdAt"], item["updatedAt"])
                if table.rows:
                    console.print(table)
                else:
                    print("There is no DONE tasks")
        except json.JSONDecodeError as err:
            print(f"Invalid JSON file format: {err}")



    elif status == "todo":
        with open("db.json", "r") as JSONfile:
            loaded = json.load(JSONfile)
            table = Table("id", "Description", "Status", "Date of creation", "Date of modification", box=box.ROUNDED,
                          title="List of TODO tasks", title_style="bold black on red", style="RED")
            for item in [item for item in loaded if item["status"] == "todo"]:
                table.add_row(str(item["id"]), item["description"], item["status"], item["createdAt"], item["updatedAt"])
            console.print(table)

    elif status == "in-progress":
        with open("db.json", "r") as JSONfile:
            loaded = json.load(JSONfile)
            table = Table("id", "Description", "Status", "Date of creation", "Date of modification", box=box.ROUNDED,
                          title="List of IN-PROGRESS tasks", title_style="bold black on cyan", style="CYAN")
            for item in [item for item in loaded if item["status"] == "in-progress"]:
                table.add_row(str(item["id"]), item["description"], item["status"], item["createdAt"], item["updatedAt"])
            console.print(table)
