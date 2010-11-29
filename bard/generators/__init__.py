#!/usr/bin/env python
import markov
import nltk

__all__ = ["markov", "generate", "sentence"]

def generate(corpus=None, length=100):
    '''use the best text generator to generate some pseudorandom text'''
    if corpus is None:
        corpus = nltk.corpus.brown.tagged_words(categories='science_fiction')
    generator = markov.IntelligentMarkovGenerator(corpus)
    return generator.generate(length=length)
