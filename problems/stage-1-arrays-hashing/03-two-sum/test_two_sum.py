from two_sum import two_sum

def test_basic():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_not_at_start():
    assert two_sum([3, 2, 4], 6) == [1, 2]

def test_same_value_twice():
    assert two_sum([3, 3], 6) == [0, 1]

def test_cannot_use_same_index_twice():
    assert two_sum([3, 5, 1], 6) == [1, 2]

def test_negative_numbers():
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]
