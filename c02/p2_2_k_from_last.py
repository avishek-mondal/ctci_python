from c02.linked_list import LinkedList, LinkedListNode


def main():
    vals = [1, 2, 3, 4, 5, 6, 7]
    ll = LinkedList(vals)
    k_node = return_k_from_last(ll=ll, k=3)
    print(k_node)


def return_k_from_last(ll: LinkedList, k: int) -> LinkedListNode:
    p1, p2 = ll.head, ll.head
    for _ in range(k):
        p2 = p2.next_node
        if p2 is None:
            return p1
    while p2:
        p2 = p2.next_node
        p1 = p1.next_node
    return p1
