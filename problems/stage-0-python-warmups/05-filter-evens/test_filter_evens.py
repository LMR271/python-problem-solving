from filter_evens import filter_evens

def test_basic():
    assert filter_evens([1, 2, 3, 4]) == [2, 4]

def test_no_evens():
    assert filter_evens([1, 3, 5]) == []

def test_zero_and_negative():
    assert filter_evens([0, -2, 7]) == [0, -2]

def test_keeps_order_and_duplicates():
    assert filter_evens([4, 2, 4, 1]) == [4, 2, 4]

def test_empty():
    assert filter_evens([]) == []

def test_does_not_change_input():
    data = [1, 2, 3]
    filter_evens(data)
    assert data == [1, 2, 3]
