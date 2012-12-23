#!/usr/bin/env python

# Copyright 2010, Zach Denton <z@chdenton.com>
# Licensed under the terms of the GPLv3 or later

import markov
import sentence
import nltk

__all__ = ["markov", "generate", "sentence"]

def generate(corpus=None, length=100, generator_type=None):
    '''use the best text generator to generate some pseudorandom text'''
    if generator_type is None or generator_type == "markov":
        if corpus is None:
           corpus = nltk.corpus.brown.tagged_words(categories='science_fiction')
        generator = markov.IntelligentMarkovGenerator(corpus)
    elif generator_type == "sentence":
        if corpus is None:
           corpus = nltk.corpus.brown.tagged_sents(categories='science_fiction')
        generator = sentence.SentenceBasedGenerator(corpus)
    return generator.generate(length=length)
