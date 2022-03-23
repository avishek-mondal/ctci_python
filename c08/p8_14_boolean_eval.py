def main():
    s = "1^0|0|1"
    expected_res = False
    memo = dict()
    cases = [("1^0|0|1", False, 2), ("0&0&0&1^1|0", True, 10)]
    for s, res, expected in cases:
        assert expected == boolean_eval(s, res, memo=dict())

    # print(boolean_eval(s=s, res=expected_res, memo=memo))


def boolean_eval(s: str, res: bool, memo: dict) -> int:
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1 if string_to_bool(s) == res else 0

    if (res, s) in memo:
        return memo.get((res, s))

    ways = 0
    for i in range(1, len(s), 2):
        c = s[i]
        left = s[:i]
        right = s[i + 1 :]
        left_true = boolean_eval(left, True, memo)
        right_true = boolean_eval(right, True, memo)
        left_false = boolean_eval(left, False, memo)
        right_false = boolean_eval(right, False, memo)
        total = (left_true + left_false) * (right_true + right_false)

        total_true = 0

        if c == "^":
            total_true = left_true * right_false + left_false * right_true
        elif c == "&":
            total_true = left_true * right_true
        elif c == "|":
            total_true = (
                left_true * right_true
                + left_false * right_true
                + left_true * right_false
            )
        sub_ways = total_true if res else total - total_true
        ways += sub_ways

    memo[(res, s)] = ways
    return ways


def string_to_bool(s):
    return s == "1"
