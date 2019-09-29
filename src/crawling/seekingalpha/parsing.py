import requests
from bs4 import BeautifulSoup

from src.crawling.seekingalpha.core import crawl_seekingalpha_article
from src.crawling.seekingalpha.core import headers
from src.crawling.seekingalpha.core import crawl_seekingalpha_author
from graphify.parsing import parse_iterable


def parse_seekingalpha_article(url):

    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.content)

    hierarchy = ['Article', 'Section', 'Paragraph']

    descriptor = {
        'components': hierarchy,
        'patterns': hierarchy
    }

    text = crawl_seekingalpha_article(soup)
    doc = parse_iterable(text, descriptor)

    doc = doc.to_dict()
    doc['url'] = url

    doc['author'] = crawl_seekingalpha_author(soup)

    return doc


if __name__ == '__main__':
    from pprint import pprint

    url = 'https://seekingalpha.com/article/4294053-mlps-sell-purpose'

    article = parse_seekingalpha_article(url)

    pprint(article)


