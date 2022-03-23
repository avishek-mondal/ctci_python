from c02.linked_list import LinkedList, LinkedListNode


def main():
    prefix = LinkedList([1, 2, 3, 4])
    loop_start = LinkedListNode(5)
    loop = LinkedList([6, 7, 8, 9, 10])

    prefix.tail.next_node = loop_start
    loop_start.next_node = loop.head
    loop.tail.next_node = loop_start

    intersection = get_intersection(prefix)
    print(intersection.value)


def get_intersection(ll: LinkedList) -> LinkedListNode:
    """Basic algo:

    1. Create 2 pointers - fast and slow

    2. move fast 2 steps, and slow 1 step

    3. when they collide, move slow back to the head, and keep fast where it is

    4. move slow and fast both at 1 step each

    5. Where they collide is the start of the loop

    Args:
        ll: the linked list

    Returns:
        node where they intersect
    """
    fast, slow = ll.head, ll.head

    while fast and fast.next_node:
        slow = slow.next_node
        fast = fast.next_node.next_node
        if slow is fast:
            break

    if fast is None or fast.next_node is None:
        return None

    # move slow back to head and increment 1 step each
    slow = ll.head
    while slow is not fast:
        slow = slow.next_node
        fast = fast.next_node

    return fast
