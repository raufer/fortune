import requests
import logging

from typing import Dict
from datetime import datetime
from bs4 import BeautifulSoup
from functools import reduce

from src.crawling.http import make_headers
from src.ops.text.tokenize import tokenize_sentences

base = 'https://www.bloomberg.com/markets'


logger = logging.getLogger(__name__)


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
    title = article_tag.find('h1',class_='lede-text-v2__hed').get_text().strip()

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


def _crawl_summary(soup):
    logger.debug(f"Extracting summary")
    section = soup.find('section', class_='usmf-new article-header')
    summary = section.find('h2').get_text().strip()
    logger.debug(f"Summary: '{summary}'")
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
        ['[[Paragraph]]{}'.format(group[0].get_text())] +
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

    article = ["[[Article]]{}.".format(title)] + [summary] + body
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

    result = requests.get(url, headers=make_headers())
    soup = BeautifulSoup(result.content)

    article = crawl_title(soup)
