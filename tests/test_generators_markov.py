import unittest
import nltk

from bard.generators import markov

class TestMarkov(unittest.TestCase):
    def setUp(self):
        self.tokens = nltk.corpus.brown.words(categories='science_fiction')
        self.tagged_tokens = nltk.corpus.brown.tagged_words(categories='science_fiction')
        self.generator = markov.MarkovGenerator(self.tokens)
        self.tagged_generator = markov.MarkovGenerator(self.tagged_tokens)

    def test_generator(self):
        random_tokens = self.generator.generate(length=100)
        self.assertTrue(isinstance(random_tokens[0], str))

    def test_tagged_generator(self):
        random_tokens = self.tagged_generator.generate(length=100)
        self.assertTrue(isinstance(random_tokens[0], tuple))

class TestIntelligentMarkov(TestMarkov):
    def setUp(self):
        self.tokens = nltk.corpus.brown.words(categories='science_fiction')
        self.tagged_tokens = nltk.corpus.brown.tagged_words(categories='science_fiction')
        self.generator = markov.IntelligentMarkovGenerator(self.tokens)
        self.tagged_generator = markov.IntelligentMarkovGenerator(self.tagged_tokens)

class TestGeneratorFunctions(unittest.TestCase):
    def setUp(self):
        self.tokens = nltk.corpus.brown.words(categories='science_fiction')
        self.tagged_tokens = nltk.corpus.brown.tagged_words(categories='science_fiction')
        self.generator = markov.MarkovGenerator(self.tokens)
        self.tagged_generator = markov.MarkovGenerator(self.tagged_tokens)


