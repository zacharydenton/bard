#!/usr/bin/env python

# Copyright 2010, Zach Denton <z@chdenton.com>
# Licensed under the terms of the GPLv3 or later

import random
from collections import defaultdict

import nltk

class SentenceBasedGenerator:
    """
    This generator generates text using a model of the input tokens' sentence structure.

    Basically it creates an index of the sentence structures in the tokens using their part-of-speech tags. It then maintains a separate index of all the part-of-speech tags in the text and the words that have those tags. Finally it picks a sentence from the sentence index and replaces the part-of-speech tags in the sentence with a random word which has that tag.
    """
    def __init__(self, tokens):
        '''
        Initialize the generator. tokens must be a list of pos-tagged sentences.
        '''
        self.tokens = tokens

        self._sentence_index = self._generate_sentence_index(self.tokens)
        self._tag_index = self._generate_tag_index(self.tokens)

    def _generate_sentence_index(self, tokens):
        '''
        Creates an index of sentence structures.

        Takes a list of lists of tagged tokens and returns a list of lists of tags.
        '''
        index = []
        for sentence in tokens:
            model = tuple(token[1] for token in sentence)
            index.append(model)
        return index

    def _generate_tag_index(self, tokens):
        '''
        Creates an index of part-of-speech tagged words.
        '''
        index = defaultdict(list)
        for sentence in tokens:
            for token in sentence:
                word = token[0]
                tag = token[1]
                index[tag].append(word)
        return index

    def generate(self, length=100):
        results = []
        while len(results) < length:
            sentence = self.get_sentence()
            for tag in sentence:
                results.append(self.get_word(tag))
        return results
        
    def get_word(self, tag):
        return random.choice(self._tag_index[tag])

    def get_sentence(self):
        return random.choice(self._sentence_index)

    def istagged(self):
        return isinstance(self.tokens[0][0], tuple)

    def issents(self):
        return isinstance(self.tokens[0], list)
