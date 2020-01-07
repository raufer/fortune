import logging
import time

from selenium import webdriver
from selenium.webdriver.phantomjs.webdriver import WebDriver

logger = logging.getLogger(__name__)


def init_phantomjs_driver(*args, headers=None, **kwargs) -> WebDriver:
    """
    Initialize a headless PhantomJS webdriver
    with custom headers support
    """
    if not headers:
        headers = {}

    logger.debug('Initializing a phantom JS webdriver')
    if not headers:
        logger.debug('Using default headers. No custom setup.')
    else:
        logger.debug(f"Using custom headers '{[(k, v) for k, v in list(headers.items())[:1]]}'")

    for key, value in headers.items():
        webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value

    if 'user-agent' in headers:
        webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = headers['user-agent']

    driver = webdriver.PhantomJS(*args, **kwargs)
    driver.set_window_size(1400, 1000)

    return driver


def get(webdriver: WebDriver, url: str, wait_for: int = None) -> str:
    """
    Uses the `webdriver` to get an `url`.
    Optionally waits `wait_for` seconds before
    fetching the url and returning it
    """
    logger.debug(f"Using webdriver to GET '{url}'")
    webdriver.get(url)

    if wait_for is not None:
        logger.debug(f"Sleeping for '{wait_for}' seconds waiting for dyanmic content rendering")
        time.sleep(wait_for)

    html = webdriver.find_element_by_tag_name('html').get_attribute('innerHTML')
    return html
