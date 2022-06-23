

def recursion_pow(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp < 0:
        return 1 / recursion_pow(base, -exp)
    return base * recursion_pow(base, exp-1)

