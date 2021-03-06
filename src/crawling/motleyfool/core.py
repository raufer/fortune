import requests
import logging

from typing import Dict
from typing import List
from typing import Tuple

from datetime import datetime
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from functools import reduce

from src.crawling.http import make_headers
from src.ops.text.tokenize import tokenize_sentences

base = 'https://www.fool.com'

logger = logging.getLogger(__name__)


def crawl_ticker_symbols(soup) -> List[Tuple[str, str]]:
    """
    Extracts all of the ticker symbols that are involved
    Returns a list of strings [(exchange, symbol)]
    """
    logger.info(f"Extracting ticker symbols in article scope")

    section = soup.find('div', class_='main-col')
    stocks = section.find_all('span', class_='ticker', recursive=True)
    logger.debug(f"'{len(stocks)}' stocks")

    symbols = [section.find('a').get_text().strip().split(":") for section in stocks]
    symbols = [(s[0], s[1]) for s in symbols]

    logger.info(f"Symbols found: '{[(s[0] + str('::') + s[1]) for s in symbols]}'")

    return symbols


def crawl_author(soup):
    logger.debug(f"Extracting author information")
    author_tag = soup.find('div', class_='author-tagline-top')

    author_url = author_tag.find('div', class_='author-name').find('a')['href']
    logger.debug(f"Author URL: '{author_url}'")

    author_name = author_tag.find('div', class_='author-name').find('a').get_text().strip()
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

    section = soup.find('section', class_='usmf-new article-header')
    title = section.find('h1').get_text()

    logger.info(f"Article title '{title}'")
    return title


def crawl_timestamp(soup) -> str:
    """
    Return timestamp in ISO 8601 UTC format
    https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    """
    logger.debug(f"Extracting timestamp")

    date = soup.find('div', class_='publication-date')

    if date:
        input_format = '%b %d, %Y at %I:%M%p'
        timestamp = date.get_text().strip()
        timestamp = datetime.strptime(timestamp, input_format).isoformat()
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
    section = soup.find('section', class_='usmf-new article-header')
    summary = section.find('h2').get_text().strip()
    logger.debug(f"Summary: '{summary}'")
    summary = ["[[Article]]Summary."] + ["[[Paragraph]]Paragraph 0."] + [summary]
    logger.debug(f"Summary w/ structure: '{summary}'")
    return summary


def _crawl_body(soup):
    logger.debug(f"Extracting body")

    section = soup.find('section', class_='usmf-new article-body')
    body = section.find('span', class_='article-content')

    items = body.find_all(recursive=False)
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
    url = 'https://www.fool.com/investing/2019/10/08/why-sailpoint-technologies-stock-dropped-17-in-sep.aspx'

    result = requests.get(url, headers=make_headers(source='fool'))
    soup = BeautifulSoup(result.content)

    crawl_ticker_symbols(soup)
