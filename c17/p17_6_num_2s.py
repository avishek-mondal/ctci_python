import math
import tlog


def main():
    num = 121432
    print(round_up_and_down(num, 0))
    print(count_digits_in_range(num=num, digit=2))


def count_digits_in_range(num, digit):
    l = len(str(num))
    count = 0
    for i in range(l):
        count += count_digits_at_digit(num=num, d=i, digit_to_count=digit)
    return count


def count_digits_at_digit(num, d, digit_to_count):
    round_up, round_down = round_up_and_down(num, d)
    pow_10 = math.pow(10, d)

    digit = (num // pow_10) % 10
    right = num % pow_10
    tlog.info(f"num = {num}, d={d}, digit={digit}, right = {right}")

    if digit > digit_to_count:
        count = round_up / 10
    elif digit < digit_to_count:
        count = round_down / 10
    else:
        count = round_down / 10 + right + 1
    tlog.info(f"count = {count}")
    return count


def round_up_and_down(num, d):
    next_10 = math.pow(10, d + 1)
    round_down = num - num % next_10
    round_up = round_down + next_10
    return round_up, round_down
