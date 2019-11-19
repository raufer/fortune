import re

from typing import Dict, Union, List


def find_first(doc: Dict, meta: Union[List[str], str], pattern: str):
    """
    Given a document, return the first id of a node[any(meta == `meta`)]
    where the first line of `text` contains a given `pattern`
    """
    if isinstance(meta, str):
        meta = [meta]

    pattern = re.compile(pattern)

    search_space = (n for n in doc['nodes'] if any(n['content']['meta'] == m for m in meta) and n['content']['text'])
    result = next((n['content']['id'] for n in search_space if pattern.search(n['content']['text'][0])), None)
    return result
