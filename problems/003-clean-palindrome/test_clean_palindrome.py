from clean_palindrome import is_clean_palindrome


def test_classic_sentence():
    assert is_clean_palindrome("A man, a plan, a canal: Panama")


def test_not_a_palindrome():
    assert not is_clean_palindrome("race a car")


def test_mixed_case_and_quotes():
    assert is_clean_palindrome("No 'x' in Nixon")


def test_digits_count():
    assert is_clean_palindrome("12321")
    assert not is_clean_palindrome("123")
    assert not is_clean_palindrome("0P")


def test_empty_and_only_symbols():
    assert is_clean_palindrome("")
    assert is_clean_palindrome("!!")
    assert is_clean_palindrome(" , . ")


def test_single_character():
    assert is_clean_palindrome("a")


def test_even_length():
    assert is_clean_palindrome("abba")
    assert not is_clean_palindrome("abca")
