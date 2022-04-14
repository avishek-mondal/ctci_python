import typing as ty


def main():
    matrix = [
        [1, 2, 3, 4, 0],
        [6, 0, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 0, 18, 19, 20],
        [21, 22, 23, 24, 25],
    ]
    expected_matrix = [
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [11, 0, 13, 14, 0],
        [0, 0, 0, 0, 0],
        [21, 0, 23, 24, 0],
    ]

    ans = zero_matrix(matrix)
    print(ans)
    assert expected_matrix == ans


def zero_matrix(matrix: ty.List[ty.List[int]]) -> ty.List[ty.List[int]]:
    R = len(matrix)
    C = len(matrix[0])

    first_row_has_zero = False
    for c in range(C):
        if matrix[0][c] == 0:
            first_row_has_zero = True
            break

    first_col_has_zero = False
    for r in range(R):
        if matrix[r][0] == 0:
            first_col_has_zero = True
            break

    for r in range(1, R):
        for c in range(1, C):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0

    for r in range(R):
        if matrix[r][0] == 0:
            for c in range(1, C):
                matrix[r][c] = 0

    for c in range(C):
        if matrix[0][c] == 0:
            for r in range(1, R):
                matrix[r][c] = 0

    if first_col_has_zero:
        for r in range(R):
            matrix[r][0] = 0

    if first_row_has_zero:
        for c in range(C):
            matrix[0][c] = 0

    return matrix
