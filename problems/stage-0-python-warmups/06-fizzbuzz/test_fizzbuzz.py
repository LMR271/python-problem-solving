from fizzbuzz import fizzbuzz

def test_first_five():
    assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]

def test_fizzbuzz_at_15():
    result = fizzbuzz(15)
    assert len(result) == 15
    assert result[14] == "FizzBuzz"
    assert result[8] == "Fizz"
    assert result[9] == "Buzz"

def test_numbers_are_strings():
    assert fizzbuzz(1) == ["1"]

def test_zero():
    assert fizzbuzz(0) == []
