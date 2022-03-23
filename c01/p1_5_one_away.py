def main():
    tests = [('pale', 'ple'), ('pales', 'pale'), ('pale', 'bale'),
             ('pale', 'bake'), ('relly long', 'short boi')]
    for str1, str2 in tests:
        print(one_away(str1, str2))


def one_away(str1: str, str2: str) -> bool:
    if len(str1) == len(str2):
        return check_replace(str1, str2)
    if len(str1) + 1 == len(str2):
        return check_insert(short_str=str1, long_str=str2)
    if len(str2) + 1 == len(str1):
        return check_insert(short_str=str2, long_str=str1)
    return False


def check_replace(str1: str, str2: str) -> bool:
    found_diff = False
    n = len(str1)
    for i in range(n):
        if str1[i] != str2[i]:
            if found_diff:
                return False
            found_diff = True
    return True


def check_insert(short_str: str, long_str: str) -> bool:
    long_str_idx = 0
    short_str_len = len(short_str)
    for short_str_idx in range(short_str_len):
        if short_str[short_str_idx] != long_str[long_str_idx]:
            if short_str_idx != long_str_idx:
                return False
            long_str_idx += 1
        long_str_idx += 1
    return True
