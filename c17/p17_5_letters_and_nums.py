import random
import tlog


def main():
    arr = generate_random_arr(chars=["A", "1"], l=15)
    tlog.info("comparing arr", arr=arr)
    bf = find_longest_sub_arr_bf(arr)
    smart = find_longest_sub_arr_smart(arr)
    tlog.info("brute force", bf=bf)
    tlog.info("smart", smart=smart)
    assert bf == smart


def find_longest_sub_arr_smart(arr):
    deltas = find_deltas(arr)

    start, end = find_longest_match(deltas)
    return arr[start : end + 1]


def find_deltas(arr):
    deltas = []

    delta = 0

    for c in arr:
        if c.isdigit():
            delta -= 1
        elif c.isalpha():
            delta += 1
        deltas.append(delta)
    tlog.info("done with deltas", arr=arr, deltas=deltas)
    return deltas


def find_longest_match(deltas):
    delta_to_start = {0: -1}
    longest_so_far, start, end = 0, 0, len(deltas) - 1

    for i, delta in enumerate(deltas):
        if delta not in delta_to_start:
            delta_to_start[delta] = i
        else:
            cur_del_start = delta_to_start[delta]
            cur_len = i - cur_del_start
            if cur_len > longest_so_far:
                longest_so_far = cur_len
                end = i
                start = cur_del_start
    return start + 1, end


def find_longest_sub_arr_bf(arr):
    for subarr_len in range(len(arr), 1, -1):
        for j in range(len(arr) - subarr_len + 1):
            end = j + subarr_len
            start = j
            if has_equal_letters_numbers(arr=arr, start=start, end=end):
                return arr[start:end]


def has_equal_letters_numbers(arr, start, end):
    count = 0
    for i in range(start, end):
        c = arr[i]
        if c.isdigit():
            count -= 1
        elif c.isalpha():
            count += 1

    return count == 0


def generate_random_arr(chars, l):
    num_chars = random.randint(0, l - 1)
    arr = [chars[0] if i < num_chars else chars[1] for i in range(l)]
    random.shuffle(arr)
    return arr
