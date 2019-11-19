import spacy

from functools import reduce
from typing import List

nlp = spacy.load("en_core_web_sm")


def merge_sentences_min_len(text: List[str], min_len: int) -> List[str]:
    """
    Combine multiple sentences to ensure
    every one has at least a length of `min_len`
    """

    def reducer(acc, x):
        if acc and (sum(map(len, acc[-1])) < min_len):
            acc[-1].append(x)
            return acc
        else:
            return acc + [[x]]

    new_text = ['. '.join(sents) for sents in reduce(reducer, text, [])]

    return new_text


def merge_sentences(text: List[str], min_len: int) -> List[str]:
    """
    Combine multiple sentences to ensure
    every one has a minimum number of tokens
    """

    def reducer(acc, x):
        x = x.strip()

        if acc and (len(nlp(acc[-1])) < min_len):
            if acc[-1] and (acc[-1][-1]) not in ['.', ':']:
                acc[-1] += '. {}'.format(x)
            else:
                acc[-1] += ' {}'.format(x)
            return acc
        else:
            return acc + [x]

    new_text = reduce(reducer, text, [])
    return new_text










