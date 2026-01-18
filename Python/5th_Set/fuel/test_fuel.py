import pytest
from fuel import convert, gauge

def test_convert():
    assert convert("0/1") == 0
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert('3/4') == 75
    assert convert("1/1") == 100

def test_convert_errors():
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    with pytest.raises(ValueError):
        convert("3/2")
    with pytest.raises(ValueError):
        convert("-3/4")
    with pytest.raises(ValueError):
        convert("cat/dog")
    with pytest.raises(ValueError):
        convert("3+2")




def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(99.5) == 'F'
    assert gauge(100) == "F"

