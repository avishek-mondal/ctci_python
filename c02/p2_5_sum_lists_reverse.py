from c02.linked_list import LinkedList, LinkedListNode


def main():
    ll1 = LinkedList([7, 1, 6])
    ll2 = LinkedList([5, 9, 2])

    ll3 = sum_lists(ll1, ll2)
    print(ll3)

    print(sum_lists(LinkedList([9, 9, 9, 9]), LinkedList([1])))


def sum_lists(ll1: LinkedList, ll2: LinkedList) -> LinkedList:
    carry = 0
    sum_list = LinkedList([])
    head = sum_list_helper(ll1.head, ll2.head, carry)
    sum_list.head = head
    return sum_list


def sum_list_helper(ln1: LinkedListNode, ln2: LinkedListNode,
                    carry: int) -> LinkedListNode:
    if ln1 is None and ln2 is None and carry == 0:
        return None
    value = carry
    if ln1:
        value += ln1.value
    if ln2:
        value += ln2.value

    carry = value // 10
    rem = value % 10
    result = LinkedListNode(value=rem)

    next_ln1 = ln1.next_node if ln1 else None
    next_ln2 = ln2.next_node if ln2 else None

    result.next_node = sum_list_helper(next_ln1, next_ln2, carry)
    return result
