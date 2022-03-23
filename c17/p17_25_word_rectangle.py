from c17.word_set import word_set
from c17.default_trie import Trie
import typing as ty
from collections import defaultdict


class WordGroups:
    def __init__(self, word_list: ty.List[str]):
        self.size2words = defaultdict(list)
        self.word_set = set(word_list)
        self.max_word_len = len(max(word_list, key=len))
        for word in word_list:
            self.size2words[len(word)].append(word)


def main():
    word_group = WordGroups(list(word_set))
    trie_list = [None for _ in range(word_group.max_word_len)]
