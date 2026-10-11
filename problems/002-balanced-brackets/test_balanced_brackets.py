from balanced_brackets import is_balanced


def test_simple_pairs():
    assert is_balanced("()")
    assert is_balanced("[]")
    assert is_balanced("{}")


def test_nested_and_sequential():
    assert is_balanced("{[()]}")
    assert is_balanced("()[]{}")
    assert is_balanced("(a[b]{c})")


def test_other_characters_ignored():
    assert is_balanced("print(len([1, 2, 3]))")
    assert is_balanced("no brackets here")


def test_empty_string():
    assert is_balanced("")


def test_wrong_order():
    assert not is_balanced("([)]")


def test_wrong_type():
    assert not is_balanced("(]")


def test_unclosed():
    assert not is_balanced("((")
    assert not is_balanced("{[()]")


def test_closing_without_opening():
    assert not is_balanced(")")
    assert not is_balanced("())")
    assert not is_balanced("]{}")
