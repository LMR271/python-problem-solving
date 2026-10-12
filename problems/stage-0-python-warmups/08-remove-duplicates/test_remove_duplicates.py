from remove_duplicates import remove_duplicates

def test_numbers():
    assert remove_duplicates([1, 2, 1, 3, 2]) == [1, 2, 3]

def test_keeps_first_occurrence_order():
    assert remove_duplicates(["b", "a", "b"]) == ["b", "a"]
    assert remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]

def test_no_duplicates():
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]

def test_empty():
    assert remove_duplicates([]) == []
