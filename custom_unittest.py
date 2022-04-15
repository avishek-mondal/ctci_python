import unittest
import typing as ty


class CustomUnittest(unittest.TestCase):
    test_fns: ty.List = []
    custom_test_cases: ty.List = []

    def test_the_testcases(self):
        for test_fn in self.test_fns:
            for test_args, expected in self.custom_test_cases:
                with self.subTest(
                    f"Testing",
                    test_fn_name=test_fn.__name__,
                    test_args=test_args,
                    expected=expected,
                ):
                    self.assertEqual(test_fn(*test_args), expected)
