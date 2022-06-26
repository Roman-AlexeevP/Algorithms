from . import exercises


def test_recursion_positive_pow():
    assert exercises.recursion_pow(2, 5) == pow(2, 5)


def test_recursion_pow_zero_exp():
    assert exercises.recursion_pow(100, 0) == pow(100, 0)


def test_recursion_pow_exp_one():
    assert exercises.recursion_pow(1000, 1) == pow(1000, 1)


def test_recursion_pow_negative_exp():
    assert exercises.recursion_pow(1, -2) == pow(1, -2)


def test_recursion_pow_negative_large_exp():
    assert exercises.recursion_pow(23, -6) == pow(23, -6)


def test_sum_digits_large_number():
    assert exercises.sum_digits(123456789) == 45


def test_sum_digits_small_number():
    assert exercises.sum_digits(11) == 2


def test_sum_digits_one_digit():
    assert exercises.sum_digits(5) == 5


def test_len_iterable_with_only_pop_small():
    n = 100
    iterable = [1 for _ in range(n)]
    assert n == exercises.recursion_len(iterable)


def test_len_iterable_with_only_pop_empty():
    assert exercises.recursion_len([]) == 0

def test_recursion_palindrome():

    assert exercises.recursion_palindrome("abba")
    assert exercises.recursion_palindrome("a")
    assert exercises.recursion_palindrome("aba")
    assert exercises.recursion_palindrome("")
    assert not exercises.recursion_palindrome("acd")
    assert not exercises.recursion_palindrome("acco")