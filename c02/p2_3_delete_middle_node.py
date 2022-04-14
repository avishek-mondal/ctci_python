from c02.linked_list import LinkedList, LinkedListNode


def del_middle(node: LinkedListNode):
    node.value = node.next_node.value
    node.next_node = node.next_node.next_node


def main():
    vals = [1, 2, 3, 4, 5, 6, 7]
    ll = LinkedList(vals)
    middle_node = ll.add(LinkedListNode(9))
    ll.add_values([8, 9, 10, 11])
    del_middle(middle_node)
    print(ll)
