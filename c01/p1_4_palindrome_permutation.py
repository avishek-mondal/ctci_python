import unittest
from curses.ascii import isalpha


def main():
    inp_ = 'Tact Coa'
    # inp_ = 'So patient a nurse to nurse a patient so'
    # inp_ = 'aabb!'
    print(pal_perm(inp_))


def pal_perm(s: str):
    char_count_dict, allowed_chars = get_char_count(s)
    allowed_non_even = 0 if allowed_chars % 2 == 0 else 1
    # breakpoint()
    for _, v in char_count_dict.items():
        if v%2 != 0:
            if allowed_non_even == 0:
                return False
            allowed_non_even -= 1
    return True


def get_char_count(s: str):
    char_count_dict = dict()
    char_count = 0
    n = len(s)
    for i in range(n):
        if s[i].isalpha():
            ch = s[i].lower()
            char_count += 1
            char_count_dict[ch] = char_count_dict.get(ch, 0) + 1
    return char_count_dict, char_count


class Test(unittest.TestCase):
    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
        ("bab!!!", True)
    ]

    def test_pal_perm(self):
        for s, expected in self.test_cases:
            self.assertEqual(expected, pal_perm(s), msg=f"failed at {s}")



if __name__ == '__main__':
    unittest.main()
