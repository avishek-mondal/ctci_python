"""Total runtime->

total of n! leaf nodes
tree of depth n
each node does n work

so runtime is O(n*n*n!) = O((n+2)!)
"""

import math
import typing as ty


def main():
    s = "abcd"
    test_funcs = [get_perms_3, get_perms_2, get_perms_1]
    for fn in test_funcs:
        print(f"fn = {fn.__name__}")
        res = fn(s)
        print(
            f"len(s) = {len(s)}, n! = {math.factorial(len(s))}, len(res) = {len(res)}"
        )
        print(res)


def get_perms_1(s: str):
    """Building from permutations of FIRST n-1 chars

    Args:
        s: string

    Returns:
        all permutations
    """
    permutations = []
    if s is None:
        return None

    if len(s) == 0:
        permutations.append(" ")
        return permutations

    first = s[0]  # <-- this is a O(n) operation
    remainder = s[1:]
    perms_from_remainder = get_perms_1(remainder)
    for perm in perms_from_remainder:
        n = len(perm)
        for i in range(n):
            new_perm = perm[:i] + first + perm[i:]
            permutations.append(new_perm)
    return permutations


def get_perms_2(s: str):
    """building from permutations of ALL n-1 char substrings

    P(a1a2a3) = {a1 + P(a2a3)} + {a2 + P(a1a3)} + {a3 + P(a1a2)}

    Args:
        s: string

    Returns:
        permutations
    """
    n = len(s)
    if n == 0:
        return [""]
    res = []

    for i in range(n):
        before = s[:i]
        after = s[i + 1 :]
        partials = get_perms_2(before + after)
        for partial in partials:
            res.append(s[i] + partial)
    return res


def get_perms_3(s: str) -> ty.List[str]:
    """Same as get_perms_2

    Instead of passing permutations back up, push prefixes down

    Args:
        s: string

    Returns:
        list of permutation
    """
    res = []
    get_perms_3_helper(prefix="", remainder=s, res=res)
    return res


def get_perms_3_helper(prefix: str, remainder: str, res: ty.List):
    n = len(remainder)
    if n == 0:
        res.append(prefix)

    for i in range(n):
        to_append = remainder[i]
        prefix_new = f"{prefix}{to_append}"
        remainder_new = remainder[:i] + remainder[i + 1 :]
        get_perms_3_helper(prefix=prefix_new, remainder=remainder_new, res=res)
