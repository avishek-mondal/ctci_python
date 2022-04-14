from collections import defaultdict

TERMINATING_CHAR = "\0"


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.indexes = []

    def __str__(self):
        return (
            f"TriNode(indexes={self.indexes}, children={self.children.keys()})"
        )

    def insert_string(self, s: str, idx: int):
        self.indexes.append(idx)
        if len(s) > 0:
            val = s[0]
            child = self.children[val]
            return child.insert_string(s=s[1:], idx=idx + 1)
        else:
            self.children[TERMINATING_CHAR] = True

    def search(self, s: str):
        if not s or len(s) == 0:

            return self.indexes

        first_char = s[0]
        if first_char in self.children:
            child = self.children[first_char]
            return child.search(s=s[1:])

    def terminates(self):
        return TERMINATING_CHAR in self.children


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_string(self, s):
        return self.root.insert_string(s)

    def search(self, s: str):
        return self.root.search(s)


def main():
    b = "mississippi"
    small_words = ["i", "is", "pp", "ms", "issi"]

    print(search_all(big_word=b, small_words=small_words))


def search_all(big_word: str, small_words: list):
    res = defaultdict(list)
    root = create_trie_from_small_words(small_words)
    for i in range(len(big_word)):
        strings_at_loc = find_strings_at_loc(
            node=root, big_word=big_word, start=i
        )
        for s in strings_at_loc:
            res[s].append(i)

    return dict(res)


def create_trie_from_small_words(small_words: list):
    root = TrieNode()
    for s in small_words:
        root.insert_string(s, 0)
    return root


def find_strings_at_loc(node: TrieNode, big_word: str, start: int):
    root = node
    idx = start
    strings = []
    while idx < len(big_word):
        char_ = big_word[idx]

        if char_ in root.children:
            root = root.children[char_]
            if root.terminates():

                strings.append(big_word[start : idx + 1])
        else:
            break
        idx += 1
    return strings
