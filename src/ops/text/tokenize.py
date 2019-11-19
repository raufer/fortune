import spacy

from typing import List


nlp = spacy.load("en_core_web_sm")


def tokenize_sentences(article: str) -> List[str]:
    """
    Split a chunk of text into various sentences
    """
    if not article:
        return [article]

    doc = nlp(article)
    sentences = [sent.text for sent in doc.sents]
    return sentences
