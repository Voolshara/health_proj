from src.db.db import DB_new
from typer import Typer


runner = Typer()


@runner.command()
def runner():
    DBN = DB_new()
    DBN.create_all_tables()