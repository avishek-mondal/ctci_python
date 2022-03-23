import typing as ty

from c02.linked_list import LinkedList, LinkedListNode


def main():
    ll1 = LinkedList([6, 1, 7])
    ll2 = LinkedList([2, 9, 5])

    ll3 = sum_lists(ll1, ll2)
    print(ll3)

    print(sum_lists(LinkedList([9, 9, 9, 9]), LinkedList([1])))


def sum_lists(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    if len(ll1) > len(ll2):
        shorter_list = ll2
        longer_list = ll1
    else:
        shorter_list = ll1
        longer_list = ll2

    pad_zeros(shorter_list, len(longer_list) - len(shorter_list))

    start, carry = sum_list_helper(shorter_list.head, longer_list.head)

    if carry != 0:
        start = LinkedListNode(1, next_node=start)

    res = LinkedList([])
    res.head = start
    return res


def sum_list_helper(node1: LinkedListNode,
                    node2: LinkedListNode) -> ty.Tuple[LinkedListNode, int]:
    if node1 is None and node2 is None:
        return None, 0

    if node1 is None or node2 is None:
        raise ValueError("Make sure lists are same length")
    
    res = LinkedListNode(0)
    
    next_node, carry = sum_list_helper(node1.next_node, node2.next_node)

    value = carry + node1.value + node2.value
    carry = value // 10
    rem = value % 10

    res.value = rem
    res.next_node = next_node

    return res, carry


def pad_zeros(l: LinkedList, pad_len: int):
    for _ in range(pad_len):
        l.head = LinkedListNode(0, l.head)
