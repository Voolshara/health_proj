from src import __version__
from src.db.db import Selection


def test_version():
    assert __version__ == '0.1.0'

def test_driver():
    Sel = Selection()
    out = Sel.without_stroke({
        "stroke" : False,
        "problem_no_stroke" : "Test"
    })
    print(out)
    assert out == 6