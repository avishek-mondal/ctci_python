import unittest
import random
import tlog


def main():
    n = 8
    arr = [i for i in range(n)]
    max_len = len(bin(arr[-1]))
    bin_arr = [bin(i)[2:].zfill(max_len) for i in arr]
    lsb = len(bin_arr[0]) - 1
    tlog.info("lsb", lsb=lsb)
    bin_arr.pop()
    byte_arr = find_missing_helper(bin_arr, lsb)
    print(int("".join(byte_arr), base=2))


def find_missing(arr):
    lsb = len(arr[0]) - 1
    byte_arr = find_missing_helper(arr, lsb)
    return byte_arr


def find_missing_helper(arr, col) -> list:
    if len(arr) == 0 or col < 0:
        return ["0"]

    zero_bits, one_bits = [], []
    for in_ in arr:
        if in_[col] == "0":
            zero_bits.append(in_)
        else:
            one_bits.append(in_)

    tlog.info("arrs", zero_bits=zero_bits, one_bits=one_bits, col=col)
    if len(zero_bits) <= len(one_bits):
        tlog.info("Is even!", zero_bits=zero_bits, col=col)
        v = find_missing_helper(zero_bits, col - 1)
        tlog.info("Is even, returned", v=v, col=col)
        v.append("0")
        return v
    else:
        tlog.info("Is odd!", one_bits=one_bits, col=col)
        v = find_missing_helper(one_bits, col - 1)
        tlog.info("Is odd, returned", v=v, col=col)
        v.append("1")
        return v


class MissingNumberTests(unittest.TestCase):
    def test_various_cases(self):
        n = 100
        for _ in range(10):
            arr = [i for i in range(n)]
            max_len = len(bin(arr[-1]))
            test_arr = [bin(i)[2:].zfill(max_len) for i in arr]
            i = random.randint(0, n - 1)
            missing = arr[i]
            test_arr.pop(i)
            byte_arr = find_missing(test_arr)
            with self.subTest(f"Testing", byte_arr=byte_arr, missing=missing):
                actual_missing = int("".join(byte_arr), base=2)
                self.assertEqual(actual_missing, missing)


if __name__ == "__main__":
    unittest.main()
