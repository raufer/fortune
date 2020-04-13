import os
import time
import logging

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
        remove = ['accept-encoding']
        logger.debug(f"Removing '{remove}' from custom headers")
        for entry in remove:
            headers.pop(entry, None)

    for key, value in headers.items():
        webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = value

    if 'user-agent' in headers:
        webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.settings.userAgent'] = headers['user-agent']

    driver = webdriver.PhantomJS(*args, **kwargs)
    driver.set_window_size(1400, 1000)

    return driver


