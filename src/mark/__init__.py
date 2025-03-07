import typer
from .done import app as done_app
from .in_progress import app as in_progress

app = typer.Typer()
app.add_typer(done_app)
app.add_typer(in_progress)

