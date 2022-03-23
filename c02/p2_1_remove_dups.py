from c02.linked_list import LinkedList, LinkedListNode


def main():
    values = [1, 1, 1, 1, 1, 1, 1]
    ll = LinkedList(values)
    print(ll)
    # new_ll = remove_dupes(ll)
    new_ll = remove_dupes_no_small_mem(ll)
    print(new_ll)

def remove_dupes_no_small_mem(ll: LinkedList):
    current = ll.head
    while current:
        runner = current
        while runner.next_node:
            if runner.next_node.value == current.value:
                runner.next_node = runner.next_node.next_node
            else:
                runner = runner.next_node
        current = current.next_node
    return ll
    

def remove_dupes(ll: LinkedList):
    previous = LinkedListNode(0, next_node=ll.head)
    head = ll.head
    seen = set()
    while head:
        if head.value in seen:
            previous.next_node = head.next_node
        else:
            seen.add(head.value)
            previous = head
        head = head.next_node
    return ll
