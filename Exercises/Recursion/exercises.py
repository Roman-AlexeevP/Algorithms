def recursion_pow(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp < 0:
        return 1 / recursion_pow(base, -exp)
    return base * recursion_pow(base, exp-1)


def sum_digits(number):
    if abs(number) < 10:
        return number
    return number % 10 + sum_digits(number // 10)


def recursion_len(iterable):
    element = iterable.pop(0)
    if element is None:
        return 0
    return 1 + recursion_len(iterable)

def recursion_palindrome(string: str) -> bool:
    length = len(string)
    if length == 0 or length == 1:
        return True
    begin_equal_end = string[0] == string[-1]
    return begin_equal_end and recursion_palindrome(string[1:-1])

def print_even_values(iterable):
    if len(iterable) == 0:
        return None
    value = iterable.pop()
    if value % 2 == 0:
        print(value, end=", ")
    return print_even_values(iterable)

def print_even_indexes(iterable):
    lentgh = len(iterable)
    if lentgh == 0:
        return None
    if lentgh == 1:
        print(iterable.pop(0), end=', ')
        return None
    print(iterable.pop(0), end=', ')
    iterable.pop(0)
    return print_even_indexes(iterable)



