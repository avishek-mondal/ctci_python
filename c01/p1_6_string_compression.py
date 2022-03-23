import unittest


def main():
    s = "aabcccccaaa"
    print(string_compression(s))


def string_compression(s: str) -> str:
    if not s:
        return ''

    n = len(s)
    compressed = []
    cnt = 0
    ch = s[0]
    for i in range(n):
        if s[i] != ch:
            compressed.append((ch, cnt))
            ch = s[i]
            cnt = 1
        else:
            cnt += 1
    compressed.append((ch, cnt))
    out = ''.join([f"{char_}{cnt_}" for char_, cnt_ in compressed])
    if len(out) >= n:
        return s
    return out


class Test(unittest.TestCase):
    test_cases = [
        ("aabcccccaaa", "a2b1c5a3"),
        ("abcdef", "abcdef"),
        ("aabb", "aabb"),
        ("aaa", "a3"),
        ("a", "a"),
        ("", ""),
    ]

    def test_string_compression(self):
        for s, expected in self.test_cases:
            self.assertEqual(expected, string_compression(s))


if __name__ == '__main__':
    unittest.main()
