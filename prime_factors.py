from gmpy2 import next_prime
from is_prime import is_prime
from math import sqrt, ceil, floor,log

def prime_factors(n):
    factors, f = {}, 2
    while f <= n:
        while n % f == 0:
            if f in factors:
                factors[f] += 1
                n /= f
            else:
                factors[f] = 1
                n /= f
        f += 1
    return factors


def prime_factors_set(m):
    facts = set()
    f = 3
    if m % 2 == 0:
        facts.add(2)
        m /= 2
    while f <= m:
        if m % f == 0:
            facts.add(f)
        f = next_prime(f)
    return facts


print(prime_factors_set(1234567890))
# print(prime_factors(1234567890))
