import random


def pprint_matrix(matrix):
    # arr = [["WHITE" if c == WHITE else "BLACK" for c in row] for row in matrix]
    for row in matrix:
        print(row)


def print_submatrix_from_size(matrix, row, col, size):
    for r_ in range(size):
        print(matrix[row + r_][col : col + size])
    # print(matrix[row : row + size][col : col + size])
    print(f"row = {row}, col = {col}, size = {size}")


def generate_random_matrix(N, min_, max_):
    return [[random.randint(min_, max_) for _ in range(N)] for _ in range(N)]
