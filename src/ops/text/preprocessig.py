import re

from functools import reduce
from typing import List


def clean_text(text: List[str], patterns: List) -> List[str]:
    """
    Clean every occurrence of 'patterns' in
    every line 'text'

    If any given line becomes blank it is removed
    """
    patterns = list(map(re.compile, patterns))

    def clean(line):
        return reduce(lambda acc, x: x.sub('', acc), patterns, line)

    cleaned_text = [clean(line) for line in text]
    cleaned_text = [line for line in cleaned_text if line]
    return cleaned_text
