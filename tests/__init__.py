import unittest


class FortuneTestCase(unittest.TestCase):

    def assertSourceHealth(self, sourcename, title, f_parse, *args):
        msg = f'{sourcename} down'
        try:
            article = f_parse(*args)
        except Exception as e:
            raise AssertionError(msg)
        self.assertEqual(article['title'], title, msg)


