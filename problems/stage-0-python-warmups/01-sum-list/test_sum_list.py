from sum_list import sum_list

def test_basic():
    assert sum_list([1, 2, 3]) == 6

def test_negative_numbers():
    assert sum_list([5, -2]) == 3
    assert sum_list([-1, -1]) == -2

def test_single_item():
    assert sum_list([42]) == 42

def test_empty_list():
    assert sum_list([]) == 0
