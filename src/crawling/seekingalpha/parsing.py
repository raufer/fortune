import requests

from src.crawling.seekingalpha.core import crawl_seekingalpha_article
from graphify.parsing import parse_iterable


def parse_seekingalpha_article(url):
    hierarchy = ['Article', 'Section', 'Paragraph']

    descriptor = {
        'components': hierarchy,
        'patterns': hierarchy
    }

    text = crawl_seekingalpha_article(url)
    doc = parse_iterable(text, descriptor)
    return doc

    doc = doc.to_dict()
    doc['url'] = url

    doc['author'] = ...

    return doc


if __name__ == '__main__':
    from pprint import pprint

    url = 'https://seekingalpha.com/article/4293834-offshore-drilling-jack-fundamentals-september-2019-edition'

    article = parse_seekingalpha_article(url)
    print(article)


