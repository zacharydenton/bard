"""
A module to generate pseudorandom text.

It utilizes Markov chains to produce new text based on
some input text. You could use it, for example, to write a
ten million word science fiction epic using the science
fiction category of the Brown corpus (yes, I have done it).

This module requires NLTK.
"""
import nltk

# metadata
__author__ = 'Zach Denton'
__version__ = '0.2'

# packages
import detokenizers; from detokenizers import *
import generators; from generators import *

def generate_text(corpus=None, length=100):
    if corpus is None:
        corpus = nltk.corpus.brown.tagged_words(categories='fiction')
    tokens = generate(corpus, length=length)
    return detokenize(tokens)
