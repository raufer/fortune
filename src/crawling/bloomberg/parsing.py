import requests
import logging

from bs4 import BeautifulSoup

from src.crawling.http import make_headers
from src.crawling.bloomberg.core import crawl_title
from src.crawling.bloomberg.core import crawl_article
from src.crawling.bloomberg.core import crawl_author
from src.crawling.bloomberg.core import crawl_timestamp
from src.crawling.bloomberg.core import crawl_metadata
from graphify.parsing import parse_iterable


logger = logging.getLogger(__name__)


def parse_article(url):
    logger.info(f"Parsing article '{url}'")

    headers = make_headers(source='bloomberg')
    logger.debug('Using Headers:')
    logger.debug(headers)
    result = requests.get(url, headers=headers)

    soup = BeautifulSoup(result.content)
    logger.debug(f"Soup length '{len(soup)}'")

    hierarchy = ['Article', 'Paragraph']

    descriptor = {
        'components': hierarchy,
        'patterns': hierarchy
    }

    text = crawl_article(soup)
    logger.info(f"Text crawled. Number of lines '{len(text)}'")

    logger.info(f"Creating a graph")
    doc = parse_iterable(text, descriptor)
    doc = doc.to_dict()

    doc['url'] = url
    doc['title'] = crawl_title(soup)
    doc['author'] = crawl_author(soup)
    doc['timestamp'] = crawl_timestamp(soup)
    # TODO: meta, e.g likes and comments are still with problems
    doc['meta'] = crawl_metadata(soup)

    return doc


if __name__ == '__main__':
    from pprint import pprint

    url = 'https://www.bloomberg.com/news/articles/2019-12-05/boeing-tries-to-win-over-pilots-attendants-with-737-max-pitch'

    article = parse_article(url)

    pprint(article)


