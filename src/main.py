import typer
from operations import app as operations
from version import app as version_app
from mark import app as mark
from list import app as list
app = typer.Typer(add_completion=False, no_args_is_help=True, rich_markup_mode="rich")

app.add_typer(version_app)
app.add_typer(operations)
app.add_typer(mark)
app.add_typer(list)

if __name__ == "__main__":
    app()
