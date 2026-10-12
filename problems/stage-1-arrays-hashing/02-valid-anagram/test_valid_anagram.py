from valid_anagram import is_anagram

def test_anagram():
    assert is_anagram("listen", "silent") is True
    assert is_anagram("anagram", "nagaram") is True

def test_not_anagram():
    assert is_anagram("rat", "car") is False

def test_same_letters_different_counts():
    assert is_anagram("aab", "abb") is False

def test_different_lengths():
    assert is_anagram("abc", "abcd") is False

def test_empty_strings():
    assert is_anagram("", "") is True
