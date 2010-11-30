import unittest
import nltk

from bard.generators import *

class TestGenerators(unittest.TestCase):
    def test_generator(self):
        random_tokens = generate(length=100)
        self.assertTrue(isinstance(random_tokens[0], tuple))

