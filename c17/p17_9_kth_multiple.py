import heapq
from copy import deepcopy


def main():
    factors = [3, 5, 7]
    k = 1000
    kth_mult = get_kth_multiple(k, factors)
    print(kth_mult)


def get_kth_multiple(k, factors):
    res = []
    heap = deepcopy(factors)
    seen = set()
    heapq.heapify(heap)

    for _ in range(k):
        next_el = heapq.heappop(heap)
        res.append(next_el)
        for factor in factors:
            if factor * next_el not in seen:
                to_add = factor * next_el
                seen.add(to_add)
                heapq.heappush(heap, to_add)

    return res
