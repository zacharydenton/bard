#!/usr/bin/env python
'''
The base detokenizer classes, from which real detokenizers should inherit.
'''
class Detokenizer:
    def detokenize(self, tokens):
        raise NotImplementedError("This class is not meant to be used directly. Use a subclass instead.")
