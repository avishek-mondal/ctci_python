class MinStack:
    def __init__(self):
        self.arr = []
        self.min_arr = []

    def push(self, val):
        min_val = val if len(self.min_arr) == 0 else min(val, self.arr[-1])
        self.arr.append(val)
        self.min_arr.append(min_val)

    def pop(self):
        self.min_arr.pop()
        return self.arr.pop()

    def get_min(self):
        return self.min_arr[-1]


def main():
    min_stack = MinStack()
    min_stack.push(5)
    assert min_stack.get_min() == 5
    min_stack.push(6)
    assert min_stack.get_min() == 5
    min_stack.push(3)
    assert min_stack.get_min() == 3
    min_stack.push(7)
    assert min_stack.get_min() == 3
    val = min_stack.pop()
    print(f"popped {val}")
    assert val == 7
    assert min_stack.get_min() == 3
    val = min_stack.pop()
    print(f"popped {val}")
    assert val == 3
    assert min_stack.get_min() == 5
