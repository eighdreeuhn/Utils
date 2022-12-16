from functools import reduce


def frequency(word):
    return reduce(lambda freq, char: {**freq, char: freq[char]+1} if char in freq else {**freq, char: 1}, [*word], {})
