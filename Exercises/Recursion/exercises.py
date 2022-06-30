import copy

# Вычисление степени

def recursion_pow(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp < 0:
        return 1 / recursion_pow(base, -exp)
    return base * recursion_pow(base, exp - 1)

# Вычисление суммы цифр числа

def sum_digits(number):
    if abs(number) < 10:
        return number
    return number % 10 + sum_digits(number // 10)

# длина списка

def recursion_len(iterable):
    local_iterable = list(iterable)
    element = local_iterable.pop(0)
    if element is None:
        return 0
    return 1 + recursion_len(local_iterable)

# Палиндром

def recursion_palindrome(string: str) -> bool:
    length = len(string)
    if length == 0 or length == 1:
        return True
    begin_equal_end = string[0] == string[-1]
    return begin_equal_end and recursion_palindrome(string[1:-1])

# Печать четных значений

def print_even_values(iterable):
    if len(iterable) == 0:
        return None
    value = iterable.pop()
    if value % 2 == 0:
        print(value, end=", ")
    print_even_values(iterable)

# Печать значений с четным индексом

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

# Поиск второго максимума с повторяющимися элементами

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

# Поиск всех файлов в каталогах и подкаталогах

import os

def print_all_files(path):
    if not os.path.isdir(path):
        return None
    recursive_print(path, os.listdir(path))


def recursive_print(path, objects):
    if len(objects) == 0:
        return None
    object_path = path + objects.pop()
    if os.path.isdir(object_path):
        dir_path = f"{object_path}/"
        recursive_print(dir_path, os.listdir(dir_path))
    if os.path.isfile(object_path):
        print(object_path)
    recursive_print(path, objects)


