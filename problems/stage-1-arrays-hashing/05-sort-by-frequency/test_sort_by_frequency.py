from sort_by_frequency import sort_by_frequency

def test_example():
    assert sort_by_frequency([1, 1, 2, 2, 2, 3]) == [3, 1, 1, 2, 2, 2]

def test_tie_larger_first():
    assert sort_by_frequency([2, 3, 1, 3, 2]) == [1, 3, 3, 2, 2]

def test_negative_numbers():
    assert sort_by_frequency([-1, 1, -6, 4, 5, -6, 1, 4, 1]) == [5, -1, 4, 4, -6, -6, 1, 1, 1]

def test_all_same_frequency():
    assert sort_by_frequency([1, 3, 2]) == [3, 2, 1]

def test_empty():
    assert sort_by_frequency([]) == []
