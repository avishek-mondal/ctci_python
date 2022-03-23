import typing as ty


class LinkedListNode:
    def __init__(self,
                 value: int,
                 next_node: 'LinkedListNode' = None,
                 prev_node: 'LinkedListNode' = None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self, values: list = None):
        self.head: LinkedListNode = None
        self.tail: LinkedListNode = None
        if values:
            self.add_values(values)

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next_node

    def __len__(self):
        len_ = 0
        current = self.head
        while current:
            len_ += 1
            current = current.next_node
        return len_

    def __str__(self):
        return " -> ".join([str(v) for v in self.values()])

    def values(self):
        return [node.value for node in self]

    def add(self, value: int) -> LinkedListNode:
        if not self.head:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.tail.next_node = LinkedListNode(value)
            self.tail = self.tail.next_node
        return self.tail

    def add_values(self, values: ty.List[int]):
        for v in values:
            self.add(v)

    def add_to_front(self, value) -> LinkedListNode:
        if self.head is None:
            self.head = self.tail = LinkedListNode(value)
        else:
            self.head = LinkedListNode(value, next_node=self.head)
        return self.head
