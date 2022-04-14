class FullStackException(Exception):
    pass


class EmptyStackException(Exception):
    pass


class MultiStack:
    class StackInfo:
        def __init__(self, start: int, capacity: int, outer):
            self.outer = outer
            self.start = start
            self.capacity = capacity
            self.end = start + capacity
            self.size = 0

        def is_full(self) -> bool:
            return self.size == self.capacity

        def is_empty(self) -> bool:
            return self.size == 0

        def is_within_stack_capacity(self, idx):
            arr_len = len(self.outer.arr)
            if idx < 0 or idx >= arr_len:
                return False
            contiguous_idx = idx if idx >= self.start else idx + arr_len
            return self.start <= contiguous_idx and contiguous_idx < self.end

        def last_capacity_idx(self):
            return self.outer.adjust_idx(self.start + self.capacity - 1)

        def last_elem_idx(self):
            return self.outer.adjust_idx(self.start + self.size - 1)

    def __init__(self, sizeof_stack, num_stacks, stack_cap: int = 15):
        self.sizeof_stack = sizeof_stack
        self.num_stacks = num_stacks
        self.arr = [0] * (self.sizeof_stack * self.num_stacks)
        self.sizes = [0] * self.num_stacks
        self.info = [
            self.StackInfo(start=i * stack_cap, capacity=stack_cap, outer=self)
            for i in range(num_stacks)
        ]

    def num_of_elements(self):
        size = 0
        for stack_info in self.info:
            size += stack_info.size
        return size

    def all_stacks_are_full(self) -> bool:
        return self.num_of_elements() == len(self.arr)

    def adjust_idx(self, idx: int) -> int:
        return idx % len(self.arr)

    def next_idx(self, idx: int) -> int:
        return self.adjust_idx(idx + 1)

    def prev_idx(self, idx: int) -> int:
        return self.adjust_idx(idx - 1)

    def shift(self, stack_num):
        stack_info = self.info[stack_num]
        # if stack is at full capacity, you need to shift the next stack
        if stack_info.size >= stack_info.capacity:
            next_stack = (stack_num + 1) % self.num_stacks
            self.shift(next_stack)
            stack_info.capacity += 1

        idx = stack_info.last_capacity_idx()
        while stack_info.is_within_stack_capacity(idx):
            self.arr[idx] = self.arr[self.prev_idx(idx)]
            idx = self.prev_idx(idx)

        self.arr[stack_info.start] = 0
        stack_info.start = self.next_idx(stack_info.start)
        stack_info.capacity -= 1

    def expand(self, stack_num: int):
        self.shift((stack_num + 1) % self.num_stacks)
        self.info[stack_num].capacity += 1

    def push(self, value, stack_num):
        if self.all_stacks_are_full():
            raise FullStackException()

        stack_info = self.info[stack_num]

        if stack_info.is_full():
            self.expand(stack_num)

        stack_info.size += 1
        self.arr[stack_info.last_elem_idx()] = value

    def pop(self, stack_num):
        stack_info = self.info[stack_num]

        if stack_info.is_empty():
            raise EmptyStackException()

        value = self.arr[stack_info.last_elem_idx()] = 0
        stack_info.size -= 1
        return value

    def peek(self, stack_num):
        stack_info = self.info[stack_num]
        return self.arr[stack_info.last_elem_idx()]

    def get_values(self):
        return self.arr

    def get_stack_values(self, stack_num):
        stack_info = self.info[stack_num]
        start_idx = stack_info.start
        l = stack_info.size
        return [self.arr[self.adjust_idx(start_idx + i)] for i in range(l)]


def main():
    newstack = MultiStack(sizeof_stack=3, num_stacks=10)
    print(newstack.info[0].is_within_stack_capacity(5))
