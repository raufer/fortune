import unittest

from src.ops.text.preprocessig import clean_text


class TestPreprocessing(unittest.TestCase):

    def test_clean_text(self):

        text = []
        expected = []
        result = clean_text(text, [r'Part \d'])
        self.assertListEqual(result, expected)

        text = [
            'This is a sentence',
            'Part 1.',
            'Part 1. ',
            'This is sentence 1 of part 2.',
            'The text has 4 sentences'
        ]
        expected = [
            'This is a sentence',
            'Part 1. ',
            'This is sentence 1 of part 2.',
            'The text s'
        ]
        result = clean_text(text, [r'Part \d\.$', r'has \d sentence'])
        self.assertListEqual(result, expected)
