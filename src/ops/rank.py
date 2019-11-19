from collections import Counter
from typing import List


def most_frequent(x: List, n: int) -> List:
    """
    Returns the `n` most frequent items of `x`
    """
    counts = Counter(x)
    sorted_count = sorted(counts.items(), key=lambda x: x[1], reverse=True)
    most_frequent = [k for k, _ in sorted_count][:n]
    return most_frequent


