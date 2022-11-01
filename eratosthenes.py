#   Sieve of Eratosthenes method for generating primes up to n     #


def eratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while p**2 <= n:
        if prime[p]:
            for i in range(p**2, n + 1, p):
                prime[i] = False
        p += 1
    prime = [n for n in range(1, n) if prime[n]]
    return prime


print(eratosthenes(10000))