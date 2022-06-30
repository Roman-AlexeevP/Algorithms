import copy


def recursion_pow(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp < 0:
        return 1 / recursion_pow(base, -exp)
    return base * recursion_pow(base, exp - 1)


def sum_digits(number):
    if abs(number) < 10:
        return number
    return number % 10 + sum_digits(number // 10)


def recursion_len(iterable):
    local_iterable = list(iterable)
    element = local_iterable.pop(0)
    if element is None:
        return 0
    return 1 + recursion_len(local_iterable)


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
    print_even_values(iterable)


def print_even_indexes(iterable):
    lentgh = len(iterable)
    if lentgh == 0:
        return None
    if lentgh == 1:
        print(iterable.pop(0), end=', ')
        return None
    print(iterable.pop(0), end=', ')
    iterable.pop(0)
    print_even_indexes(iterable)


def recursive_max(iterable):
    if len(iterable) == 1:
        return iterable.pop()
    first_value = iterable.pop()
    second = recursive_max(iterable)
    return first_value if first_value > second else second


def recursive_max_2(iterable, index):
    if index > 0:
        first = iterable[index]
        second = recursive_max_2(iterable, index - 1)
        return first if first > second else second
    return iterable[0]

def find_max(iterable, index, first_max, second_max):
    if index == len(iterable):
        return second_max
    value = iterable[index]
    index += 1
    if value > second_max:
        if value > first_max:
            return find_max(iterable, index, value, first_max)
        return find_max(iterable, index, first_max, value)

    return find_max(iterable, index, first_max, second_max)

def second_max(iterable):
    if len(iterable) == 0 or len(iterable) == 1:
        return None
    local_iterable = list(set(iterable))
    min_value = float("-inf")
    return find_max(local_iterable, 0, min_value, min_value)


