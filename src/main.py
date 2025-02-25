import typer
from operations import app as operations
from version import app as version_app

app = typer.Typer(no_args_is_help=True, rich_markup_mode="rich")

app.add_typer(version_app)
app.add_typer(operations, name="add")

if __name__ == "__main__":
    app()
