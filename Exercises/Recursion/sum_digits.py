
def sum_digits(number):
    if abs(number) < 10:
        return number
    return number % 10 + sum_digits(number // 10)

