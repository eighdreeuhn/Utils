from is_prime import is_prime


def prime_factors(n):
    factors = {}
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0:
                factors[i] = 1 if not i in factors else factors[i] + 1
                n = n // i
                break
    return factors


print(is_prime(8276447))
print(prime_factors(9198323463))
