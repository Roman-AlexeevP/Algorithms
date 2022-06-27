# Возведение в степень
def recursion_pow(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp < 0:
        return 1 / recursion_pow(base, -exp)
    return base * recursion_pow(base, exp-1)


# Сумма цифр
def sum_digits(number):
    if abs(number) < 10:
        return number
    return number % 10 + sum_digits(number // 10)


# расчёт длины списка, для которого разрешена только одна операция удаления первого элемента pop(0)
def recursion_len(iterable):
    element = iterable.pop(0)
    if element is None:
        return 0
    return 1 + recursion_len(iterable)


# проверка, является ли строка палиндромом;
def recursion_palindrome(string: str) -> bool:
    length = len(string)
    if length == 0 or length == 1:
        return True
    begin_equal_end = string[0] == string[-1]
    return begin_equal_end and recursion_palindrome(string[1:-1])


# печать только чётных значений из списка
def print_even_values(iterable):
    if len(iterable) == 0:
        return None
    value = iterable.pop()
    if value % 2 == 0:
        print(value, end=", ")
    return print_even_values(iterable)


# печать элементов списка с чётными индексами
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



