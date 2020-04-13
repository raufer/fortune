import logging
import requests

from urllib.parse import urljoin
from bs4 import BeautifulSoup
from typing import List
from typing import Tuple

from src.crawling.seekingalpha.core import base

logger = logging.getLogger(__name__)


def list_articles(url: str) -> List[Tuple[str, str]]:
    """
    Given a url pointing to a page that lists the
    (latest) articles, parses all of the elements
    and returns a list of them :: [(name, url)]
    """
    logger.info(f"Listing articles in '{url}'")
    result = requests.get(url)
    soup = BeautifulSoup(result.content)

    items = soup.find_all('li', class_='article media')
    items = filter(bool, [i.find('div', class_='media-body') for i in items])
    items = filter(bool, [i.find('a') for i in items])

    articles = ((item.get_text().strip(), item.get('href')) for item in items)

    articles = [
        (name, urljoin(base, href))
        for name, href in articles if href is not None
    ]

    logger.info(f"Found '{len(articles)}' articles")

    for name, url in articles:
        logger.info(f"{name} ({url})")

    return articles


if __name__ == '__main__':
    from pprint import pprint

    url = 'https://seekingalpha.com/stock-ideas'

    list_articles(url)
