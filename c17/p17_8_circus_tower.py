import typing as ty
from copy import deepcopy


def main():
    ht_wt = [(65, 100), (70, 150), (56, 90), (75, 190), (60, 95), (68, 110)]
    arr = [HtWt(*i) for i in ht_wt]
    # res = longest_increasing_seq_recursive(arr)
    # print(len(res))
    res = longest_increasing_seq_iterative(arr)
    print(len(res))


class HtWt:
    def __init__(self, ht, wt):
        self.ht = ht
        self.wt = wt

    def __lt__(self, other: "HtWt"):
        if self.ht != other.ht:
            return self.ht <= other.ht
        else:
            self.wt <= other.wt

    def __eq__(self, other: "HtWt"):
        return self.ht == other.ht and self.wt == other.wt

    def __str__(self):
        return f"HtWt(ht={self.ht}, wt={self.wt})"


def longest_increasing_seq_iterative(arr: ty.List[HtWt]):
    arr.sort(reverse=True)
    best_sequence = []
    solns = []

    for i in range(len(arr)):
        longest_at_idx = get_longest_at_idx(arr=arr, solns=solns, idx=i)
        solns.append(longest_at_idx)
        best_sequence = (
            best_sequence
            if len(best_sequence) > len(longest_at_idx)
            else longest_at_idx
        )

    return best_sequence


def get_longest_at_idx(arr: ty.List[HtWt], solns, idx):
    val = arr[idx]
    best_seq = []
    for i in range(idx):
        soln = solns[i]
        if can_append(soln, val):
            best_seq = best_seq if len(best_seq) > len(soln) else soln
    best = deepcopy(best_seq)
    best.append(val)
    return best

def longest_increasing_seq_recursive(ht_wt: ty.List):
    ht_wt.sort(reverse=True)
    return best_seq_at_idx(ht_wt=ht_wt, res=[], idx=0)


def best_seq_at_idx(ht_wt, res, idx):
    if idx >= len(ht_wt):
        return res
    val = ht_wt[idx]

    best_with = []
    if can_append(res, val):
        seq_with = deepcopy(res)
        seq_with.append(val)
        best_with = best_seq_at_idx(ht_wt, res=seq_with, idx=idx + 1)

    best_without = best_seq_at_idx(ht_wt, res=res, idx=idx + 1)

    return best_with if len(best_with) > len(best_without) else best_without


def can_append(res: ty.List, val: HtWt):
    return len(res) == 0 or res[-1] > val
