import requests
import logging

from bs4 import BeautifulSoup

from src.crawling.http import make_headers
from src.crawling.bloomberg.core import crawl_title
from src.crawling.bloomberg.core import crawl_article
from src.crawling.bloomberg.core import crawl_author
from src.crawling.bloomberg.core import crawl_timestamp
from src.crawling.bloomberg.core import crawl_metadata
from src.crawling.bloomberg.core import crawl_ticker_symbols
from graphify.parsing import parse_iterable

from selenium.webdriver.chrome.webdriver import WebDriver
from src.webdriver import api


logger = logging.getLogger(__name__)


def parse_article(driver: WebDriver, url: str):
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

    html = api.get(driver, url,  make_headers(source='bloomberg'), wait_for=2)
    soup = BeautifulSoup(html)
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
    doc['symbols'] = crawl_ticker_symbols(driver=driver, soup=soup)

    # TODO: meta, e.g likes and comments are still with problems
    doc['meta'] = crawl_metadata(soup)

    return doc


if __name__ == '__main__':

    from pprint import pprint
    from src.webdriver import init_chrome_driver

    driver = init_chrome_driver()
    url = 'https://www.bloomberg.com/news/articles/2019-12-05/boeing-tries-to-win-over-pilots-attendants-with-737-max-pitch'

    article = parse_article(driver, url)
    pprint(article)


