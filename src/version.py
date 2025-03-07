import typer
from typing_extensions import Annotated

app = typer.Typer()


@app.command()
def version():
    print("CLI Task Manager Version 1.0")
