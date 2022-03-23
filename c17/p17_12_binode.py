import tlog


class BiNode:
    def __init__(self, d):
        self.node1 = None
        self.node2 = None
        self.data = d

    def __str__(self):
        print_left = self.node1.data if self.node1 else "None"
        print_right = self.node2.data if self.node2 else "None"
        return f"BiNode(d={self.data}, left={print_left}, right={print_right})"


class NodePair:
    def __init__(self, head: BiNode, tail: BiNode):
        self.head = head
        self.tail = tail

    def __str__(self):
        return f"NodePair(head={self.head}, tail={self.tail})"


def convert_using_circular(root: BiNode):
    head = convert_using_circular_helper(root)
    head.node1.node2 = None
    head.node1 = None
    return head


def convert_using_circular_helper(root: BiNode) -> BiNode:
    """Return circular linked list

    Args:
        root: the root

    Returns:
        head of a circular linked list, whose tail is node.node1
    """
    if root is None:
        return None

    left_circular = convert_using_circular_helper(root.node1)
    right_circular = convert_using_circular_helper(root.node2)

    if left_circular is None and right_circular is None:
        root.node1 = root
        root.node2 = root
        return root

    right_tail = right_circular.node1 if right_circular else None

    # join left to root
    if left_circular:
        # connect tail to root
        concat(left_circular.node1, root)
    else:
        # connect the other tail to the root
        concat(right_circular.node1, root)

    # join right to root
    if right_circular:
        concat(root, right_circular)
    else:
        concat(root, left_circular)

    # now connect left and right
    if left_circular and right_circular:
        concat(right_tail, left_circular)

    return left_circular if left_circular else root


def concat(x: BiNode, y: BiNode):
    x.node2 = y
    y.node1 = x


def convert_using_node_pairs(root: BiNode) -> NodePair:
    if not root:
        return None

    part1 = convert_using_node_pairs(root.node1)
    part2 = convert_using_node_pairs(root.node2)

    if part1:
        concat(part1.tail, root)
    if part2:
        concat(root, part2.head)

    head = part1.head if part1 else root
    tail = part2.tail if part2 else root
    tlog.info(f"returning head={head}, tail={tail}")
    return NodePair(head, tail)


def convert_by_retrieving_tail(root: BiNode) -> BiNode:
    """Don't need both head and tail, can just get tail

    O(N^2), because a leaf node at depth d will be touched by get_tail method
    d times (one for every node above it)

    Args:
        root: the binode

    Returns:
        a binode
    """
    if not root:
        return None

    part1 = convert_by_retrieving_tail(root.node1)
    part2 = convert_by_retrieving_tail(root.node2)

    if part1:
        concat(get_tail(part1), root)
    if part2:
        concat(root, part2)

    return part1 if part1 is not None else root


def get_tail(root: BiNode):
    if not root:
        return None
    while root.node2:
        root = root.node2
    return root


def create_example_tree():
    nodes = [BiNode(i) for i in range(7)]
    nodes[4].node1 = nodes[2]
    nodes[4].node2 = nodes[5]
    nodes[2].node1 = nodes[1]
    nodes[2].node2 = nodes[3]
    nodes[5].node2 = nodes[6]
    nodes[1].node1 = nodes[0]

    return nodes[4]


def print_as_tree(root: BiNode, spaces: str):
    if not root:
        print(f"{spaces}-None")
        return
    print(f"{spaces}- {root.data}")
    print_as_tree(root.node1, spaces=f"{spaces}   ")
    print_as_tree(root.node2, spaces=f"{spaces}   ")


def print_ll(root: BiNode):
    node = root
    to_print = ""
    while node:
        if node.node2 and node.node2.node1 != node:
            to_print = f"Found inconsistent node = ({node.data}). "
        to_print += f"{node.data} -> "
        node = node.node2
    print(to_print[:-3])


def main():
    root = create_example_tree()
    print_as_tree(root=root, spaces="")
    # node_pair = convert_using_node_pairs(root)
    # print_ll(node_pair.head)
    # node = convert_by_retrieving_tail(root)
    # print_ll(node)
    node = convert_using_circular(root)
    print_ll(node)
