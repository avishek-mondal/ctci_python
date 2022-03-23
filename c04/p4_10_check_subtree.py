from c04.construct_tree import construct_tree_with_parent, create_node_arr
from c04.node import Node


def main():
    node_arr = create_node_arr([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    root = construct_tree_with_parent(node_arr)
    print(check_subtree(big_tree=root, small_tree=node_arr[3]))
    print(check_subtree(big_tree=root, small_tree=Node(2)))


def check_subtree(big_tree: Node, small_tree: Node) -> bool:
    if not big_tree:
        # big tree is empty, but small tree still not found
        return False
    elif big_tree.key == small_tree.key and matched_tree(big_tree, small_tree):
        return True

    return check_subtree(
        big_tree=big_tree.left, small_tree=small_tree
    ) or check_subtree(big_tree=big_tree.right, small_tree=small_tree)


def matched_tree(big_tree: Node, small_tree: Node) -> bool:
    if not big_tree and not small_tree:
        # have searched both until none -> small tree and big tree equivalent
        return True
    elif not big_tree or not small_tree:
        # have exhausted one but not hte other, not matched
        return False
    elif big_tree.key != small_tree.key:
        return False

    return matched_tree(
        big_tree=big_tree.right, small_tree=small_tree.right
    ) and matched_tree(big_tree=big_tree.left, small_tree=small_tree.left)
