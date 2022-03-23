from tkinter import N


UNFILLED_VAL = -1


def main():
    vals = [1, 2, 3, 4, 5, 6]
    for n in vals:
        print(count_ways(n))


def count_ways(n: int):
    if n <= 0:
        raise ValueError
    memo = [UNFILLED_VAL] * (n + 1)
    memo[0] = 1
    return count_ways_memo(n, memo)


def count_ways_memo(n: int, memo: list):
    if n < 0:
        return 0
    if memo[n] != UNFILLED_VAL:
        return memo[n]

    memo[n] = (
        count_ways_memo(n - 1, memo)
        + count_ways_memo(n - 2, memo)
        + count_ways_memo(n - 3, memo)
    )
    return memo[n]
