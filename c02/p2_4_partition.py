from c02.linked_list import LinkedList


def partition(ll: LinkedList, k: int):
    node, start, end = ll.head, ll.head, ll.head
    while node:
        next_node = node.next_node
        if node.value < k:
            # add to start
            node.next_node = start
            start = node
        else:
            end.next_node = node
            end = node
        node = next_node

    end.next_node = None
    ll.head = start
    ll.tail = end

def main():
    vals = [10, 10, 10, 10, 10, 0, 0, 0, 0, 0]
    ll = LinkedList(vals)
    partition(ll, 5)
    print(ll)