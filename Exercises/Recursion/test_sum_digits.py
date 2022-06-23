from .sum_digits import sum_digits

def test_sum_digits_large_number():
    assert sum_digits(123456789) == 45

def test_sum_digits_small_number():
    assert sum_digits(11) == 2

def test_sum_digits_one_digit():
    assert sum_digits(5) == 5