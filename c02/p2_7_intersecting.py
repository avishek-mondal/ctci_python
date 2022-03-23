from torch import short

from c02.linked_list import LinkedList, LinkedListNode


def get_intersection(l1: LinkedList, l2: LinkedList) -> LinkedListNode:
    if l1.tail is not l2.tail:
        return None

    shorter_list = l1 if len(l1) < len(l2) else l2
    longer_list = l1 if len(l1) > len(l2) else l2

    diff = len(longer_list) - len(shorter_list)

    short_node, long_node = shorter_list.head, longer_list.head

    for _ in range(diff):
        long_node = long_node.next_node

    while short_node is not long_node:
        short_node = short_node.next_node
        long_node = long_node.next_node

    return long_node


def main():
    shared = LinkedList([7, 2, 1])
    l1 = LinkedList([3, 1, 5, 9])
    l2 = LinkedList([4, 6])

    l1.tail.next_node = shared.head
    l1.tail = shared.tail
    l2.tail.next_node = shared.head
    l2.tail = shared.tail

    print(get_intersection(l1, l2).value)
