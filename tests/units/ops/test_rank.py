import unittest
import numpy as np

from src.ops.rank import most_frequent


class TestRankOps(unittest.TestCase):

    def test_most_frequent(self):
        x = []
        expected = []
        result = most_frequent(x, n=3)
        self.assertListEqual(result, expected)

        x = [1, 1, 2, 3, 4, 1, 2, 2, 1, 1, 2, 3, 5, 6, 7, 8, 9]
        expected = [1, 2, 3]
        result = most_frequent(x, n=3)
        self.assertListEqual(result, expected)

        x = [1, 2, 3]
        expected = [1, 2, 3]
        result = most_frequent(x, n=3)
        self.assertListEqual(result, expected)

        x = [1, 2, 3]
        expected = [1, 2, 3]
        result = most_frequent(x, n=5)
        self.assertListEqual(result, expected)

        x = [1, 2, 3]
        expected = [1, 2]
        result = most_frequent(x, n=2)
        self.assertListEqual(result, expected)

        x = [1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8, 8, 8, 8, 8, 8, 9]
        expected = [8, 4]
        result = most_frequent(x, n=2)
        self.assertListEqual(result, expected)

        x = [1, 1, 2, 3, 4, 4, 4, 4, 4, 5, 6, 7, 8, 8, 8, 9]
        expected = [4, 8]
        result = most_frequent(x, n=2)
        self.assertListEqual(result, expected)
