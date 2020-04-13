import sys
import logging

PROJECT_ID = 'weighty-purpose-273914'


logging.basicConfig(
    format='%(asctime)s, %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG
)

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)