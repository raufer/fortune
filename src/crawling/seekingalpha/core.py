import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from functools import reduce

from typing import List, Tuple

base = 'https://seekingalpha.com'


def list_articles(url: str) -> List[Tuple[str, str]]:
    """
    Returns a list of the first page articles
    [(name, url)]
    """
    result = requests.get(url)
    soup = BeautifulSoup(result.content)

    main = soup.find('ul', class_='articles-list')
    articles = main.find_all('li')

    articles = [art.find('div', class_='media-body').find('a') for art in articles]
    articles = [(art.get_text(), urljoin(base, art['href'])) for art in articles]

    return articles


def _crawl_summary(soup):
    summary_html = soup.find('div', class_='article-summary')

    if summary_html:
        paragraphs = summary_html.find('div', class_='a-sum').find_all('p')
        paragraphs = [["[[Paragraph]]Paragraph {}.".format(i)] + [p.get_text()] for i, p in enumerate(paragraphs)]
        text = ["[[Section]]Summary."] + sum(paragraphs, [])
    else:
        text = []

    return text


def _crawl_body(soup):
    main = soup.find('div', class_='sa-art article-width')
    items = main.findChildren(recursive=False)

    def reducer(acc, x):
        if not acc:
            return [[x]]

        if x.name in ['h2', 'h3']:
            return acc + [[x]]

        else:
            acc[-1].append(x)
            return acc

    sections = reduce(reducer, items, [])
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


def _crawl_title(soup):
    title = soup.find('div', class_='sa-art-hd').find('h1').get_text().strip()
    return title


def crawl_seekingalpha_article(x: str):
    """
    """
    if isinstance(x, str):
        result = requests.get(x)
        soup = BeautifulSoup(result.content)
    else:
        soup = x

    title = _crawl_title(soup)
    summary = _crawl_summary(soup)
    body = _crawl_body(soup)

    article = ["[[Article]]{}.".format(title)] + summary + body
    return article



