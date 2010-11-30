import unittest
import nltk

from bard.detokenizers import *

class TestDetokenizer(unittest.TestCase):
    def setUp(self):
        self.tokens = [
            '``', 'What', '...', 'is', 'the', 'airspeed', 'velocity', 
            'of', 'an', 'unladen', 'swallow', '?', "''", '``', 'African',
            'or', 'European', '?', "''", '``', 'I', 'do', "n't", "know",
            "that", '!', "''"]
        self.tagged_tokens = nltk.pos_tag(self.tokens)
        self.correct_response = """``What... is the airspeed velocity of an unladen swallow?''

``African or European?''

``I don't know that!''"""
    
    def test_regex(self):
        detokenizer = regex.RegexDetokenizer()
        result = detokenizer.detokenize(self.tokens)
        self.assertEqual(result, self.correct_response)

    def test_regex_tagged(self):
        detokenizer = regex.RegexDetokenizer()
        tagged_result = detokenizer.detokenize(self.tagged_tokens)
        self.assertEqual(tagged_result, self.correct_response)

    def test_default(self):
        self.assertEqual(detokenize(self.tokens), self.correct_response)

    def test_default_tagged(self):
        self.assertEqual(detokenize(self.tagged_tokens), self.correct_response)



