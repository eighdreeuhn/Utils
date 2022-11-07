def prime_factors(n):
    factors, f = {}, 2
    while f <= n:
        while n%f == 0:
            if f in factors:
                factors[f] += 1
                n /= f
            else:
                factors[f] = 1
                n /= f
        f += 1
    return factors


print(prime_factors(9192777468))
