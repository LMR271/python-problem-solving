from char_frequency import char_frequency

def test_basic():
    assert char_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}

def test_case_sensitive():
    assert char_frequency("aA") == {"a": 1, "A": 1}

def test_spaces_count():
    assert char_frequency("a a") == {"a": 2, " ": 1}

def test_empty():
    assert char_frequency("") == {}
