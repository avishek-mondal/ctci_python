import typing as ty

NOT_SET = -1


def main():
    test_cases = [
        ([30, 15, 60, 75, 45, 15, 15, 45], 180),
        ([75, 105, 120, 75, 90, 135], 330),
    ]
    for arr, expected in test_cases:
        # actual = get_max_minutes_memo(arr)
        actual = get_max_minutes_iterative(arr)
        assert actual == expected


def get_max_minutes_iterative(arr: ty.List):
    n = len(arr)
    one_away, two_away = 0, 0
    for i in range(n - 1, -1, -1):
        best_with = arr[i] + two_away
        best_without = one_away
        current = max(best_with, best_without)
        one_away, two_away = current, one_away
    return one_away


def get_max_minutes_memo(arr: ty.List):
    memo = [NOT_SET for _ in range(len(arr))]
    return get_max_minutes_memo_helper(arr=arr, idx=0, memo=memo)


def get_max_minutes_memo_helper(arr: ty.List, idx: int, memo: ty.List[int]):
    """Using a memo, make a decision at each point whether to take the
    appointment or not take the appointment

    O(N) runtime and O(N) space

    Args:
        arr: array of appointments
        idx: index to check
        memo: caching

    Returns:
        max minutes
    """

    if idx >= len(arr):
        return 0

    if memo[idx] == NOT_SET:
        best_with = arr[idx] + get_max_minutes_memo_helper(
            arr=arr, idx=idx + 2, memo=memo
        )
        best_without = get_max_minutes_memo_helper(
            arr=arr, idx=idx + 1, memo=memo
        )
        memo[idx] = max(best_with, best_without)

    return memo[idx]
