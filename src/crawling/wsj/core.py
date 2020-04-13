import re
import requests
import logging

from typing import Dict
from typing import List
from typing import Tuple

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from functools import reduce

from src.crawling.http import make_headers
from src.ops.text.tokenize import tokenize_sentences
from src.ops.datetime import safe_datetime_to_iso

from selenium.webdriver.chrome.webdriver import WebDriver
from src.webdriver import api

base = 'https://www.wsj.com/news/business'


logger = logging.getLogger(__name__)


def crawl_ticker_symbols(driver: WebDriver = None, url: str = None, soup=None) -> List[Tuple[str, str]]:
    """
    Extracts all of the ticker symbols that are involved
    Returns a list of strings [(exchange, symbol)]
    """
    logger.info(f"Extracting ticker symbols in article scope")

    if soup is None:
        html = api.get(driver, url, headers=make_headers('wsj'), wait_for=2)
        soup = BeautifulSoup(html)

    stocks = soup.find_all('a', class_=lambda v: v and v.startswith("media-object-chiclet"), recursive=True)
    logger.debug(f"'{len(stocks)}' stocks")

    urls = list(set([urljoin(base, s['href']) for s in stocks]))
    pages = [api.get(driver, url, headers=make_headers(source='wsj')) for url in urls]

    sections = [BeautifulSoup(html).find('div', class_='cr_quotesHeader') for html in pages]

    symbols = [
        (
            re.search(r'.+:\s?([A-Z0-9a-z]+)\)?', section.find('span', class_='exchangeName', recursive=True).get_text()).group(1),
            section.find('span', class_='tickerName', recursive=True).get_text().strip()
        )
        for section in sections
    ]

    logger.info(f"Symbols found: '{[(s[0] + str('::') + s[1]) for s in symbols]}'")

    return symbols


def crawl_author(soup):
    logger.debug(f"Extracting author information")
    author_info = soup.find('ul', class_='author-info')

    author_name = author_info.find('div', class_='info-name').get_text().strip()
    logger.debug(f"Author Name: '{author_name}'")

    author_url = author_info.find('li').find('a')['href']
    logger.debug(f"Author URL: '{author_url}'")

    # TODO: add extra fields
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

    section = soup.find('div', class_='wsj-article-headline-wrap')
    title = section.find('h1').get_text().strip()

    logger.info(f"Article title '{title}'")
    return title


def crawl_timestamp(soup) -> str:
    """
    Return timestamp in ISO 8601 UTC format
    https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    """
    logger.debug(f"Extracting timestamp")

    timestamp_tag = soup.find('time', class_='timestamp article__timestamp flexbox__flex--1')
    timestamp_txt = timestamp_tag.get_text().strip().replace(' ET', '')

    input_formats = [
        '%b. %d, %Y %I:%M %p',
        '%B %d, %Y %I:%M %p'
    ]

    timestamp = safe_datetime_to_iso(timestamp_txt, input_formats)

    logger.info(f"Article timestamp '{timestamp}'")
    return timestamp


def _crawl_summary(soup) -> List[str]:
    """
    Extracts a summary that that is able
    to provide a short description of the article
    """
    logger.debug(f"Extracting summary")
    section = soup.find('div', class_='wsj-article-headline-wrap')
    summary = section.find('h2').get_text().strip()
    logger.debug(f"Summary: '{summary}'")
    summary = ["[[Article]]Summary."] + ["[[Paragraph]]Paragraph 0."] + [summary]
    logger.debug(f"Summary w/ structure: '{summary}'")
    return summary


def _crawl_body(soup):
    logger.debug(f"Extracting body")

    body = soup.find('div', class_='article-content')
    items = body.find_all('p')

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
    url = 'https://www.wsj.com/articles/goldman-sachs-lifts-the-veil-to-woo-skeptical-shareholders-11578394803'

    result = requests.get(url, headers=make_headers(source='wsj'))
    soup = BeautifulSoup(result.content)

    crawl_ticker_symbols(soup, url)
