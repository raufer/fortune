import unittest

from src.ops.text.tokenize import tokenize_sentences


class TestTextTokenize(unittest.TestCase):

    def test_tokenize_sentences(self):
        text = ''
        result = tokenize_sentences(text)
        self.assertListEqual([text], result)

        text = 'Just a single sentence.'
        result = tokenize_sentences(text)
        self.assertListEqual([text], result)

        text = 'Everyday I leave the house between 8 a.m and 9 a.m. for work. Really early! Going for work.'

        expected = [
            'Everyday I leave the house between 8 a.m and 9 a.m. for work.',
            'Really early!',
            'Going for work.'
        ]

        result = tokenize_sentences(text)
        self.assertListEqual(result, expected)

