from custom_unittest import CustomUnittest
import unittest


def one_arg(a):
    return f"{str(a)}"


def two_args(a, b):
    return f"{str(a)}{str(b)}"


def another_two_args(a, b):
    return f"{str(a)}{str(b)}"


def three_args(a, b, c):
    return f"{str(a)}{str(b)}{str(c)}"


def another_three_args(a, b, c):
    return f"{str(a)}{str(b)}{str(c)}"


class OneArgsTest(CustomUnittest):
    test_fns = [one_arg]
    custom_test_cases = [
        ([1], "1"),
        ([3], "3"),
    ]
class TwoArgsTest(CustomUnittest):
    test_fns = [two_args, another_two_args]
    custom_test_cases = [
        ([1, 2], "12"),
        ([3, 4], "34"),
    ]


class ThreeArgsTest(CustomUnittest):
    test_fns = [three_args, another_three_args]
    custom_test_cases = [
        ([1, 2, 3], "123"),
        ([3, 4, 5], "345"),
    ]


if __name__ == "__main__":
    unittest.main()
