import unittest
import nltk

from bard.generators import sentence

class TestSentenceBased(TestMarkov):
    def setUp(self):
        self.tokens = nltk.corpus.brown.words(categories='science_fiction')
        self.tagged_tokens = nltk.corpus.brown.tagged_words(categories='science_fiction')
        self.generator = sentence.SentenceBasedGenerator(self.tokens)
        self.tagged_generator = sentence.SentenceBasedGenerator(self.tagged_tokens)

    def test_generator(self):
        random_tokens = self.generator.generate(length=100)
        self.assertTrue(isinstance(random_tokens[0], str))

    def test_tagged_generator(self):
        random_tokens = self.tagged_generator.generate(length=100)
        self.assertTrue(isinstance(random_tokens[0], tuple))


