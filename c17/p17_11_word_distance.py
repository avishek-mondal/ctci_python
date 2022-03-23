import typing as ty
import tlog


def main():
    doc = """
    this is an example of a document that

    We will use in testing
    Use words like this and that and document and things
    and then testing
    """

    words = doc.replace("\n", " ").strip().split()
    word2loc = get_word2loc(words)
    s1 = "this"
    s2 = "testing"
    print(find_closest(s1=s1, s2=s2, word2loc=word2loc))


def find_closest(s1, s2, word2loc) -> ty.Tuple:
    """Find closest given pre computation

    O(A + B) => A = len(s1), B = len(s2)

    Args:
        s1: first string
        s2: second string
        word2loc: dict

    Returns:
        tuple
    """
    if not word2loc.get(s1) or not word2loc.get(s2):
        tlog.error(
            "make sure s1, s2 are in word2loc", s1=s1, s2=s2, word2loc=word2loc
        )
        return None
    s1_locs = word2loc.get(s1)
    s2_locs = word2loc.get(s2)
    tlog.info(
        "before loop", s1_locs=s1_locs, s2_locs=s2_locs, word2loc=word2loc
    )
    best_pair = (float("inf"), -float("inf"))
    idx1, idx2 = 0, 0
    while idx1 < len(s1_locs) and idx2 < len(s2_locs):
        best_dist = abs(best_pair[0] - best_pair[1])
        cur1 = s1_locs[idx1]
        cur2 = s2_locs[idx2]
        cur_dist = abs(cur1 - cur2)
        if cur_dist < best_dist:
            tlog.info(
                "updating best_dist", cur=(cur1, cur2), best_pair=best_pair
            )
            best_pair = (cur1, cur2)
        if cur1 < cur2:
            idx1 += 1
        else:
            idx2 += 1
    return best_pair


def get_word2loc(words: ty.List[str]):
    word2loc = dict()
    for i, word in enumerate(words):
        arr = word2loc.get(word, [])
        arr.append(i)
        word2loc[word] = arr
    return word2loc
