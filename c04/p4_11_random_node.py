class ExtendedNode:
    def __init__(self, data):
        self.data = data
        self.size = 1
        self.left: ExtendedNode = None
        self.right: ExtendedNode = None

    def insert_in_order(self, data):
        if (data <= self.data):
            if not self.left:
                self.left = ExtendedNode(data)
            else:
                self.left.insert_in_order(data)
        else:
            if not self.right:
                self.right = ExtendedNode(data)
            else:
                self.right.insert_in_order(data)

        self.size += 1

    def find(self, data) -> 'ExtendedNode':
        if data == self.data:
            return self
        elif data < self.data:
            return self.left.find(data) if self.left is not None else None
        elif data > self.data:
            return self.right.find(data) if self.right is not None else None

    def get_ith_node(self, i):
        if i > self.size:
            raise ValueError
        left_size = self.left.size if self.left else 0
        if i < left_size:
            return self.left.get_ith_node(i)
        elif i == left_size:
            return self
        else:
            self.right.get_ith_node(i - (left_size + 1))