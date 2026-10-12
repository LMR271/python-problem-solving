from count_vowels import count_vowels

def test_basic():
    assert count_vowels("hello") == 2

def test_uppercase():
    assert count_vowels("AEIOU") == 5
    assert count_vowels("Banana") == 3

def test_no_vowels():
    assert count_vowels("rhythm") == 0

def test_spaces_and_punctuation():
    assert count_vowels("I am here!") == 4

def test_empty():
    assert count_vowels("") == 0
