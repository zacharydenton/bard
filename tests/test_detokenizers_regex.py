import unittest
import nltk

from bard.detokenizers import regex;

class TestDetokenizer(unittest.TestCase):
    def setUp(self):
        self.correct_response = """``What... is the airspeed velocity of an unladen swallow?''

``African or European?''

``I don't know that!''"""
        self.tokens = nltk.wordpunct_tokenize(self.correct_response)
        self.tagged_tokens = nltk.pos_tag(self.tokens)
    
    def test_regex(self):
        detokenizer = regex.RegexDetokenizer()
        print self.tokens
        result = detokenizer.detokenize(self.tokens)
        print result
        self.assertEqual(result, self.correct_response)
        print self.correct_response

    def test_regex_tagged(self):
        detokenizer = regex.RegexDetokenizer()
        tagged_result = detokenizer.detokenize(self.tagged_tokens)
        self.assertEqual(tagged_result, self.correct_response)

    def test_sanity(self):
        detokenizer = regex.RegexDetokenizer()
        tagged_result = detokenizer.detokenize(self.tagged_tokens)
        tokenized = nltk.wordpunct_tokenize(tagged_result)
        self.assertEqual(tokenized, self.tokens)

    def test_various(self):
        known_values = (
            (['single-handedly', '``', 'creeping', 'socialism', "''"], "single-handedly ``creeping socialism''"),
        )
        detokenizer = regex.RegexDetokenizer()
        for tokens, correct_response in known_values:
            result = detokenizer.detokenize(tokens)
            self.assertEqual(result, correct_response)
            

class TestToken(unittest.TestCase):
    def test_contraction(self):
        known_values = (
            ("n't", True),
            ("I'm", False),
            ("'re", True),
            ("hasn't", False),
            ("B'dikkat", False),
            ("'", True)
        )
        for test, value in known_values:
            guess = regex.Token(test).iscontraction()
            self.assertEqual(guess, value)

    def test_punct(self):
        known_values = (
            (".", True),
            ("?''", True),
            ("''?", True),
            ("half-man", False)
        )
        for test, value in known_values:
            self.assertEqual(regex.Token(test).ispunct(), value)

    def test_starts_quotation(self):
        known_values = (
            ("''", False),
            ("``", True),
            ("``That's", True),
            ("''?", False),
            ("?''", False)
        )
        for test, value in known_values:
            self.assertEqual(regex.Token(test).starts_quotation(), value)

    def test_ends_quotation(self):
        known_values = (
            ("''", True),
            ("``", False),
            ("``That's", False),
            ("''?", True),
            ("?''", True)
        )
        for test, value in known_values:
            self.assertEqual(regex.Token(test).ends_quotation(), value)

    def test_ends_sentence(self):
        known_values = (
            ("''?", True),
            ("?''", True)
        )
        for test, value in known_values:
            self.assertEqual(regex.Token(test).ends_sentence(), value)


