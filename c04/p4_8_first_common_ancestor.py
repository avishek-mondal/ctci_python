"""Test case

Tree 1:
          A
       /     \
      B       C
     / \     / \
    D   E   F   G
   /
  H

Tree 2:
          A
       /     \
      B       C
     / \     / \
    D   E   F   G
   /
  H


"""
from functools import partial

import tlog
from c04.construct_tree import construct_tree_with_parent, create_node_arr
from c04.node import Node


def main():
    node_arr = create_node_arr(["A", "B", "C", "D", "E", "F", "G", "H"])
    construct_tree_with_parent(node_arr)

    # test_func = partial(common_ancestor_brute_force, node_arr[0])
    test_func = partial(common_ancestor_no_parents, node_arr[0])
    fca: Node = test_func(node_arr[-2], node_arr[-1])
    assert fca.key == "A"
    fca = test_func(node_arr[-4], node_arr[-3])
    assert fca.key == "A"
    fca = test_func(node_arr[-4], node_arr[-1])
    assert fca.key == "B"
    print(fca)


def fca_w_parents(p: Node, q: Node) -> Node:
    tlog.info(f"fca with parents. p = {p}, q = {q}")
    p_depth = get_depth(p)
    q_depth = get_depth(q)

    shallow = p if p_depth < q_depth else q
    deeper = p if p_depth >= q_depth else q

    deeper = go_up_by(deeper, abs(q_depth - p_depth))

    while shallow != deeper and shallow and deeper:
        tlog.info(f"shallow = {shallow}, deeper = {deeper}")
        shallow = shallow.parent
        deeper = deeper.parent

    tlog.info(f"Done. shallow = {shallow}, deeper = {deeper}")
    ret_none = shallow is None or deeper is None
    if ret_none:
        return None
    return shallow


def get_depth(node: Node):
    cnt = 0
    while node.parent:
        cnt += 1
        node = node.parent

    return cnt


def go_up_by(node: Node, delta: int):
    tlog.info(f"node = {node}, delta = {delta}")
    while delta > 0:
        node = node.parent
        delta -= 1
    tlog.info(f"after moving up, node = {node}")
    return node


def fca_w_parents_check_subtree(p: Node, q: Node) -> Node:
    tlog.info(f"starting. p = {p}, q = {q}")
    if covers(p, q):
        return p
    elif covers(q, p):
        return q

    sibling = get_sibling(p)
    parent = p.parent
    while not covers(sibling, q):
        tlog.info(f"parent = {parent}, sibling = {sibling}")
        sibling = get_sibling(parent)
        parent = parent.parent
    return parent


def covers(root: Node, q: Node):
    if root is None:
        return False
    elif root == q:
        return True
    return covers(root.right, q) or covers(root.left, q)


def get_sibling(p: Node):
    if not p or not p.parent:
        return None
    parent = p.parent

    to_ret = parent.left if parent.right == p else parent.right
    return to_ret


class Result:
    """Need to be able to differentiate between the followign 2 cases:

    Case 1: q is a child of p, or p is a child of q. In this case need to
    correctly return p/q, whichever is the ancestor

    Case 2: p is in the tree, but q is not in the tree. In this cae need to
    return None
    """

    def __init__(self, node: Node, is_ancestor: bool):
        self.node = node
        self.is_ancestor = is_ancestor


def common_ancestor_no_parents_w_res(root: Node, p: Node, q: Node) -> Node:
    res: Result = _common_ancestor_no_parents_w_res(root, p, q)
    if res.is_ancestor:
        return res.node
    return None


def _common_ancestor_no_parents_w_res(root: Node, p: Node, q: Node) -> Node:
    if not root:
        return Result(node=None, is_ancestor=False)

    if root == p and root == q:
        return Result(node=root, is_ancestor=True)

    res_right: Result = _common_ancestor_no_parents_w_res(root.right, p, q)
    if res_right.is_ancestor:
        return res_right

    res_left: Result = _common_ancestor_no_parents_w_res(root.left, p, q)
    if res_left.is_ancestor:
        return res_left

    if res_right.node and res_left.node:
        return Result(node=root, is_ancestor=True)
    elif root == p or root == q:
        """If we're currently at p or q, and we also found one of those nodes
        in a subtree, then this is truly an ancestor and the flag should be
        true"""
        is_ancestor = res_right.node is not None or res_left.node is not None
        return Result(node=root, is_ancestor=is_ancestor)
    else:
        ret_node = res_right.node if res_right.node else res_left.node
        return Result(node=ret_node, is_ancestor=False)


def common_ancestor_no_parents(root: Node, p: Node, q: Node):
    if not node_exists(root, p) or not node_exists(root, q):
        return None
    args= locals()
    tlog.info("args", args_passed={k: str(v) for k, v in args.items()})
    tlog.info("Starting helper")
    return _common_ancestor_no_parents(root, p, q)


def _common_ancestor_no_parents(root: Node, p: Node, q: Node):
    tlog.info(f"root = {root}, p = {p}, q = {q}")
    if root is None:
        return None
    if root == p and root == q:
        return root

    res_right = _common_ancestor_no_parents(root.right, p, q)
    if res_right and res_right != p and res_right != q:
        return res_right
    res_left = _common_ancestor_no_parents(root.left, p, q)
    if res_left and res_left != p and res_left != q:
        return res_left

    if res_right and res_left:
        return root
    elif root == p or root == q:
        return root
    else:
        return res_right if res_right else res_left


def node_exists(root: Node, p: Node):

    if not root:
        return False
    if root == p:
        return True
    return node_exists(root.right, p) or node_exists(root.left, p)


def common_ancestor_brute_force(root: Node, p: Node, q: Node):
    if not covers(root, p) or not covers(root, q):
        return None
    return _common_ancestor_brute_force(root, p, q)


def _common_ancestor_brute_force(root: Node, p: Node, q: Node):
    if not root or root == p or root == q:
        return root

    p_is_on_left = covers(root.left, p)
    q_is_on_left = covers(root.left, q)
    if q_is_on_left != p_is_on_left:
        return root

    child = root.left if p_is_on_left else root.right
    return _common_ancestor_brute_force(child, p, q)
