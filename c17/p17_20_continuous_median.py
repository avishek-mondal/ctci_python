import heapq
import random

import tlog


class ContinuousMedian:
    def __init__(self):
        self.max_heap = []  # for numbers below median
        self.min_heap = []  # for numbers above median

    def __str__(self):
        return f"(max_heap={self.max_heap}, min_heap={self.min_heap})"

    def add_elem(self, num):
        min_len = len(self.min_heap)
        max_len = len(self.max_heap)
        if min_len == max_len:
            if min_len > 0 and num > self.min_heap[0]:
                min_above_median = heapq.heappop(self.min_heap)
                heapq.heappush(self.max_heap, -min_above_median)
                heapq.heappush(self.min_heap, num)
            else:
                heapq.heappush(self.max_heap, -num)
        else:
            if (
                num < -self.max_heap[0]
            ):  # num is smaller than max num below median
                max_below_median = -heapq.heappop(self.max_heap)
                heapq.heappush(self.min_heap, max_below_median)
                heapq.heappush(self.max_heap, -num)
            else:
                heapq.heappush(self.min_heap, num)

    def get_median(self):
        if len(self.max_heap) == 0:
            tlog.error("max heap is empty!", self=self)
            return 0
        if len(self.max_heap) == len(self.min_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else:
            return -self.max_heap[0]


def main():
    n = 10
    arr = [random.randint(0, n - 1) for _ in range(n)]
    print(arr)
    continuous_median = ContinuousMedian()
    for i in arr:
        print(f"adding i = {i}")
        continuous_median.add_elem(i)
        print(f"median = {continuous_median.get_median()}")
