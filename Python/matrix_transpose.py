# transpose a 2d list clockwise #

def transpose(lst: list) -> list:
    return [[lst[j][i] for j in range(len(lst))] for i in range(len(lst[0]))]


mat = [
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3],
    [1, 2, 3]
]
print(transpose(mat))
