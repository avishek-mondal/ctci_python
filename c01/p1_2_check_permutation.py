import unittest


def main():
    print(check_permutation("dog", "god"))

def check_permutation(str1: str, str2: str) -> bool:
    str1_dict = get_str_dict(str1)
    str2_dict = get_str_dict(str2)
    for k, v in str1_dict.items():
        if k not in str2_dict:
            return False
        if str2_dict[k] != v:
            return False
    for k in str2_dict.keys():
        if k not in str1_dict:
            return False
    return True
    
def get_str_dict(str_: str) -> dict:
    str_dict = dict()
    for ch in str_:
        str_dict[ch] = str_dict.get(ch, 0) + 1
    return str_dict


class CheckPermutationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.test_cases = (
            ("dog", "god", True),
            ("abcd", "bacd", True),
            ("3563476", "7334566", True),
            ("wef34f", "wffe34", True),
            ("dogx", "godz", False),
            ("abcd", "d2cba", False),
            ("2354", "1234", False),
            ("dcw4f", "dcw5f", False),
            ("DOG", "dog", False),
            ("dog ", "dog", False),
            ("aaab", "bbba", False),
        )

    def test_check_permutation(self):
        for str1, str2, is_perm in self.test_cases:
            self.assertEqual(is_perm, check_permutation(str1, str2))


if __name__ == '__main__':
    unittest.main()