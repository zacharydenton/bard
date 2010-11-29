#!/usr/bin/env python
import markov
import nltk

__all__ = ["markov", "generate"]

def generate(corpus=None, w1=None, w2=None, length=100):
    '''use the best text generator to generate some pseudorandom text'''
    if corpus is None:
        corpus = nltk.corpus.brown.tagged_words(categories='fiction')
    generator = markov.IntelligentMarkovGenerator(corpus)
    return generator.generate(w1, w2, length)
