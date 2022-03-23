import pdb
import sys
import traceback
import unittest


def main():
    inp_ = "Mr John Smith    "
    out_ = urlify(list(inp_), 13)
    print(f"out_ = {out_}")


def urlify(arr: list, true_len: int):
    space_count = arr[:true_len].count(' ')
    new_idx = true_len + 2*space_count - 1
    for old_idx in range(true_len - 1, -1, -1):
        if arr[old_idx] == ' ':
            arr[new_idx] = '0'
            arr[new_idx - 1] = '2'
            arr[new_idx - 2] = '%'
            new_idx -= 3
        else:
            arr[new_idx] = arr[old_idx]
            new_idx -= 1
    return arr



if __name__ == '__main__':
    try:
        main()
        # unittest.main()
    except Exception as e:
        extype, value, tb = sys.exc_info()
        traceback.print_exc()
        pdb.post_mortem(tb)
