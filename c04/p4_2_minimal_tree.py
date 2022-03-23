from c04.node import Node


def main():
    a = [4, 2, 5, 1, 3, 4]
    a.sort()
    print(create_minimal_bst(a, 0, len(a) - 1))


def create_minimal_bst(arr: list, start: int, end: int) -> Node:
    if end < start:
        return None
    mid = start + (end - start) // 2
    node = Node(arr[mid])
    node.left = create_minimal_bst(arr, start, mid - 1)
    node.right = create_minimal_bst(arr, mid + 1, end)
    return node
