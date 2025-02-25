import typer

app = typer.Typer()


@app.command()
def version():
    print("My CLI Task Manager Version 1.0")