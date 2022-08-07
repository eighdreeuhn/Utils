def is_prime(_p):
    if _p < 2:
        return False
    if _p == 2:
        return True
    for i in range(2, int(_p**0.5) + 1):
        if _p % i == 0:
            return False
    return True


print(is_prime(8))