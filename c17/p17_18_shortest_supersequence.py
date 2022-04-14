import heapq
import typing as ty
from collections import deque

import tlog

NOT_FOUND = -1


def main():
    big_array = [int(c) for c in "75902135791158897"]
    tlog.info(f"{big_array}")
    small_array = [int(c) for c in "159"]
    # print(get_shortest_brute_force(big_array, small_array))
    print(get_shortest_seq_heap(big_array, small_array))


def get_shortest_seq_heap(big_array: ty.List, small_array: ty.List):
    locations: ty.Dict[str, ty.List] = get_locations(big_array, small_array)
    if locations is None:
        return None
    return get_shortest_closure(locations)


def get_locations(big_array: ty.List, small_array: ty.Deque):
    locations = {k: deque([]) for k in small_array}
    for i, c in enumerate(big_array):
        if c in locations:
            locations[c].append(i)
    return locations


def get_shortest_closure(locations: ty.Dict[str, ty.Deque]):
    heap = [(val.popleft(), k) for k, val in locations.items()]

    tlog.info("heapifying", initial_arr=heap)
    heapq.heapify(heap)
    tlog.info("heapified", heap=heap)

    max_so_far, _ = max(heap)
    min_so_far, _ = heap[0]
    tlog.info("max and min", max_so_far=max_so_far, min_so_far=min_so_far)

    best_max, best_min = max_so_far, min_so_far

    while True:
        min_so_far, k_ = heapq.heappop(heap)
        q = locations[k_]
        if max_so_far - min_so_far < best_max - best_min:
            best_max, best_min = max_so_far, min_so_far

        if len(q) == 0:
            break
        loc_in_q = q.popleft()
        heapq.heappush(heap, (loc_in_q, k_))
        max_so_far = max(max_so_far, loc_in_q)

    return best_min, best_max


def get_shortest_brute_force(big_array: ty.List, small_array: ty.List):
    best_start = NOT_FOUND
    best_end = NOT_FOUND
    for i in range(len(big_array)):
        end = find_closure(big_array=big_array, small_array=small_array, idx=i)
        if end == NOT_FOUND:
            break
        if best_start == NOT_FOUND or end - i < best_end - best_start:
            best_start = i
            best_end = end
    return best_start, best_end


def find_closure(big_array, small_array, idx):
    max_so_far = -1
    for i in range(len(small_array)):
        next_instance = find_next_instance(
            big_array, small_elem=small_array[i], idx=idx
        )
        if next_instance == NOT_FOUND:
            return NOT_FOUND
        max_so_far = max(max_so_far, next_instance)
    return max_so_far


def find_next_instance(big_array, small_elem, idx):
    for i in range(idx, len(big_array)):
        if big_array[i] == small_elem:
            return i
    return NOT_FOUND
