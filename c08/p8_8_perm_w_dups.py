import math


def main():
    strings = ["aaaaaaaaa", "abc", "ffffabc"]
    for s in strings:
        res = get_perms(s)
        print(f"res = {res}")
        print(
            (f"len(s) = {len(s)}, n! = {math.factorial(len(s))}, "
             f"len(res) = {len(res)}, len(set(res))={len(set(res))} ")
        )


def get_perms(s: str):
    char_count_map = get_char_count_map(s)
    res = []
    generate_perms(
        char_count_map=char_count_map, prefix="", len_remaining=len(s), res=res
    )
    return res


def get_char_count_map(s: str):
    d_ = dict()
    for c in s:
        d_[c] = d_.setdefault(c, 0) + 1
    return d_


def generate_perms(
    char_count_map: dict, prefix: str, len_remaining: int, res: list
):
    if len_remaining == 0:
        res.append(prefix)
        return

    for char in char_count_map.keys():
        count = char_count_map[char]
        if count > 0:
            char_count_map[char] = count - 1
            generate_perms(
                char_count_map=char_count_map,
                prefix=f"{prefix}{char}",
                len_remaining=len_remaining - 1,
                res=res,
            )
            char_count_map[char] = count
