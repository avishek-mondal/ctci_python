import unittest


def main():
    unittest.main()


def recursive_mult_memo(a: int, b: int):
    bigger = a if a > b else b
    smaller = a if a < b else b
    memo = [0 for _ in range(smaller + 1)]
    return recursive_mult_memo_helper(smaller, bigger, memo)


def recursive_mult_memo_helper(smaller: int, bigger: int, memo: list):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger
    if memo[smaller] > 0:
        return memo[smaller]

    divide_2 = smaller >> 1
    side1 = recursive_mult_memo_helper(divide_2, bigger, memo)
    side2 = side1
    if smaller % 2 == 1:
        side2 = recursive_mult_memo_helper(smaller - divide_2, bigger, memo)
    memo[smaller] = side1 + side2
    return memo[smaller]


def recursive_mul_handle_odd(a: int, b: int):
    bigger = a if a > b else b
    smaller = a if a < b else b
    return recursive_mul_handle_odd_helper(smaller, bigger)


def recursive_mul_handle_odd_helper(smaller, bigger):
    if smaller == 0:
        return 0
    if smaller == 1:
        return bigger

    s = smaller >> 1
    half_prod = recursive_mul_handle_odd_helper(s, bigger)

    if smaller % 2 == 0:
        # even case
        return half_prod + half_prod
    else:
        # odd case
        return half_prod + half_prod + bigger


class RecursiveMultiplyTest(unittest.TestCase):
    def setUp(self) -> None:
        self.test_cases = [(3, 4), (5, 6), (234, 391), (33243, 23)]
        self.test_funcs = [recursive_mult_memo, recursive_mul_handle_odd]

    def test_recursive_fns(self):
        for a, b in self.test_cases:
            for fn in self.test_funcs:
                self.assertEqual(fn(a, b), a * b)


if __name__ == "__main__":
    main()
