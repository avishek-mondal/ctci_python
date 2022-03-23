from c17.assorted_methods import (generate_random_matrix,
                                  print_submatrix_from_size)

WHITE = 1
BLACK = 0


def main():
    matrix = generate_random_matrix(N=100, min_=BLACK, max_=WHITE)
    # pprint_matrix(matrix)
    row, col, size = find_square_brute(matrix)
    print_submatrix_from_size(matrix, row, col, size)

    row, col, size = find_square_efficient(matrix)
    print_submatrix_from_size(matrix, row, col, size)


def find_square_efficient(matrix):
    processed_matrix = process_matrix(matrix)
    N = len(matrix)
    for size in range(N, 0, -1):
        square = find_square_with_size(
            processed_matrix, size, is_square_fn=is_square_efficient
        )
        if square:
            return square


def is_square_efficient(matrix, row, col, size):
    """O(1) method of confirming if there is a square of size=size with top left
    in matrix[row][col]

    Args:
        matrix: the PROCESSED matrix
        row: top left
        col: col
        size: size

    Returns:
        boolean in O(1) time
    """
    top_left_right_zeros, top_left_below_zeros = matrix[row][col]
    _, top_right_below_zeros = matrix[row][col + size - 1]
    bottom_left_right_zeros, _ = matrix[row + size - 1][col]

    if (
        top_left_below_zeros < size
        or top_left_right_zeros < size
        or top_right_below_zeros < size
        or bottom_left_right_zeros < size
    ):
        return False
    return True


def process_matrix(matrix):
    N = len(matrix)
    processed = [[None for c in range(N)] for r in range(N)]
    for row in range(N - 1, -1, -1):
        for col in range(N - 1, -1, -1):
            right_zeros = 0
            below_zeros = 0

            # only need to process cell if it is a black cell
            if matrix[row][col] == BLACK:
                right_zeros += 1
                below_zeros += 1

                if col < N - 1:
                    prev_right_zeros, _ = processed[row][col + 1]
                    right_zeros += prev_right_zeros

                if row < N - 1:
                    _, prev_below_zeros = processed[row + 1][col]
                    below_zeros += prev_below_zeros
            processed[row][col] = (right_zeros, below_zeros)
    return processed


def find_square_brute(matrix):
    for size in range(len(matrix), 0, -1):
        square = find_square_with_size(
            matrix, size=size, is_square_fn=is_square_naive
        )
        if square:
            return square


def find_square_with_size(matrix, size, is_square_fn):
    N = len(matrix)
    count = N - size + 1
    for row in range(count):
        for col in range(count):
            if is_square_fn(matrix, row, col, size):
                return (row, col, size)


def is_square_naive(matrix, row, col, size):
    """Checks in O(N) time if there is a square with all black border

    with top left at (row, col) of size=size

    Args:
        matrix: the matrix
        row: the row
        col: col position
        size: the size of square

    Returns:
        boolean
    """
    # check top and bottom border
    for idx in range(size):
        if matrix[row][col + idx] == WHITE:
            return False
        if matrix[row + size - 1][col + idx] == WHITE:
            return False

    # check left and right border
    for idx in range(1, size - 1):
        if matrix[row + idx][col] == WHITE:
            return False

        if matrix[row + idx][col + size - 1] == WHITE:
            return False

    return True


