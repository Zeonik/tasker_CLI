import typer
from typing_extensions import Annotated

app = typer.Typer(no_args_is_help=True, rich_markup_mode="rich")

@app.command(rich_help_panel="Adding a new task")
def add(task: Annotated[str, typer.Argument(help="Enter task")] = "qwe",):
    """
        Create a new task.
    """
    print(f"Creating task ->> {task}")