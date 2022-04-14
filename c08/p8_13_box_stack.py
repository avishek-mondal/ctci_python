import typing as ty
import unittest


def main():
    print(create_stack([Box(3, 2, 1), Box(6, 5, 4)]))


def create_stack(boxes: ty.List["Box"]):
    boxes.sort(reverse=True)
    hash_map = [0 for _ in range(len(boxes))]
    return create_stack_helper(
        boxes=boxes, bottom_box=None, idx=0, hash_map=hash_map
    )


def create_stack_helper(
    boxes: ty.List["Box"], bottom_box: "Box", idx: int, hash_map: ty.List
):
    """Think about recursion as a choice - at each step, decide whether
    to put bottom_box in the stack.

    Take 1 recursive path with bottom_box at the bottom
    Take another recursive path without bottom_box at the bottom

    Return better of the two options

    Args:
        boxes (ty.List[&quot;Box&quot;]): _description_
        bottom_box (Box): _description_
        idx (int): _description_
        hash_map: ith idx is the height if box_i is at the bottom

    Returns:
        the best height at ith idx
    """
    if idx >= len(boxes):
        return 0

    new_bottom = boxes[idx]

    # put bottom in the stack
    height_with_bottom = 0
    if (
        bottom_box is None  # <- if it is the first step
        or new_bottom < bottom_box
    ):
        if hash_map[idx] == 0:
            recurse = create_stack_helper(
                boxes=boxes,
                bottom_box=new_bottom,
                idx=idx + 1,
                hash_map=hash_map,
            )
            hash_map[idx] = recurse + new_bottom.h
        height_with_bottom = hash_map[idx]

    height_without_bottom = create_stack_helper(
        boxes=boxes,
        bottom_box=bottom_box,
        idx=idx + 1,
        hash_map=hash_map,
    )

    # print(f"bottom_box={bottom_box}, idx={idx}, height_with_bottom = {height_with_bottom}, height_without_bottom = {height_without_bottom}")
    return max(height_with_bottom, height_without_bottom)


class Box:
    def __init__(self, h, w, l):
        self.h = h
        self.w = w
        self.l = l

    def __lt__(self, other):
        return self.h < other.h and self.l < other.l and self.w < other.w

    def __eq__(self, other):
        return self.h == other.h and self.l == other.l and self.w == other.w

    def __str__(self):
        return f"Box(h={self.h}, w={self.w}, d={self.l})"


def test_null():
    assert create_stack([]) == 0


def test_single_box():
    assert create_stack([Box(3, 2, 1)]) == 3


def test_two_conflicting_boxes():
    assert create_stack([Box(3, 2, 1), Box(5, 4, 1)]) == 5


def test_two_stackable_boxes():
    assert create_stack([Box(3, 2, 1), Box(6, 5, 4)]) == 9


class BoxesTest(unittest.TestCase):
    def test_boxes(self):
        test_cases = [
            ([Box(3, 2, 1), Box(6, 5, 4)], 9),
            ([Box(3, 2, 1), Box(5, 4, 1)], 5),
            ([Box(3, 2, 1)], 3),
            ([], 0),
        ]
        for boxes, expected in test_cases:
            self.assertEqual(create_stack(boxes), expected)


if __name__ == "__main__":
    unittest.main()
