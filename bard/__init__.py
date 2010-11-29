"""
A module which generates pseudorandom text.

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

def generate_text(length=100):
    tokens = generate(corpus=None, length=length)
    return detokenize(tokens)
