from plates import is_valid

def test_condition_1():
    assert is_valid('CS50')
    assert not is_valid('C50')

def test_condition_2():
    assert is_valid('Allah')
    assert not is_valid('A')
    assert not is_valid('AllahAkbar')


def test_condition_3():
    assert not is_valid('CS50C')
    assert not is_valid('CS05')

def test_condition_4():
    assert not is_valid('CS50!')
    assert not is_valid('CS 50')
    assert not is_valid('CS.50')


