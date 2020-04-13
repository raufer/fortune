import re
import spacy

from typing import Union
from typing import List

from itertools import dropwhile

nlp = spacy.load("en_core_web_sm")


def scan_inserts(text: Union[List[str], str]) -> Union[List[str], str]:
    """
    Given an input text detect if there is any
    block of text that should be 'inserted' / 'added'
    e.g.
        After paragraph 2 insert:
        ```
        - (h) condition 1
        - (j) condition 2
        ```
    """
    patterns = [
        r'(after|before)[a-zA-Z0-9\.\-\s\(\)]{1,40}insert'
    ]

    patterns = [re.compile(p) for p in patterns]

    def insertion_signal(line):
        return any(p.search(line) for p in patterns)

    new_text = dropwhile(lambda x: not insertion_signal(x), text)
    return list(new_text)


def token_count(text: Union[str, List[str]]):
    """
    Returns the token count of `text`
    Uses spacy tokenization
    """
    if isinstance(text, str):
        text = [text]
    return sum((len(nlp(l)) for l in text))









