import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from functools import reduce
from typing import List, Tuple
from src.crawling.http import headers
from src.ops.text.tokenize import tokenize_sentences
from selenium import webdriver

base = 'https://www.fool.com'


def crawl_motleyfool_author(soup):
    author_tag = soup.find('section', class_='author-card')
    author_url = author_tag.find('div', class_='author-username').find('a')['href']
    author_name = author_tag.find('div', class_='author-username').find('a').get_text().strip()

    url = 'https://www.fool.com/investing/2019/10/08/why-sailpoint-technologies-stock-dropped-17-in-sep.aspx'
    browser = webdriver.PhantomJS()
    browser.get(url)
    soup = BeautifulSoup(browser.page_source)

    iframe_src = soup.select_one("#twitter-widget-0").attrs["src"]

    twitter = soup.find('a', class_="twitter-follow-button")

    if twitter:
        soup_twitter = BeautifulSoup(requests.get(twitter['href'], headers=headers).content)
        followers = soup_twitter.find('span', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')

    result = {
        'name': author_name,
        'url': author_url,
        'followers': followers,
        # 'articles': articles
        }

    return result


def crawl_title(soup):
    section = soup.find('section', class_='usmf-new article-header')
    title = section.find('h1').get_text()
    return title


def _crawl_summary(soup):
    section = soup.find('section', class_='usmf-new article-header')
    summary = section.find('h2').get_text()
    return summary


def _crawl_body(soup):
    section = soup.find('section', class_='usmf-new article-body')
    body = section.find('span', class_='article-content')
    items = body.find_all(recursive=False)

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

    paragraphs = [
        ['[[Paragraph]]{}'.format(group[0].get_text())] +
        ([] if not group[1:] else tokenize_sentences(group[1].get_text()))
        for group in grouped if group
    ]

    paragraphs = sum(paragraphs, [])

    return paragraphs


def crawl_motleyfool_article(x):
    """
    """
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


if __name__ == '__main__':
    url = 'https://www.fool.com/investing/2019/10/08/why-sailpoint-technologies-stock-dropped-17-in-sep.aspx'
    result = requests.get(url)
    soup = BeautifulSoup(result.content)

    article = crawl_motleyfool_article(soup)
    print(article)
