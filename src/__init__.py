import sys
import logging

sys.path.append('/Users/rauferreira/waymark/graphify')
sys.path.append('/Users/rauferreira/waymark/linkify')

logging.getLogger("requests").setLevel(logging.WARNING)
logging.getLogger("urllib3").setLevel(logging.WARNING)