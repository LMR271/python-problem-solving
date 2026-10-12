from reverse_string import reverse_string

def test_basic():
    assert reverse_string("abc") == "cba"

def test_palindrome():
    assert reverse_string("racecar") == "racecar"

def test_with_spaces():
    assert reverse_string("hi there") == "ereht ih"

def test_single_and_empty():
    assert reverse_string("a") == "a"
    assert reverse_string("") == ""
