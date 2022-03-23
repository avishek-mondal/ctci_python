import random


def main():
    original = [i for i in range(1, 9)]
    m = 4
    m_set = pick_m(original, m)
    print(m_set)


def pick_m(original: list, m: int):
    """We want each element of the array to have a probability m/n
    of choosing.

    This is called a reservoir family of algorithms
    https://en.wikipedia.org/wiki/Reservoir_sampling

    Args:
        original (list): _description_
        m (int): _description_

    Returns:
        _type_: _description_
    """

    n = len(original)

    # we are constructing subset here, so we need
    # m <=n
    if m > n:
        return None

    m_set = [original[i] for i in range(m)]

    for i in range(m, n):
        k = random.randint(0, i)
        if k < m:
            m_set[k] = original[i]

    return m_set
