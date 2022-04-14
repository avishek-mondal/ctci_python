import typing as ty
from collections import deque

from c04.node import Node


def get_list_depths_dfs(root: Node) -> ty.List:
    lists = []
    get_list_depths_dfs_helper(root=root, lists=lists, level=0)
    return lists


def get_list_depths_dfs_helper(
    root: Node, lists: ty.List[ty.List], level: int
):
    if root is None:
        return
    if len(lists) == level:
        arr = []
        lists.append(arr)
    else:
        arr = lists[level]
    arr.append(root)
    get_list_depths_dfs_helper(root.left, lists, level + 1)
    get_list_depths_dfs_helper(root.right, lists, level + 1)


def get_list_depths_bfs(root: Node) -> ty.List:
    if root is None:
        return []

    lvl = 0
    res = [[root]]

    while len(res[lvl]) > 0:
        res.append([])
        for node in res[lvl]:
            if node.left:
                res[lvl + 1].append(node.left)
            if node.right:
                res[lvl + 1].append(node.right)
        lvl += 1
    res.pop()
    return res


def construct_tree(nodes: ty.List[Node]) -> Node:
    num_nodes = len(nodes)
    q = deque()
    q.append(nodes[0])
    i = 0
    while i < num_nodes:
        cur = q.popleft()
        i += 1
        if i < num_nodes:
            left = nodes[i]
            cur.left = left
            q.append(left)
            i += 1
        if i < num_nodes:
            right = nodes[i]
            cur.right = right
            q.append(right)
    return nodes[0]


def main():
    num_nodes = 8
    nodes = [Node(i) for i in range(num_nodes)]
    root = construct_tree(nodes)
    testable_funcs = [get_list_depths_bfs, get_list_depths_dfs]
    for f in testable_funcs:
        lists = f(root)
        assert lists[0] == [nodes[0]]
        assert lists[1] == [nodes[1], nodes[2]]
        assert lists[2] == [nodes[3], nodes[4], nodes[5], nodes[6]]
        assert lists[3] == [nodes[7]]
