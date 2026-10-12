from top_k_words import top_k_words


def test_basic():
    assert top_k_words("the cat and the hat", 2) == [("the", 2), ("and", 1)]


def test_case_insensitive():
    assert top_k_words("Go go GO! Stop.", 5) == [("go", 3), ("stop", 1)]


def test_ties_broken_alphabetically():
    assert top_k_words("pear apple banana", 3) == [
        ("apple", 1),
        ("banana", 1),
        ("pear", 1),
    ]


def test_punctuation_and_digits_split_words():
    assert top_k_words("end. end, end!2end", 1) == [("end", 4)]


def test_apostrophes_stay_in_words():
    assert top_k_words("don't stop, don't", 1) == [("don't", 2)]


def test_k_larger_than_distinct_words():
    assert top_k_words("a b a", 10) == [("a", 2), ("b", 1)]


def test_empty_text():
    assert top_k_words("", 3) == []


def test_no_words_only_symbols():
    assert top_k_words("123 !!! ...", 2) == []


def test_k_zero_or_negative():
    assert top_k_words("a b c", 0) == []
    assert top_k_words("a b c", -1) == []


def test_longer_text():
    text = "b a b c a b d"
    assert top_k_words(text, 2) == [("b", 3), ("a", 2)]
