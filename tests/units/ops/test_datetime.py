import unittest

from src.ops.datetime import safe_datetime_to_iso


class TestDatetimeOps(unittest.TestCase):

    def test_safe_datetime_to_iso(self):

        input_formats = [
            '%b. %d, %Y %I:%M %p',
            '%B %d, %Y %I:%M %p'
        ]

        d = 'Jan. 2, 2020 7:46 am'
        timestamp = safe_datetime_to_iso(d, input_formats[0])
        expected = '2020-01-02T07:46:00'
        self.assertEqual(timestamp, expected)

        d = 'Jan. 2, 2020 7:46 am'
        timestamp = safe_datetime_to_iso(d, input_formats[1])
        expected = None
        self.assertEqual(timestamp, expected)

        d = 'Jan. 2, 2020 7:46 am'
        timestamp = safe_datetime_to_iso(d, input_formats)
        expected = '2020-01-02T07:46:00'
        self.assertEqual(timestamp, expected)
