"""Implement algo to print all valid combinations of n paris of parenthesis

Brute force:
Insert a parenthesis inside every existing pair of parentheses as well as the
beginning of the string. Need to check duplicates
"""
import typing as ty


def main():
    n = [i for i in range(5)]
    test_funcs = [generate_parens_bf, generate_parens_from_scratch]
    for fn in test_funcs:
        for num in n:
            res = fn(num)
            print(f"fn = {fn.__name__}, len(res) = {len(res)}")
            print(res)


def generate_parens_from_scratch(n: int):
    """Build from scratch, don't need to check duplicates

    1. Add left and right parents, as long as expression stays valid

    2.On each recursive call, we have the index for a particular character in
    the string.
        a. Need to select either a left parenthesis or a right paren
        b. When can you use a left/right paren?
            i. Left paren => As long as you haven't used up all n
            ii. Right paren => as long as there aren't more right parens than
            left parens
        c. Just need to keep track of left and right parens
    Args:
        n (int): _description_
    """
    initial_arr = [""] * n * 2
    res = []
    add_paren_from_scratch(
        char_arr=initial_arr, left_parens=n, right_parens=n, idx=0, res=res
    )
    return res


def add_paren_from_scratch(
    char_arr: ty.List,
    left_parens: int,
    right_parens: int,
    idx: int,
    res: ty.List,
):
    if left_parens < 0 or right_parens < left_parens:
        return

    if left_parens == 0 and right_parens == 0:
        res.append("".join(char_arr))
    else:
        # add left and recurse
        char_arr[idx] = "("
        add_paren_from_scratch(
            char_arr=char_arr,
            left_parens=left_parens - 1,
            right_parens=right_parens,
            idx=idx + 1,
            res=res,
        )
        char_arr[idx] = ")"

        # add right and recurse
        add_paren_from_scratch(
            char_arr=char_arr,
            left_parens=left_parens,
            right_parens=right_parens - 1,
            idx=idx + 1,
            res=res,
        )


def generate_parens_bf(n: int):
    set_ = set()
    if n == 0:
        set_.add("")

    if n > 0:
        prev_set = generate_parens_bf(n - 1)
        for string_ in prev_set:
            for i in range(len(string_)):
                if string_[i] == "(":
                    new_elem = insert_paren_at(string_, i + 1)
                    set_.add(new_elem)

            set_.add(f"(){string_}")
    return set_


def insert_paren_at(s: str, i: int):
    return f"{s[:i]}(){s[i:]}"
