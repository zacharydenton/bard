#!/usr/bin/env python
import regex

__all__ = ["regex", "detokenize"]

def detokenize(tokens):
    '''
    detokenize tokens using the currently-recommended detokenizer 
    
        >>> tokens = ['``', 'What', '...', 'is', 'the', 'airspeed', 'velocity', 'of', 'an', 'unladen', 'swallow', '?', "''", '``', 'African', 'or', 'European', '?', "''", '``', 'I', 'do', "n't", "know", "that", '!', "''"]
        >>> sentence = detokenize(tokens)
        >>> print sentence
        ``What... is the airspeed velocity of an unladen swallow?''
        <BLANKLINE>
        ``African or European?''
        <BLANKLINE>
        ``I don't know that!''

    '''
    detokenizer = regex.RegexDetokenizer()
    return detokenizer.detokenize(tokens)
