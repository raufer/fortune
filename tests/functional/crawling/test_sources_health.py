from tests import FortuneTestCase

from src.crawling.seekingalpha.parsing import parse_article as parse_seeking_alpha_article
from src.crawling.motleyfool.parsing import parse_article as parse_motleyfool_article
from src.crawling.bloomberg.parsing import parse_article as parse_bloomberg_article
from src.crawling.wsj.parsing import parse_article as parse_wsj_article


class TestSourcesHealth(FortuneTestCase):

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

    def test_wsj(self):
        source = 'wsj'
        url = 'https://www.wsj.com/articles/vanguards-asia-head-leaves-investing-giant-after-leading-china-push-11577969213'
        title = 'Vanguard’s Asia Head Leaves Investing Giant After Leading China Push'
        self.assertSourceHealth(source, title, parse_wsj_article, url)

    def test_bloomberg(self):
        source = 'bloomberg'
        url = 'https://www.bloomberg.com/news/articles/2019-12-05/boeing-tries-to-win-over-pilots-attendants-with-737-max-pitch'
        title = 'Boeing Tries to Win Over Pilots, Attendants with 737 Max Pitch'
        self.assertSourceHealth(source, title, parse_bloomberg_article, url)
