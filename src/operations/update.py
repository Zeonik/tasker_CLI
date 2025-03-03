import typer
from typing_extensions import Annotated

app = typer.Typer(no_args_is_help=True, rich_markup_mode="rich")

@app.command()
def update(id: int, task: str):
    """
           Update a task.
    """
    print("Updating task")
