import unittest
import nltk

from bard.generators import sentence

class TestSentenceBased(unittest.TestCase):
    def setUp(self):
        self.sents = nltk.corpus.brown.tagged_sents(categories='science_fiction')
        self.generator = sentence.SentenceBasedGenerator(self.sents)

    def test_generator(self):
        random_tokens = self.generator.generate(length=100)
        self.assertTrue(isinstance(random_tokens[0], str))


