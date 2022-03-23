import typing as ty
import tlog
from collections import defaultdict


def main():
    names = {
        "john": 10,
        "jon": 3,
        "davis": 2,
        "kari": 3,
        "johny": 11,
        "carlton": 8,
        "carleton": 2,
        "jonathan": 9,
        "carrie": 5,
    }
    synonyms = [
        ("jonathan", "john"),
        ("jon", "johny"),
        ("johny", "john"),
        ("kari", "carrie"),
        ("carleton", "carlton"),
    ]
    truly_most_popular = get_truly_most_popular(names=names, synonyms=synonyms)
    print(truly_most_popular)


def get_truly_most_popular(names, synonyms):
    parents = build_parents(names, synonyms)
    tlog.info("found parents", parents=parents)
    res = get_res_from_parents(names, parents)
    return res


def get_res_from_parents(names: ty.Dict, parents):
    res = defaultdict(int)
    for name, count in names.items():
        r = find(name, parents)
        res[r] += count

    return dict(res)


def build_parents(names: ty.Dict, synonyms: ty.List[ty.Tuple]):
    parents = dict()
    for name in names.keys():
        parents[name] = name

    for name1, name2 in synonyms:
        union(name1, name2, parents)

    return parents


def union(name1, name2, parents):
    r1 = find(name1, parents)
    r2 = find(name2, parents)
    if r1 != r2:
        parents[r1] = r2


def find(name, parents):
    while name != parents[name]:
        name = parents[name]
    return name
