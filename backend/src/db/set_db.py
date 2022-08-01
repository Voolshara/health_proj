from src.db.db import create_all_tables
from typer import Typer


runner = Typer()


@runner.command()
def runner():
    create_all_tables()