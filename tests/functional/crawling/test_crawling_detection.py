from tests import FortuneTestCase

from src.crawling.seekingalpha.parsing import parse_article as parse_seeking_alpha_article
from src.crawling.motleyfool.parsing import parse_article as parse_motleyfool_article


class TestCrawlingDetectionHealth(FortuneTestCase):

    def test_seekingalpha(self):
        source = 'seenkingalpha'
        url = 'https://seekingalpha.com/article/4294051-week-review-henlius-licenses-southeast-asia-rights-pdminus-1-candidate-692-million-deal'
        title = 'Week In Review: Henlius Out-Licenses Southeast Asia Rights For PD-1 Candidate In $692 Million Deal'
        self.assertSourceHealth(source, title, parse_seeking_alpha_article, url)

    def test_motleyfool(self):
        source = 'motleyfool'
        url = 'https://www.fool.com/investing/2019/10/08/why-sailpoint-technologies-stock-dropped-17-in-sep.aspx'
        title = 'Why Sailpoint Technologies Stock Dropped 17% in September'
        self.assertSourceHealth(source, title, parse_motleyfool_article, url)
