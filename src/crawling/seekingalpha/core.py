import requests
import logging

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from functools import reduce

from typing import List, Tuple

from src.crawling.http import make_headers

base = 'https://seekingalpha.com'


logger = logging.getLogger(__name__)


def list_articles(url: str) -> List[Tuple[str, str]]:
    """
    Returns a list of the first page articles
    [(name, url)]
    """
    logger.info(f"Listing articles")

    result = requests.get(url)
    soup = BeautifulSoup(result.content)

    main = soup.find('ul', class_='articles-list')
    articles = main.find_all('li')

    articles = [art.find('div', class_='media-body').find('a') for art in articles]
    articles = [(art.get_text(), urljoin(base, art['href'])) for art in articles]

    logger.debug(f"Found articles:")
    for article in articles:
        logger.debug(article)

    return articles


def _crawl_summary(soup):
    logger.debug(f"Extracting summary")

    summary_html = soup.find('div', class_='article-summary')

    if summary_html:
        paragraphs = summary_html.find('div', class_='a-sum').find_all('p')
        paragraphs = [["[[Paragraph]]Paragraph {}.".format(i)] + [p.get_text()] for i, p in enumerate(paragraphs)]
        text = ["[[Section]]Summary."] + sum(paragraphs, [])
    else:
        text = []

    logger.debug(f"Summary: '{text}'")
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


def crawl_author(soup):
    logger.debug(f"Extracting author information")

    author_tag = soup.find('div',class_='media hidden-print').find('div',class_='info').find('div',class_='top')

    author_url = author_tag.find('a')['href']
    logger.debug(f"Author URL: '{author_url}'")

    author_name = author_tag.find('span',class_='name').get_text()
    logger.debug(f"Author Name: '{author_name}'")

    logger.debug(f"Getting author specific page '{author_url}'")
    soup = BeautifulSoup(requests.get(author_url, headers=make_headers()).content)

    followers = soup.find('li',class_='followers').find('i',class_='profile-top-nav-count').get_text()
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
    result = requests.get(url)
    soup = BeautifulSoup(result.content)

    author = crawl_author(soup)
    print(author)








