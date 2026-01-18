from twttr import shorten

def test_vowels_removed():
    assert shorten("twitter") == "twttr"
    assert shorten("aeiou") == ""

def test_uppercase_preserved():
    assert shorten("TWITTER") == "TWTTR"

def test_y():
    assert shorten("tiny") == "tny"

def test_numbers_punctuation():
    assert shorten("/.124!?+") == "/.124!?+"

def test_empty():
    assert shorten("") == ""

