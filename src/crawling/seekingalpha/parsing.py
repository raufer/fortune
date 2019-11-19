import requests
from bs4 import BeautifulSoup

from src.crawling.http import make_headers
from src.crawling.seekingalpha.core import crawl_seekingalpha_article, crawl_title
from src.crawling.seekingalpha.core import crawl_timestamp
from src.crawling.seekingalpha.core import crawl_metadata
from src.crawling.seekingalpha.core import crawl_seekingalpha_author
from graphify.parsing import parse_iterable


def parse_seekingalpha_article(url):

    result = requests.get(url, headers=make_headers())
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
    doc['title'] = crawl_title(soup)
    doc['author'] = crawl_seekingalpha_author(soup)
    doc['timestamp'] = crawl_timestamp(soup)

    # TODO: meta, e.g likes and comments are still with problems
    doc['meta'] = crawl_metadata(soup)

    return doc


if __name__ == '__main__':
    from pprint import pprint

    url = 'https://seekingalpha.com/article/4295543-fiverr-exciting-growth-play-takes-patience'

    article = parse_seekingalpha_article(url)

    pprint(article)


