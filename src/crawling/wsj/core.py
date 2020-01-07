import requests
import logging

from typing import Dict
from typing import List
from datetime import datetime
from bs4 import BeautifulSoup
from functools import reduce

from src.crawling.http import make_headers
from src.ops.text.tokenize import tokenize_sentences

base = 'https://www.wsj.com/news/business'


logger = logging.getLogger(__name__)


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

    input_format = '%b. %d, %Y %I:%M %p'
    timestamp = datetime.strptime(timestamp_txt, input_format).isoformat()

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
    url = 'https://www.wsj.com/articles/vanguards-asia-head-leaves-investing-giant-after-leading-china-push-11577969213'

    result = requests.get(url, headers=make_headers(source='wsj'))
    soup = BeautifulSoup(result.content)

    _crawl_summary(soup)
