import typing as ty


def main():
    standard_coin_size = [1, 5, 10, 25]
    amt = 100
    bf_res = make_change_bf(total=amt, denoms=standard_coin_size)
    print(bf_res)
    two_d_res = make_change_2d(total=amt, denoms=standard_coin_size)
    print(two_d_res)


def make_change_2d(total, denoms):
    memo = dict()
    return make_change_2d_helper(total=total, denoms=denoms, idx=0, memo=memo)


def make_change_2d_helper(total, denoms, idx, memo):
    if (total, idx) in memo:
        return memo[(total, idx)]

    coin = denoms[idx]
    if idx == len(denoms) - 1:
        return 1 if total % coin == 0 else 0

    ways = 0
    for amt in range(0, total + 1, coin):
        ways += make_change_2d_helper(total - amt, denoms, idx + 1, memo)

    memo[(total, idx)] = ways
    return ways


def make_change_bf(total: int, denoms: ty.List):
    return make_change_bf_helper(total=total, denoms=denoms, idx=0)


def make_change_bf_helper(total, denoms, idx):
    coin = denoms[idx]
    if idx == len(denoms) - 1:
        return 1 if total % coin == 0 else 0

    ways = 0
    for amt in range(0, total + 1, coin):
        ways += make_change_bf_helper(total - amt, denoms, idx + 1)
    return ways
