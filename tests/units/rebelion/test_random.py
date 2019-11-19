import unittest

from src.rebelion import random


class TestRandom(unittest.TestCase):

    def test_random_user_agent(self):
        user_agent = random.user_agent()
        self.assertTrue('/' in user_agent)
        self.assertTrue('.' in user_agent)


