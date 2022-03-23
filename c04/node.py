class Node:
    def __init__(self, key):
        self.key = key
        self.parent: Node = None
        self.left: Node = None
        self.right: Node = None

    def __str__(self):
        parent_str = self.parent.key if self.parent else "None"
        right_str = self.right.key if self.right else "None"
        left_str = self.left.key if self.left else "None"
        return (
            f"Node(key={self.key}, parent={parent_str}, "
            f"left_str={left_str}, right_str={right_str})"
        )
