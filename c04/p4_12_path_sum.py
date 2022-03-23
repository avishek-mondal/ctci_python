from c04.construct_tree import construct_tree_with_parent, create_node_arr
from c04.node import Node
import tlog


def main():
    node_arr = create_node_arr([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
    root = construct_tree_with_parent(node_arr)
    target = 8
    # print(count_sum_paths_bf(root, target))
    print(count_sum_paths(root, target))


def count_sum_paths(root: Node, target: int) -> int:
    if not root:
        return 0
    return _count_sum_paths(root, target, running_total=0, table=dict())


def _count_sum_paths(root: Node, target: int, running_total: int, table: dict):
    if not root:
        return 0
    running_total += root.key
    old_path_sum = running_total - target
    total = table.get(old_path_sum, 0)

    increment_table(table, running_total, 1)

    left_total = _count_sum_paths(
        root.left, target, running_total=running_total, table=table
    )
    right_total = _count_sum_paths(
        root.right, target, running_total=running_total, table=table
    )

    increment_table(table, running_total, -1)

    if running_total == target:
        tlog.info(f"node = {root}, table = {table}, left_total={left_total}, right_total={right_total}")
        total += 1

    total += left_total + right_total
    if total != 0:
        tlog.info(f"node = {root}, table = {table}, total = {total}, left_total={left_total}, right_total={right_total}, running_total = {running_total}")
    return total

def increment_table(table: dict, key, delta):
    # tlog.info(f"table before = {table}, key = {key}, delta = {delta}")
    new_count = table.get(key, 0) + delta
    if new_count == 0:
        table.pop(key, None)
        # tlog.info(f"table POPPING = {table}, key = {key}")
    else:
        table[key] = new_count
    # tlog.info(f"table after = {table}, key = {key}")

def count_sum_paths_bf(root, target):
    if root is None:
        return 0
    paths_from_root = count_paths_from_root(root, target, 0)

    right_path = count_sum_paths_bf(root.right, target)
    left_path = count_sum_paths_bf(root.left, target)

    return paths_from_root + right_path + left_path

def count_paths_from_root(root, target, cur_sum):
    if not root:
        return 0

    cur_sum += root.key

    total_paths = 0
    if cur_sum == target:
        total_paths += 1

    total_paths += count_paths_from_root(root.right, target, cur_sum)
    total_paths += count_paths_from_root(root.left, target, cur_sum)
    return total_paths
