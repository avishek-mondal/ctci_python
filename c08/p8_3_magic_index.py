import unittest

NOT_FOUND = -1


def main():
    unittest.main()


def magic_index(arr: list):
    return magic_idx_no_dups(arr, 0, len(arr) - 1)


def magic_idx_no_dups(arr: list, start: int, end: int):
    if end < start:
        return NOT_FOUND
    mid_idx = (start + end) // 2
    mid_val = arr[mid_idx]
    if mid_idx == mid_val:
        return mid_idx
    if mid_val > mid_idx:
        # search left
        return magic_idx_no_dups(arr, start, mid_idx - 1)
    else:
        # search right
        return magic_idx_no_dups(arr, mid_idx + 1, end)


def magic_index_dups(arr: list):
    return magic_idx_dups(arr, 0, len(arr) - 1)


def magic_idx_dups(arr: list, start: int, end: int):
    if end < start:
        return NOT_FOUND

    mid_idx = (start + end) // 2
    mid_val = arr[mid_idx]
    if mid_val == mid_idx:
        return mid_idx

    left_idx = min(mid_val, mid_idx - 1)
    left = magic_idx_dups(arr, start, left_idx)
    if left != NOT_FOUND:
        return left

    right_idx = max(mid_val, mid_idx + 1)
    right = magic_idx_dups(arr, right_idx, end)
    return right


class MagicIndex(unittest.TestCase):
    def setUp(self) -> None:
        self.test_cases_no_dups = [
            ([-14, -12, 0, 1, 2, 5, 9, 10, 23, 25], 5),
            ([-14, -12, 0, 1, 2, 7, 9, 10, 23, 25], NOT_FOUND),
            ([0, 1, 2, 3, 4], 2),
            ([], NOT_FOUND),
        ]
        self.test_funcs = [magic_index]

        self.test_cases_dups = self.test_cases_no_dups + [
            ([-10, -5, 2, 2, 2, 3, 4, 5, 9, 12, 13], 2)
        ]

    def test_no_dupes(self):
        for arr, expected in self.test_cases_no_dups:
            for fn in self.test_funcs:
                with self.subTest("Running subtest", arr=arr, fn=fn):
                    self.assertEqual(fn(arr), expected)

    def test_w_dupes(self):
        for arr, expected in self.test_cases_dups:
            with self.subTest("Running subtest w dupes", arr=arr):
                self.assertEqual(magic_index_dups(arr), expected)


if __name__ == "__main__":
    main()
