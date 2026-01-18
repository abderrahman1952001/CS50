from bank import value


def test_hello():
    assert value("hello, world") == 0

def test_h():
    assert value('hi, world') == 20

def test_rest():
    assert value('world') == 100

def test_case():
    assert value('Hello') == 0
    assert value('Hi') == 20
    assert value('ABCD') == 100

