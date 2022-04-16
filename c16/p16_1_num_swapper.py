from custom_unittest import CustomUnittest
from run_main import breakpoint_on_error
import unittest


@breakpoint_on_error
def num_swapper(a, b):
    a = a - b
    b = a + b
    a = b - a
    return a, b

class NumSwapTest(CustomUnittest):
    test_fns = [num_swapper]
    custom_test_cases = [
        ((1, 3), (3, 1))
    ]


if __name__ == "__main__":
    unittest.main()
