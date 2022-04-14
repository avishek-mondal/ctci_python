"""Find volume of histogram
"""
import typing as ty


def main():
    hist = [0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0]
    # print(find_volume_brute(hist))
    # print(find_volume_monotonic_stack(hist))
    print(find_volume_two_sweeps(hist))


def find_volume_two_sweeps(hist):
    """Following steps:

    1. Sweep left to right, tracking the max height you've seen and setting
    left max

    2. Sweep right to left, tracking the max height you've seen and setting
    right max

    3. Sweep across the histogram, computing the minimum of the left max and
    right max for each index

    4. Sweep across the histogram, computing the delta between each minimum and
    the bar. Total area with be total of these deltas

    Args:
        total volume
    """
    left_maxes = []
    left_max = hist[0]
    for v in hist:
        left_max = max(left_max, v)
        left_maxes.append(left_max)

    tot = 0

    right_max = 0

    for i in range(len(hist) - 1, -1, -1):
        right_max = max(right_max, hist[i])
        second_tallest = min(right_max, left_maxes[i])

        if second_tallest > hist[i]:
            tot += second_tallest - hist[i]

    return tot


def find_volume_monotonic_stack(hist):
    """Use a monotonic stack

    This will be a continually decreasing stack

    https://medium.com/techtofreedom/algorithms-for-interview-2-monotonic-stack-462251689da8

    Args:
        max volume
    """
    stack = []  # continually decreasing stack
    tot = 0

    for i, v in enumerate(hist):
        while stack and hist[stack[-1]] < v:
            idx_popped = stack.pop()

            if not stack:
                break
            height = min(v, hist[stack[-1]]) - hist[idx_popped]
            length = i - stack[-1] - 1
            tot += height * length
        stack.append(i)
    return tot


def find_volume_brute(hist: ty.List[int]):
    start = 0
    end = len(hist) - 1
    idx_of_max = find_idx_of_max(hist, start=start, end=end)
    left_vol = sub_graph_vol(
        hist=hist, start=start, end=idx_of_max, is_left=True
    )
    right_vol = sub_graph_vol(
        hist=hist, start=idx_of_max, end=end, is_left=False
    )
    return left_vol + right_vol


def sub_graph_vol(hist: ty.List[int], start: int, end: int, is_left: bool):
    if start >= end:
        return 0

    tot = 0
    if is_left:
        # if is_left, end is the tallest
        second_tallest = find_idx_of_max(hist=hist, start=start, end=end - 1)
        tot += sub_graph_vol(
            hist=hist, start=start, end=second_tallest, is_left=is_left
        )
        tot += vol_between(hist=hist, start=second_tallest, end=end)
    else:
        # now, start is the tallest
        second_tallest = find_idx_of_max(hist=hist, start=start + 1, end=end)
        tot += sub_graph_vol(
            hist=hist, start=second_tallest, end=end, is_left=is_left
        )
        tot += vol_between(hist=hist, start=start, end=second_tallest)
    return tot


def find_idx_of_max(hist: ty.List, start, end):
    idx_of_max = start
    for i in range(start + 1, end + 1):
        if hist[i] > hist[idx_of_max]:
            idx_of_max = i
    return idx_of_max


def vol_between(hist: ty.List, start: int, end: int):
    if start >= end:
        return 0
    smaller = min(hist[start], hist[end])

    tot = 0
    for i in range(start + 1, end):
        tot += smaller - hist[i]

    return tot
