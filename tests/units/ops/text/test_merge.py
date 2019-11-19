import unittest

from src.ops.text.merge import merge_sentences
from src.ops.text.merge import merge_sentences_min_len


class TestTextMerge(unittest.TestCase):

    def test_merge_sentence_min_len(self):
        text = []
        result = merge_sentences_min_len(text, min_len=3)
        self.assertListEqual(text, result)

        text = ['A']
        result = merge_sentences_min_len(text, min_len=3)
        self.assertListEqual(text, result)

        text = [
            'ABCD',
            'ABC',
            'A',
            'B',
            'ABCD',
            'ABC',
            'AA',
            'ABCDE'
        ]

        expected = [
            'ABCD',
            'ABC',
            'A. B. ABCD',
            'ABC',
            'AA. ABCDE'
        ]

        result = merge_sentences_min_len(text, min_len=3)
        self.assertListEqual(result, expected)

    def test_merge_sentence(self):
        text = []
        result = merge_sentences(text, min_len=3)
        self.assertListEqual(text, result)

        text = [
            'First sentence.',
            'Sentence number two.',
            'Third sentence'
        ]
        expected = [
            'First sentence. Sentence number two.',
            'Third sentence'
        ]

        result = merge_sentences(text, min_len=5)
        self.assertListEqual(result, expected)

        text = [
            'Consider these items:',
            'first item with the higher price',
            'second item with the second higher price.',
            'End of the block',
            'Final notes'
        ]
        expected = [
            'Consider these items: first item with the higher price',
            'second item with the second higher price.',
            'End of the block. Final notes'
        ]

        result = merge_sentences(text, min_len=5)
        self.assertListEqual(result, expected)

