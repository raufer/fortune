import requests
from bs4 import BeautifulSoup

from src.crawling.http import make_headers
from src.crawling.motleyfool.core import crawl_motleyfool_article, crawl_title
from src.crawling.motleyfool.core import crawl_motleyfool_author
from graphify.parsing import parse_iterable


def parse_motelyfool_article(url):

    result = requests.get(url, headers=make_headers())
    soup = BeautifulSoup(result.content)

    hierarchy = ['Article', 'Paragraph']

    descriptor = {
        'components': hierarchy,
        'patterns': hierarchy
    }

    text = crawl_motleyfool_article(soup)

    doc = parse_iterable(text, descriptor)
    doc = doc.to_dict()

    doc['url'] = url
    doc['title'] = crawl_title(soup)
    doc['author'] = crawl_motleyfool_author(soup)
    doc['timestamp'] = crawl_motleyfool_timestamp(soup)
    # TODO: meta, e.g likes and comments are still with problems
    doc['meta'] = crawl_motleyfool_metadata(soup)

    return doc


if __name__ == '__main__':
    from pprint import pprint

    url = 'https://www.fool.com/investing/2019/10/08/why-sailpoint-technologies-stock-dropped-17-in-sep.aspx'

    article = parse_motelyfool_article(url)

    pprint(article)

