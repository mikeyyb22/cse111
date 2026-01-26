from chemistry import make_uppercase
import pytest

def test_make_uppercase():
    assert make_uppercase("c5h4") == "C5H4"
    assert make_uppercase("h20") == "H20"
    assert make_uppercase("H2o") == "H2O"
    # assert make_uppercase("H3(C4h4)fl32") == "H3(C4H4)Fl32"