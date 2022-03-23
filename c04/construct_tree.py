"""Test case

Tree 1:
          A
       /     \
      B       C
     / \     / \
    D   E   F   G
     \
      H

Tree 2:
          A
       /     \
      B       C
     / \       \
    D   E       G
     \         /
      H       F


"""

import typing as ty
from collections import deque

from c04.node import Node


def main():
    tree1 = ["A", "B", "C", "D", "E", "F", "G", None, "H"]
    tree2 = [
        "A",
        "B",
        "C",
        "D",
        "E",
        None,
        "G",
        None,
        "H",
        None,
        None,
        None,
        None,
        "F",
        None,
    ]
    root1 = construct_tree_with_no_parent(create_node_arr(tree1))
    print(root1.left.left)
    root2 = construct_tree_with_no_parent(create_node_arr(tree2))
    print(root2.right.right.left)

    root1 = construct_tree_with_parent(create_node_arr(tree1))
    print(root1.left.left.right)
    root2 = construct_tree_with_parent(create_node_arr(tree2))
    print(root2.right.right.left)


def construct_tree_with_parent(nodes: ty.List[Node]) -> Node:
    num_nodes = len(nodes)
    q = deque()
    q.append(nodes[0])
    i = 0
    while i < num_nodes:
        cur = q.popleft()
        i += 1
        if i < num_nodes:
            left = nodes[i]
            if cur:
                cur.left = left
                if left:
                    left.parent = cur
            q.append(left)
            i += 1
        if i < num_nodes:
            right = nodes[i]
            if cur:
                cur.right = right
                if right:
                    right.parent = cur
            q.append(right)
    return nodes[0]


def construct_tree_with_no_parent(nodes: ty.List[Node]) -> Node:
    num_nodes = len(nodes)
    q = deque()
    q.append(nodes[0])
    i = 0
    while i < num_nodes:
        cur = q.popleft()
        i += 1
        if i < num_nodes:
            left = nodes[i]
            if cur:
                cur.left = left
            q.append(left)
            i += 1
        if i < num_nodes:
            right = nodes[i]
            if cur:
                cur.right = right
            q.append(right)
    return nodes[0]


def create_node_arr(arr: ty.List[ty.Any]) -> ty.List[Node]:
    return [Node(k) if k is not None else None for k in arr]
