import requests
import logging
import time

from typing import Tuple
from typing import List
from functools import reduce

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium.webdriver.chrome.webdriver import WebDriver

from src.webdriver import api
from src.crawling.http import make_headers

base = 'https://seekingalpha.com'

logger = logging.getLogger(__name__)


def crawl_ticker_symbols(soup) -> List[Tuple[str, str]]:
    """
    Extracts all of the ticker symbols that are involved
    Returns a list of strings [(exchange, symbol)]
    """
    logger.info(f"Extracting ticker symbols in article scope")

    section = soup.find('span', id='about_stocks')
    stocks = section.find_all('a')
    logger.debug(f"'{len(stocks)}' stocks")

    urls = [urljoin(base, s['href']) for s in stocks]
    pages = [requests.get(url, headers=make_headers(source='seekingalpha')) for url in urls]
    sections = [BeautifulSoup(result.content).find('div', class_='symbol_title') for result in pages]

    symbols = [
        (section.find('meta', itemprop='exchange')['content'], section.find('meta', itemprop='tickerSymbol')['content'])
        for section in sections
    ]

    logger.info(f"Symbols found: '{[(s[0] + str('::') + s[1]) for s in symbols]}'")

    return symbols


def _crawl_summary(soup) -> List[str]:
    """
    Extracts a summary that that is able
    to provide a short description of the article
    """
    logger.debug(f"Extracting summary")

    summary_html = soup.find('div', class_='article-summary')

    if summary_html:
        paragraphs = summary_html.find('div', class_='a-sum').find_all('p')
        paragraphs = [["[[Paragraph]]Paragraph {}.".format(i)] + [p.get_text()] for i, p in enumerate(paragraphs)]
        text = ["[[Article]]Summary."] + sum(paragraphs, [])
    else:
        text = []

    logger.debug(f"Summary w/ structure: '{text}'")
    return text


def _crawl_body(soup):
    logger.debug(f"Extracting body")

    main = soup.find('div', class_='sa-art article-width')
    items = main.findChildren(recursive=False)
    logger.debug(f"Number of items: '{len(items)}'")

    def reducer(acc, x):
        if not acc:
            return [[x]]

        if x.name in ['h2', 'h3']:
            return acc + [[x]]

        else:
            acc[-1].append(x)
            return acc

    sections = reduce(reducer, items, [])
    logger.debug(f"Number of groups: '{len(sections)}'")

    sections = [
        ["[[Section]]{}.".format(s[0].get_text().strip())] +
        sum(
            [["[[Paragraph]]Paragraph {}.".format(i)] + [par.get_text()]
             for i, par in enumerate(s[1:]) if par.get_text().strip()], []
        )
        for s in sections
    ]
    sections = sum(sections, [])

    return sections


def crawl_title(soup):
    logger.debug(f"Extracting title")
    title = soup.find('div', class_='sa-art-hd').find('h1').get_text().strip()
    logger.info(f"Article title '{title}'")
    return title


def crawl_article(x):
    """
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


def crawl_author(driver: WebDriver, soup):
    logger.debug(f"Extracting author information")

    author_tag = soup.find('div', class_='media hidden-print').find('div', class_='info').find('div', class_='top')

    author_url = author_tag.find('a')['href']
    logger.debug(f"Author URL: '{author_url}'")

    author_name = author_tag.find('span', class_='name').get_text()
    logger.debug(f"Author Name: '{author_name}'")

    logger.debug(f"Getting author specific page '{author_url}'")

    html = api.get(driver, author_url, make_headers('seekingalpha'), wait_for=2)
    soup = BeautifulSoup(html)

    followers = soup.find('li', class_=['followers', 'followers tab ']).find('i').get_text()
    logger.debug(f"Number of followers '{followers}'")

    articles = soup.find('li', class_='articles').find('i', class_='profile-top-nav-count').get_text()
    logger.debug(f"Number of articles '{articles}'")

    result = {
        'name': author_name,
        'url': author_url,
        'followers': followers,
        'articles': articles
    }

    logger.debug(f"Author Information: '{result}'")
    return result


def crawl_timestamp(soup):
    """
    Return timestamp in ISO 8601 UTC format
    """
    logger.debug(f"Extracting timestamp")

    header = soup.find('div', class_='a-info clearfix')
    timestamp = header.find('time')['content']

    logger.info(f"Article timestamp '{timestamp}'")
    return timestamp


def crawl_metadata(soup):
    """
    Returns article metadata,
    e.g. number of likes, comments, etc
    """
    logger.debug(f"Crawling metadata")

    header = soup.find('div', class_='a-info clearfix')

    comments_tag = header.find('span', id='a-comments')
    if comments_tag:
        comments = comments_tag.find('a').get_text()
    else:
        comments = 0

    likes_tag = header.find('div', class_='likers show-likers inited')
    if likes_tag:
        likes = likes_tag['data-count']
    else:
        likes = 0

    metadata = {
        'comments': comments,
        'likes': likes
    }

    logger.debug(f"Article metadata: '{metadata}'")
    return metadata


if __name__ == '__main__':

    url = 'https://seekingalpha.com/article/4294051-week-review-henlius-licenses-southeast-asia-rights-pdminus-1-candidate-692-million-deal'

    result = requests.get(url, headers=make_headers(source='seekingalpha'))
    soup = BeautifulSoup(result.content)

    crawl_ticker_symbols(soup)
