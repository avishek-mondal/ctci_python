import typing as ty
from random import randint

import tlog


class PartitionResult:
    def __init__(self, left_size: int, middle_size: int):
        self.left_size = left_size
        self.middle_size = middle_size


def main():
    n = 20
    k = 5
    arr = [randint(0, 100) for _ in range(n)]
    arr.sort()
    tlog.info("generated arr", arr=arr, k_small=arr[:k])
    print(k_smallest_with_dups(arr, k))


def k_smallest_with_dups(arr, k):
    threshold = rank_with_dups(arr=arr, left=0, right=len(arr) - 1, k=k)
    out = []
    cnt = 0
    for i in arr:
        if i < threshold:
            out.append(i)
            cnt += 1
    if cnt < k:
        for i in arr:
            if i == threshold:
                out.append(i)
    return out


def rank_with_dups(arr: ty.List[int], left: int, right: int, k: int):
    pivot = arr[randint(left, right)]
    partition_res: PartitionResult = partition_with_dups(
        arr=arr, start=left, end=right, pivot=pivot
    )
    left_size = partition_res.left_size
    middle_size = partition_res.middle_size

    if k < left_size:  # rank k in on left
        return rank_with_dups(
            arr=arr, left=left, right=left + left_size - 1, k=k
        )
    elif k < left_size + middle_size:  # rank k in in the middle
        return pivot
    else:  # rank k is in the right
        return rank_with_dups(
            arr=arr,
            left=left + left_size + middle_size,
            right=right,
            k=k - left_size - middle_size,
        )


def partition_with_dups(arr: ty.List[int], start: int, end: int, pivot: int):
    left, right = start, end
    middle = start

    while middle <= right:
        if arr[middle] < pivot:
            arr[middle], arr[left] = arr[left], arr[middle]
            middle += 1
            left += 1
        elif arr[middle] > pivot:
            arr[middle], arr[right] = arr[right], arr[middle]
            right -= 1
        else:
            middle += 1

    return PartitionResult(
        left_size=left - start, middle_size=right - left + 1
    )


def rank_no_dups(arr: ty.List, start: int, end: int, k: int):
    pivot = arr[randint(start, end)]
    left_end = partition_no_dups(arr=arr, left=start, right=end, pivot=pivot)
    left_size = left_end - start + 1
    if k == left_size - 1:
        return max(arr[start : left_end + 1])
    elif k < left_size:
        return rank_no_dups(arr=arr, start=start, end=left_end, k=k)
    else:
        return rank_no_dups(
            arr=arr, start=left_end + 1, end=end, k=k - left_size
        )


def partition_no_dups(arr: ty.List, left: int, right: int, pivot: int):
    while left <= right:
        if arr[left] > pivot:
            # left more than pivot, swap around
            swap(arr, left, right)
            right -= 1
        elif arr[right] <= pivot:
            # right is in incorrect place
            swap(arr, left, right)
            left += 1
        else:
            left += 1
            right -= 1
    left_end = left - 1
    return left_end


def swap(arr, left, right):
    arr[left], arr[right] = arr[right], arr[left]
