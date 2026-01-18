from numb3rs import validate


def test_valid_addresses():
    assert validate("0.0.0.0")
    assert validate("1.2.3.4")
    assert validate("192.168.0.1")
    assert validate("255.255.255.255")

def test_out_range():
    assert not validate("256.100.111.111")
    assert not validate("2.300.0.1")
    assert not validate("2.30.440.1")
    assert not validate("0.0.0.256")

def test_not_numeric():
    assert not validate("cat.1.2.3")
    assert not validate("1.2.3.three")
    assert not validate("1.2.3.-1")

def test_wrong_shape():
    assert not validate("1.1.1")       #too few
    assert not validate("1.1.1.1.1")   #too many
    assert not validate("1..1.1")      #empty_octet
    assert not validate(".1.1.1.1")    #leading dot
    assert not validate("1.1.1.1.")    #tailing dot
    assert not validate(" 1.1.1.1")    #leading space
    assert not validate("1.1.1.1 ")    #leading space
    assert not validate("1.1. 1.1")    #space inside



