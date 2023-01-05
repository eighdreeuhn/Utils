from math import ceil, sqrt


def is_prime(n: int) -> bool:
    """Improved Primality test"""
    if n < 3 or not n % 2:
        return n == 2
    for i in range(3, ceil(sqrt(n)) + 1, 2):
        if not n % i:
            return False
    return True
