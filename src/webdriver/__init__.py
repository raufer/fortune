import os
import json
import logging

from seleniumwire import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

logger = logging.getLogger(__name__)


def init_chrome_driver(driver_path=None) -> WebDriver:
    """
    Initialize a Chrome webdriver
    with custom headers support

    Assumes Chrome Driver path executable is set by
    env :: CHROME_DRIVER_PATH, defaults to /usr/local/bin
    """
    if driver_path is None:
        driver_path = os.environ.get('CHROME_DRIVER_PATH', '/usr/local/bin/chromedriver')

    logger.info(f"Chrome Driver path at '{driver_path}'")

    options = Options()
    options.add_argument("--headless")
    options.add_argument("--window-size=1920x1080")
    options.add_argument('--log-level 3')

    logger.debug(f"Chrome options: '{options}'")
    logger.debug(json.dumps(options.to_capabilities(), indent=4))

    driver = webdriver.Chrome(chrome_options=options, executable_path=driver_path)
    return driver




