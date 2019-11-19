import unittest

from src.crawling.seekingalpha.parsing import parse_seekingalpha_article


class TestCrawlingDetectionHealth(unittest.TestCase):

    def test_seeking_alpha(self):
        url = 'https://seekingalpha.com/article/4294051-week-review-henlius-licenses-southeast-asia-rights-pdminus-1-candidate-692-million-deal'
        msg = 'seekingalpha down'
        try:
            article = parse_seekingalpha_article(url)
        except Exception as e:
            raise AssertionError(msg)
        self.assertEqual(article['title'], 'Week In Review: Henlius Out-Licenses Southeast Asia Rights For PD-1 Candidate In $692 Million Deal', msg)
