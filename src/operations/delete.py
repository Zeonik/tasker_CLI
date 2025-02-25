import typer
from typing_extensions import Annotated

app = typer.Typer(no_args_is_help=True, rich_markup_mode="rich")

@app.command(rich_help_panel="[red]Updating and deleting tasks[/red]")
def delete(id: int):
    print("Deleting task")