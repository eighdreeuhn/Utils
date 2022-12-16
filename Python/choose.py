from factorial import factorial


def choose(m: int, k: int) -> int:
    return factorial(m)//(factorial(k)*factorial(m-k))
