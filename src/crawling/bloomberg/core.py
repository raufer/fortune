import requests
import logging
import time

import src.crawling.webdriver as webdriver

from typing import Dict
from typing import List
from typing import Tuple
from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from functools import reduce

from src.crawling.http import make_headers
from src.ops.text.tokenize import tokenize_sentences

base = 'https://www.bloomberg.com'

logger = logging.getLogger(__name__)


def crawl_ticker_symbols(soup, url) -> List[Tuple[str, str]]:
    """
    Extracts all of the ticker symbols that are involved
    Returns a list of strings [(exchange, symbol)]
    """
    logger.info(f"Extracting ticker symbols in article scope")

    driver = webdriver.init_phantomjs_driver(headers=make_headers(source='bloomberg'))
    html = webdriver.get(driver, url, wait_for=4)
    soup = BeautifulSoup(html)

    section = soup.find('div', class_='blens', recursive=True)

    stocks = section.find("div", class_=lambda v: v and v.startswith("instruments__"), recursive=True)
    stocks = [s.find('a') for s in stocks.find_all('div', recursive=False)]
    stocks = [urljoin(base, s['href']) for s in stocks if not s['href'].split('/')[-1][0].isdigit()]

    logger.debug(f"'{len(stocks)}' stocks")

    pages = [requests.get(url, headers=make_headers(source='bloomberg')) for url in stocks]

    sections = [BeautifulSoup(result.content) for result in pages]
    sections = [
        section.find('section', class_=lambda v: v and v.startswith("company__"), recursive=True)
        for section in sections
    ]

    symbols = [
        (
            section.find('span', class_=lambda v: v and v.startswith("exchange__")).get_text().strip(),
            section.find('span', class_=lambda v: v and v.startswith("companyId__")).get_text().strip().split(":")[0]
        )
        for section in sections
    ]

    translate = {
        'New York': 'NYSE',
        'NASDAQ GS': 'NASDAQ'
    }

    symbols = [(translate[exchange], ticker) for exchange, ticker in symbols]

    logger.info(f"Symbols found: '{[(s[0] + str('::') + s[1]) for s in symbols]}'")

    return symbols


def crawl_author(soup) -> Dict:
    logger.debug(f"Extracting author information")
    article_tag = soup.find('div', class_='article-content')

    author_url = article_tag.find('div', class_='author-v2').find('a')['href']
    logger.debug(f"Author URL: '{author_url}'")

    author_name = article_tag.find('div', class_='author-v2').find('a').get_text().strip()
    logger.debug(f"Author Name: '{author_name}'")

    # TODO: parse remaning data (needs JS)
    result = {
        'name': author_name,
        'url': author_url,
        # 'followers': followers,
        # 'articles': articles
    }

    logger.debug(f"Author Information: '{result}'")
    return result


def crawl_title(soup) -> str:
    """
    Extracts main title of the article
    """
    logger.debug(f"Extracting title")

    article_tag = soup.find('div', class_='article-content')
    title = article_tag.find('h1', class_='lede-text-v2__hed').get_text().strip()

    logger.info(f"Article title '{title}'")
    return title


def crawl_timestamp(soup) -> str:
    """
    Return timestamp in ISO 8601 UTC format
    https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    """
    logger.debug(f"Extracting timestamp")

    date = soup.find('time', class_='article-timestamp')

    if date:
        timestamp = date['datetime']
    else:
        timestamp = None

    logger.info(f"Article timestamp '{timestamp}'")
    return timestamp


def _crawl_summary(soup) -> List[str]:
    """
    Extracts a summary that that is able
    to provide a short description of the article
    """
    logger.debug(f"Extracting summary")
    section = soup.find('div', class_='body-copy-v2 fence-body')
    summary = section.find('p', recursive=True).get_text().strip()
    logger.debug(f"Summary: '{summary}'")
    summary = ["[[Article]]Summary."] + ["[[Paragraph]]Paragraph 0."] + [summary]
    logger.debug(f"Summary w/ structure: '{summary}'")
    return summary


def _crawl_body(soup):
    logger.debug(f"Extracting body")

    section = soup.find('section', class_='main-column-v2')
    body = section.find('div', class_='body-copy-v2 fence-body')

    items = body.find_all(['h1', 'h2', 'h3', 'h4', 'p'], recursive=False)
    logger.debug(f"Number of items: '{len(items)}'")

    def reducer(acc, x):
        if not acc:
            return [[x]]

        elif x.name in ['h2', 'h3']:
            return acc + [[x]]

        elif x.name == 'div':
            return acc

        else:
            acc[-1].append(x)
            return acc

    grouped = reduce(reducer, items, [])
    logger.debug(f"Number of groups: '{len(grouped)}'")

    paragraphs = [
        ['[[Paragraph]]{}'.format(group[0].get_text().strip())] +
        sum([tokenize_sentences(xs.get_text().strip()) for xs in group[1:]], [])
        for group in grouped if group
    ]

    paragraphs = sum(paragraphs, [])

    return paragraphs


def crawl_article(x):
    """
    Crawls the full article.
    Adds top level section `Article` with the main
    title of document
    """
    logger.debug(f"Crawling article")

    if isinstance(x, str):
        result = requests.get(x)
        soup = BeautifulSoup(result.content)
    else:
        soup = x

    title = crawl_title(soup)
    summary = _crawl_summary(soup)
    body = _crawl_body(soup)

    article = ["[[Article]]{}.".format(title)] + summary + body
    return article


def crawl_metadata(soup) -> Dict:
    """
    Returns article metadata,
    e.g. number of likes, comments, etc
    """
    logger.debug(f"Crawling metadata")
    # TODO: no metadata?
    return {}


if __name__ == '__main__':
    url = 'https://www.bloomberg.com/news/articles/2019-12-05/boeing-tries-to-win-over-pilots-attendants-with-737-max-pitch'

    result = requests.get(url, headers=make_headers(source='bloomberg'))
    soup = BeautifulSoup(result.content)

    crawl_ticker_symbols(soup, url)
