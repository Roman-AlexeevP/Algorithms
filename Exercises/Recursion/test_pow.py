def test_recursion_positive_pow():

    assert recursion_pow(2, 5) == pow(2, 5)

def test_recursion_pow_zero_exp():

    assert recursion_pow(100, 0) == pow(100, 0)

def test_recursion_pow_exp_one():

    assert recursion_pow(1000, 1) == pow(1000, 1)

def test_recursion_pow_negative_exp():

    assert recursion_pow(1, -2) == pow(1, -2)

def test_recursion_pow_negative_large_exp():

    assert recursion_pow(23, -6) == pow(23, -6)