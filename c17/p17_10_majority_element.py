"""A majority element is an element that makes up more than half of the items
in an array.

Given an array of positive integers, find the majority element. If there is no
majority element, return -1, in O(N) time and O(1) space

"""


def main():
    arr = [1, 2, 5, 9, 5, 5, 5, 9, 5]
    bf = find_majority_elem_bf(arr)
    # print(bf)
    smart = find_majority_elem_smart(arr)
    assert smart == bf


def find_majority_elem_smart(arr):
    candidate = get_candidate(arr)
    return candidate if validate(arr, candidate) else -1


def get_candidate(arr):
    majority = 0
    cnt = 0
    for x in arr:
        if cnt == 0:
            majority = x
        if x == majority:
            cnt += 1
        else:
            cnt -= 1
    return majority


def find_majority_elem_bf(arr):
    for x in arr:
        if validate(arr, x):
            return x

    return -1


def validate(arr, x):
    n = len(arr)
    cnt = 0
    for i in arr:
        if x == i:
            cnt += 1

    return cnt > n // 2
