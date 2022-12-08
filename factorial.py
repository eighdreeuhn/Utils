def factorial(x: int) -> int:
    return 1 if x == 0 else x * factorial(x - 1)
