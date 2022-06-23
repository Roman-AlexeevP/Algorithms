

def recursion_pow(base, exp):
    # 2^-5 = 1 / 2^5
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp < 0:
        return 1 / recursion_pow(base, -exp)
    return base * recursion_pow(base, exp-1)

