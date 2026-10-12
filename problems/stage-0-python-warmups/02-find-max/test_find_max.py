from find_max import find_max

def test_basic():
    assert find_max([3, 7, 2]) == 7

def test_max_at_start_and_end():
    assert find_max([9, 1, 2]) == 9
    assert find_max([1, 2, 9]) == 9

def test_all_negative():
    assert find_max([-5, -1, -9]) == -1

def test_single_item():
    assert find_max([4]) == 4

def test_empty_list():
    assert find_max([]) is None
