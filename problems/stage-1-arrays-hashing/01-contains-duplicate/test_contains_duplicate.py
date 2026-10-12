from contains_duplicate import contains_duplicate

def test_has_duplicate():
    assert contains_duplicate([1, 2, 3, 1]) is True

def test_all_unique():
    assert contains_duplicate([1, 2, 3, 4]) is False

def test_many_duplicates():
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True

def test_negative_numbers():
    assert contains_duplicate([-1, 0, -1]) is True

def test_empty_and_single():
    assert contains_duplicate([]) is False
    assert contains_duplicate([7]) is False
