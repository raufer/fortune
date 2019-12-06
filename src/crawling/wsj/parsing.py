import logging
import requests
from datetime import datetime
from bs4 import BeautifulSoup

from src.crawling.http import make_headers
from src.crawling.wsj.core import crawl_title
from src.crawling.wsj.core import crawl_article
from src.crawling.wsj.core import crawl_author
from src.crawling.wsj.core import crawl_timestamp
from src.crawling.wsj.core import crawl_metadata
from graphify.parsing import parse_iterable

from typing import Dict


logger = logging.getLogger(__name__)


def parse_article(url) -> Dict:
    """
    Given an article, parse its content into a
    representation that preserves the structure

    * Grab the HTML page
    * Crawl its contents
    * Tag the text with the different hierarchical components
    * Parse the resulting output into a graph
    * Enrich with metadata:
        - author information: name, url, etc;
        - document title;
        - publishing timestamp;
        - other metadata;
    """
    logger.info(f"Parsing article '{url}'")

    headers = make_headers(source='wsj')

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
    doc['meta'] = crawl_metadata(soup)

    return doc


if __name__ == '__main__':
    from pprint import pprint

    url = 'https://www.wsj.com/articles/how-johnson-johnson-shares-can-get-well-11574180520'

    article = parse_article(url)

    # pprint(article)


