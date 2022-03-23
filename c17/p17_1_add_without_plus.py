"""If you add 2 binary numbers together but forget to carry,
the ith bit in the sum will be 0 only if a and b have the same ith bit
This is a XOR

If you add 2 binary numbers and ONLY carry, the ith bit of the sum will be 1
only if i-1th bit of BOTH a and b have a 1. This is an AND, shifted by 1 bit


"""


def main():
    print(add_(759, 674))


def add_(a, b):
    while b != 0:
        # If you add 2 binary numbers together but forget to carry,
        # the ith bit in the sum will be 0 only if a and b have the
        # same ith bit. This is a XOR
        s = a ^ b

        # If you add 2 binary numbers and ONLY carry, the ith bit of the
        # sum will be 1 only if i-1th bit of BOTH a and b have a 1.
        # This is an AND, shifted by 1 bit
        c = (a & b) << 1

        # iterate
        a, b = s, c
    return a
