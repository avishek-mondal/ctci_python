import typing as ty


class TrieNode:
    def __init__(self, char_=""):
        self.children: ty.Dict[str, TrieNode] = dict(TrieNode)
        self.char_ = char_
        self.terminates = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert_word(self, word):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode(char_=c)
            node = node.children[c]

        node.terminates = True

    def contains_word(self, word: str, need_exact: bool = False) -> bool:
        node = self.root
        for c in word:
            node = node.children.get(c)
            if not node:
                return False

        if need_exact:
            return node.terminates
        return True
