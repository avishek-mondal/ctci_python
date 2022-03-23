from c17.word_set import word_set
import tlog


class ParseResult:
    def __init__(self, parsed: str, invalid_chars: int):
        self.parsed: str = parsed
        self.invalid_chars = invalid_chars


def main():
    sentence = "As one of the topk companies in the world, Google will surely attract the attention of computer gurus. This does not, however, mean the company is for everyone."
    sentence = despace(sentence)
    tlog.info("putting in sentence", sentence=sentence)
    res = best_split(sentence=sentence, dictionary=word_set)
    print(res)


def best_split(sentence, dictionary):
    memo = [None for _ in range(len(sentence))]
    res = split_sentence(
        sentence=sentence, dictionary=dictionary, start=0, memo=memo
    )
    tlog.info("gotten res", invalid_chars=res.invalid_chars)
    return res.parsed if res else None


def split_sentence(
    sentence: str, dictionary: set, start: int, memo: list
) -> ParseResult:
    if start >= len(sentence):
        return ParseResult(parsed="", invalid_chars=0)
    if memo[start]:
        return memo[start]

    best_invalid = float("inf")
    best_parsing, partial = "", ""
    for idx in range(start, len(sentence)):
        char_ = sentence[idx]
        partial = f"{partial}{char_}"
        num_invalid = 0 if partial in dictionary else len(partial)

        if num_invalid < best_invalid:
            tmp_res = split_sentence(
                sentence=sentence,
                dictionary=dictionary,
                start=idx + 1,
                memo=memo,
            )
            if num_invalid + tmp_res.invalid_chars < best_invalid:
                best_invalid = num_invalid + tmp_res.invalid_chars
                best_parsing = f"{partial} {tmp_res.parsed}"
                if best_invalid == 0:
                    break

    if start == len(sentence) - 1:
        tlog.info(
            "in the last",
            start=start,
            best_parsing=best_parsing,
            best_invalid=best_invalid,
        )
    memo[start] = ParseResult(parsed=best_parsing, invalid_chars=best_invalid)
    tlog.info("returning memo", memo=memo)
    return memo[start]


def despace(sentence: str) -> str:
    punctuations = [",", '"', "!", ".", "'", "?", ","]
    for c in punctuations:
        sentence = sentence.replace(c, " ")
    return sentence.replace(" ", "").lower()
