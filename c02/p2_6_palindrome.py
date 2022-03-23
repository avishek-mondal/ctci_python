import unittest

from c02.linked_list import LinkedList, LinkedListNode


def main():
    ll = LinkedList([1, 1, 1, 1])
    print(is_palindrome(ll))


def is_palindrome(ll: LinkedList) -> bool:
    fast, slow = ll.head, ll.head
    stack = []

    while fast and fast.next_node:
        stack.append(slow.value)
        slow = slow.next_node
        fast = fast.next_node.next_node

    # for odd list lens, skip the middle node
    if fast:
        slow = slow.next_node

    while slow:
        top = stack.pop()
        if top != slow.value:
            return False
        slow = slow.next_node

    return True


class IsPalindromeTest(unittest.TestCase):

    test_cases = [
        ([1, 2, 3, 4, 3, 2, 1], True),
        ([1], True),
        (["a", "a"], True),
        ("aba", True),
        ([], True),
        ([1, 2, 3, 4, 5], False),
        ([1, 2], False),
    ]

    def test_is_palindrome(self):
        for arr, expected in self.test_cases:
            ll = LinkedList(arr)
            self.assertEqual(is_palindrome(ll), expected)


if __name__ == '__main__':
    unittest.main()
