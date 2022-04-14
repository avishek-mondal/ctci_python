from dataclasses import dataclass

import tlog
from c17.assorted_methods import generate_random_matrix, pprint_matrix


@dataclass
class SubMatrix:
    start_row: int = 0
    end_row: int = 0
    start_col: int = 0
    end_col: int = 0
    sum_: int = 0

    def print_submatrix_from_endpoints(self, matrix):
        print(f"Sum = {self.sum_}")
        for r_ in range(self.start_row, self.end_row + 1):
            print(matrix[r_][self.start_col : self.end_col + 1])


@dataclass
class LinearRange:
    start: int = 0
    end: int = 0
    sum_: int = 0


def main():
    matrix = generate_random_matrix(N=10, min_=-5, max_=5)
    pprint_matrix(matrix)
    sub_matrix = find_max_sub_matrix_sum_through(matrix)
    sub_matrix.print_submatrix_from_endpoints(matrix=matrix)

    sub_matrix = find_max_sub_matrix_optimal(matrix)
    sub_matrix.print_submatrix_from_endpoints(matrix=matrix)


def find_max_sub_matrix_optimal(matrix) -> SubMatrix:
    R = len(matrix)
    C = len(matrix[0])
    best_sub_matrix = SubMatrix(sum_=-float("inf"))
    for row_start in range(R):

        # partial_sum[col] is basically sum of matrix[row_start, col] through
        # to matrix[row_end, col]
        partial_sum = [0 for _ in range(C)]
        for row_end in range(row_start, R):

            # the following allows use to reuse computation done in previous
            # iteration
            for i in range(C):
                partial_sum[i] += matrix[row_end][i]

            linear_range: LinearRange = get_max_subarray_range(partial_sum)
            if linear_range.sum_ > best_sub_matrix.sum_:
                best_sub_matrix = SubMatrix(
                    start_row=row_start,
                    end_row=row_end,
                    start_col=linear_range.start,
                    end_col=linear_range.end,
                    sum_=linear_range.sum_,
                )
    return best_sub_matrix


def get_max_subarray_range(arr) -> LinearRange:
    best_range = LinearRange(sum_=-float("inf"))
    start = 0
    sum_so_far = 0

    for idx in range(len(arr)):
        sum_so_far += arr[idx]
        if sum_so_far > best_range.sum_:
            best_range = LinearRange(start=start, end=idx, sum_=sum_so_far)

        if sum_so_far < 0:
            # reset
            start = idx + 1
            sum_so_far = 0

    return best_range


def find_max_sub_matrix_sum_through(matrix):
    """O(N^4) way of getting max sub matrix

    memor is O(N^2)

    Args:
        matrix: the matrix

    Returns:
        sub_matrix
    """

    sum_through = pre_compute(matrix)
    best_sub_matrix = SubMatrix()
    R = len(matrix)
    C = len(matrix[0])
    for row_start in range(R):
        for row_end in range(row_start, R):
            for col_start in range(C):
                for col_end in range(col_start, C):
                    sum_so_far = compute_sum(
                        sum_through,
                        row_start=row_start,
                        row_end=row_end,
                        col_start=col_start,
                        col_end=col_end,
                    )
                    if sum_so_far > best_sub_matrix.sum_:
                        best_sub_matrix = SubMatrix(
                            start_row=row_start,
                            end_row=row_end,
                            start_col=col_start,
                            end_col=col_end,
                            sum_=sum_so_far,
                        )
    return best_sub_matrix


def pre_compute(matrix):
    R = len(matrix)
    C = len(matrix[0])
    sum_through = [[0 for _ in range(C)] for _ in range(R)]
    for row in range(R):
        for col in range(C):
            left = sum_through[row][col - 1] if col > 0 else 0
            top = sum_through[row - 1][col] if row > 0 else 0
            overlap = (
                sum_through[row - 1][col - 1] if row > 0 and col > 0 else 0
            )
            sum_through[row][col] = left + top - overlap + matrix[row][col]
    return sum_through


def compute_sum(sum_through, row_start, row_end, col_start, col_end):
    diagonal = (
        sum_through[row_start - 1][col_start - 1]
        if row_start > 0 and col_start > 0
        else 0
    )

    left = sum_through[row_end][col_start - 1] if col_start > 0 else 0
    top = sum_through[row_start - 1][col_end] if row_start > 0 else 0
    full = sum_through[row_end][col_end]
    return full - left - top + diagonal
