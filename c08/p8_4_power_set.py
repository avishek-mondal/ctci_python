import json
import unittest
from copy import deepcopy


def main():
    unittest.main()
    # print(powerset_recurse_build_up(arr=[1, 2, 3]))


def powerset_recurse(arr: list, idx=None):
    if idx is None:
        idx = len(arr) - 1
    if idx == -1:
        return [[]]
    old_sets = powerset_recurse(arr, idx - 1)
    new_sets = []
    item = arr[idx]
    for old_set in old_sets:
        new_sets.append(old_set)
        new_set = deepcopy(old_set)
        new_set.append(item)
        new_sets.append(new_set)
    return new_sets


def powerset_recurse_build_up(arr: list, idx: int = 0):
    all_subsets = []
    if idx == len(arr):
        all_subsets.append([])
    else:
        old_subsets = powerset_recurse_build_up(arr, idx + 1)
        item = arr[idx]
        for old_set in old_subsets:
            all_subsets.append(old_set)
            new_set = deepcopy(old_set)
            new_set.append(item)
            all_subsets.append(new_set)
    return all_subsets


def powerset_combinatorics(arr: list):
    n = len(arr)
    two_exp_n = 1 << n  # calc 2^n
    all_subsets = []
    for k in range(two_exp_n):
        subset = convert_to_subset(arr, k)
        all_subsets.append(subset)

    return all_subsets


def convert_to_subset(arr: list, x: int):
    subset = []
    idx = 0
    k = x
    while k > 0:
        if k & 1 == 1:
            subset.append(arr[idx])
        idx += 1
        k = k >> 1
    return subset


class PowerSetTests(unittest.TestCase):
    def setUp(self) -> None:
        self.test_cases = [
            (
                [1, 2, 3],
                [
                    [],
                    [
                        1,
                    ],
                    [1, 2],
                    [1, 2, 3],
                    [1, 3],
                    [
                        2,
                    ],
                    [2, 3],
                    [
                        3,
                    ],
                ],  #  noqa
            )
        ]
        self.test_funcs = [
            powerset_recurse,
            powerset_recurse_build_up,
            powerset_combinatorics,
        ]

    def test_powerset_funcs(self):
        for arr, expected in self.test_cases:
            for fn in self.test_funcs:
                with self.subTest(f"Testing func {fn.__name__}", arr=arr):
                    # self.assertCountEqual(expected, fn(arr))  # <- doesn't work
                    j1 = [set(i) for i in expected]
                    res = fn(arr)
                    j2 = [set(i) for i in res]
                    self.assertCountEqual(j1, j2)


if __name__ == "__main__":
    main()
