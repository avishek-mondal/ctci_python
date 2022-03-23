from c04.node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new = Node(key=key)
        if self.root is None:
            self.root = new
            return None

        current = self.root
        while current is not None:
            if current.key > key:
                if current.left is None:
                    current.left = new
                    new.parent = current
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new
                    new.parent = current
                    return
                current = current.right

    def get_node(self, key) -> Node:
        current = self.root
        while current is not None:
            if current.key == key:
                return current
            elif current.key > key:
                current = current.left
            elif current.key < key:
                current = current.right
        raise Exception("No such node found")


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    node = bst.get_node(9)
    print(node)
