import math
import typing as ty
import unittest


def main():
    matrix = [[1, 1, 0], [0, 1, 1], [0, 0, 1]]
    print(rotate_matrix(matrix))


def rotate_matrix(matrix: ty.List[ty.List]) -> ty.List[ty.List]:
    if len(matrix) != len(matrix[0]):
        raise Exception('need a square matrix')
    n = len(matrix)
    num_layers = math.ceil(n/2)

    for layer in range(num_layers):
        first = layer
        last = n - layer - 1
        temp = [0 for i in range(first, last)]
        for i in range(first, last):
            offset = i - first

            # store top as temp
            temp = matrix[first][i]

            # top[i] = left[i]
            matrix[first][i] = matrix[last - offset][first]

            # left[i] = bottom[i]
            matrix[last - offset][first] = matrix[last][last - offset]

            # bottom[i] = right[i]
            matrix[last][last - offset] = matrix[i][last]

            # top = temp
            matrix[i][last] = temp

    return matrix


class Test(unittest.TestCase):

    test_cases = [
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        (
            [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            [
                [21, 16, 11, 6, 1],
                [22, 17, 12, 7, 2],
                [23, 18, 13, 8, 3],
                [24, 19, 14, 9, 4],
                [25, 20, 15, 10, 5],
            ],
        ),
    ]

    def test_rotate_matrix(self):
        for matrix, expected in self.test_cases:
            self.assertEqual(expected, rotate_matrix(matrix))

if __name__ == '__main__':
    unittest.main()
