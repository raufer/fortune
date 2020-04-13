import os
import time
import json
import logging

from typing import Dict
from selenium.webdriver.chrome.webdriver import WebDriver

logger = logging.getLogger(__name__)


def get(driver: WebDriver, url: str, headers: Dict = None, wait_for: int = None) -> str:
    """
    Uses the `webdriver` to get an `url`.
    Optionally waits `wait_for` seconds before
    fetching the url and returning it
    """
    logger.debug(f"GET '{url}'")

    if headers is not None:
        logger.info(f"Using custom headers")
        logger.debug(json.dumps(headers, indent=4))

        remove = ['accept-encoding']
        logger.debug(f"Removing '{remove}' from custom headers")
        for entry in remove:
            headers.pop(entry, None)

        driver.header_overrides = headers

    driver.get(url)

    if wait_for is not None:
        logger.debug(f"Sleeping for '{wait_for}' seconds waiting for dyanmic content rendering")
        time.sleep(wait_for)

    html = driver.find_element_by_tag_name('html').get_attribute('innerHTML')

    return html


if __name__ == '__main__':

    from src.webdriver import init_chrome_driver
    from src.crawling.http import make_headers

    driver = init_chrome_driver()

    url = 'https://www.wsj.com/articles/goldman-sachs-lifts-the-veil-to-woo-skeptical-shareholders-11578394803'
    url = 'https://www.bloomberg.com/news/articles/2019-12-05/boeing-tries-to-win-over-pilots-attendants-with-737-max-pitch'
    url = 'https://seekingalpha.com/article/4337293-tale-of-2-stocks-luckin-coffee-and-iqiyi'
    url = 'https://www.fool.com/investing/2019/10/08/why-sailpoint-technologies-stock-dropped-17-in-sep.aspx'

    html = get(driver, url,  make_headers(source='fool'))
    # html = get(driver, url)
    print(html)

