import random
import tlog
import math


def main():
    n = 20
    a = random.randint(0, n - 1)
    b = random.randint(0, n - 1)
    while a == b:
        b = random.randint(0, n - 1)

    tlog.info(f"expected missing {(a,b)}")
    arr = [i for i in range(n) if i not in (a, b)]
    x, y = find_missing_pair(arr, n)
    tlog.info(f"found missing {(x,y)}")


def find_missing_pair(arr, n):
    s = find_missing_sum(arr, n)
    t = find_missing_sq(arr, n)
    return solve_eqn(s, t)


def solve_eqn(s, t):
    a_ = 2
    b_ = -2 * s
    c_ = s**2 - t
    x = (0.5 / a_) * (-b_ + math.sqrt((b_**2) - (4 * a_ * c_)))
    y = (0.5 / a_) * (-b_ - math.sqrt((b_**2) - (4 * a_ * c_)))
    tlog.info("solved eqn", s=s, t=t, a=a_, b=b_, c=c_, x=x, y=y)
    return x, y


def find_missing_sum(arr, n):
    expected_sum = 0
    actual_sum = 0
    for i in range(n):
        expected_sum += i
    for x in arr:
        actual_sum += x
    dif = expected_sum - actual_sum
    tlog.info(
        "returning sums",
        expected_sum=expected_sum,
        actual_sum=actual_sum,
        dif=dif,
    )
    return dif


def find_missing_sq(arr, n):
    expected_sum = 0
    actual_sum = 0
    for i in range(n):
        expected_sum += i**2
    for x in arr:
        actual_sum += x**2
    dif = expected_sum - actual_sum
    tlog.info(
        "returning squares",
        expected_sum=expected_sum,
        actual_sum=actual_sum,
        dif=dif,
    )
    return dif
