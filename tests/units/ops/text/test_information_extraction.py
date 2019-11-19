import unittest

from src.ops.text.information_extraction import scan_inserts


class TestInformationExtraction(unittest.TestCase):

    def test_merge_sentence_min_len(self):
        input = [
            "Paragraph 1.",
            "after paragraph (i) insert\u2014",
            "\u201c(j)has satisfactory equipment;",
            "(k)has satisfactory equipment installed."
        ]

        input = [i.encode('utf-8').decode('utf-8') for i in input]

        expected = [
            "after paragraph (i) insert\u2014",
            "\u201c(j)has satisfactory equipment;",
            "(k)has satisfactory equipment installed."
        ]

        result = scan_inserts(input)

        self.assertListEqual(result, expected)

