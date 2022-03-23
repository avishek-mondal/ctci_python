import typing as ty
import unittest


class Node:
    def __init__(self, value):
        self.value = value
        self.above = None
        self.below = None

class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.top : Node = None
        self.bottom : Node = None

    def is_full(self) -> bool:
        return self.capacity == self.size

    def push(self, value):
        if self.size >= self.capacity:
            return
        self.size += 1
        node = Node(value=value)
        if self.size == 1:
            self.bottom = node
        self.join(node, self.top)
        self.top = node

    def pop(self):
        t = self.top
        if t is None:
            return None
        self.top = self.top.below
        self.size -= 1
        return t.value

    def is_empty(self):
        return self.size == 0

    def remove_bottom(self):
        b = self.bottom
        if not b:
            return None
        self.bottom = self.bottom.above
        if self.bottom:
            self.bottom.below = None
        self.size -= 1
        return b.value

    def join(self, above: Node, below: Node):
        if below:
            below.above = above
        if above:
            above.below = below


class StackSet:
    def __init__(self, stack_capacity):
        self.stack_capacity = stack_capacity
        self.stacks : ty.List[Stack] = []

    def get_last_stack(self) -> Stack:
        if not self.stacks:
            return None
        return self.stacks[-1]

    def is_empty(self):
        last = self.get_last_stack()
        return last is None or last.is_empty()

    def push(self, value):
        last = self.get_last_stack()
        if last is not None and not last.is_full():
            last.push(value)
        else:
            s = Stack(self.stack_capacity)
            s.push(value)
            self.stacks.append(s)

    def pop(self):
        last = self.get_last_stack()
        if last is None:
            return None
        v = last.pop()
        if last.size == 0:
            del self.stacks[-1]
        return v

    def pop_at(self, idx):
        return self.left_shift(idx=idx, remove_top=True)

    def left_shift(self, idx: int, remove_top: bool):
        st = self.stacks[idx]
        removed_item = st.pop() if remove_top else st.remove_bottom()
        if st.is_empty():
            del self.stacks[idx]
        elif len(self.stacks) > idx + 1:
            v = self.left_shift(idx=idx + 1, remove_top=False)
            st.push(v)
        return removed_item



class Tests(unittest.TestCase):
    def test_stacks(self):
        stacks = StackSet(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(35):
            lst.append(stacks.pop())
        assert lst == list(reversed(range(35)))

    def test_pop_at(self):
        stacks = StackSet(5)
        for i in range(35):
            stacks.push(i)
        lst = []
        for _ in range(31):
            lst.append(stacks.pop_at(0))
        assert lst == list(range(4, 35))


if __name__ == "__main__":
    unittest.main()