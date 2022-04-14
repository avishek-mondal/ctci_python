import typing as ty
from collections import deque
from copy import deepcopy

import tlog
from c04.construct_tree import construct_tree_with_parent, create_node_arr
from c04.node import Node


def main():
    node_arr = create_node_arr(
        [50, 20, 60, 10, 25, None, 70, 5, 15, None, None, None, None, 65, 80]
    )
    root = construct_tree_with_parent(node_arr)
    sequences = get_all_sequences(root)
    print(sequences)
    # test_weave()


def test_weave():
    first = deque([1, 2])
    second = deque([3, 4])
    # second = deque([])
    out = deque([])
    weave(first, second, prefix=deque([]), sequences=out)
    print(out)


def get_all_sequences(root: Node) -> ty.List:
    if not root:
        return []
    return list(get_all_sequences_helper(root))


def get_all_sequences_helper(root: Node) -> ty.Deque[ty.Deque]:
    if not root:
        return deque([deque([])])
    right_sequences = get_all_sequences_helper(root.right)
    left_sequences = get_all_sequences_helper(root.left)
    # tlog.info(f"root = {root}, right_sequences = {right_sequences}, left_sequences = {left_sequences}")
    sequences = deque([])
    for right_seq in right_sequences:
        for left_seq in left_sequences:
            weave(
                right_seq,
                left_seq,
                prefix=deque([root.key]),
                sequences=sequences,
            )
    return sequences


def weave(
    first: ty.Deque,
    second: ty.Deque,
    prefix: ty.Deque,
    sequences: ty.Deque[ty.Deque],
):
    # tlog.info(f"weaving first={first}, second={second}, prefix={prefix}, sequences = {sequences}")
    if len(first) == 0 or len(second) == 0:
        result: ty.Deque = deepcopy(prefix)
        result.extend(first)
        result.extend(second)
        sequences.append(result)
        return

    first_head = first.popleft()
    prefix.append(first_head)
    weave(first, second, prefix, sequences)
    first.appendleft(prefix.pop())

    second_head = second.popleft()
    prefix.append(second_head)
    weave(first, second, prefix, sequences)
    second.appendleft(prefix.pop())
