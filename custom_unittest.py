import unittest
import typing as ty


class CustomUnittest(unittest.TestCase):
    def __init__(self, test_fns: ty.List, test_cases):
        self.test_fns = test_fns
        self.test_cases = test_cases

    def test_the_testcases(self):
        for test_fn in self.test_fns:
            for test_args, expected in self.test_cases:
                with self.subTest(
                    f"Testing",
                    test_fn=test_fn,
                    test_args=test_args,
                    expected=expected,
                ):
                    self.assertEqual(test_fn(*test_args), expected)
