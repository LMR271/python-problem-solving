from running_sum import running_sum

def test_basic():
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]

def test_ones():
    assert running_sum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]

def test_negative():
    assert running_sum([3, -1, 2]) == [3, 2, 4]

def test_single_and_empty():
    assert running_sum([5]) == [5]
    assert running_sum([]) == []
