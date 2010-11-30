#!/usr/bin/env python
import re

class Token(str):
    def iscontraction(self):
        '''
        returns True if the token is a contraction.

        Here contraction is taken to mean tokens like "n't", "'re", 
        or "'s". Tokens like "you're", "I'm", and "isn't" are considered
        words, not contractions.
        '''
        try:
            # check if there's an apostrophe
            if not "'" in self:
                return False

            # split the token into its constituent parts
            left,right = self.split("'")

            # check if there's a word preceding the apostrophe
            if len(left) > 1 or left.istitle():
                return False

            # it's passed all tests, so it must be a contraction.
            return True

        except:
            # assume it's not a contraction.
            return False

    def ispunct(self):
        if not re.search('[A-Za-z0-9]+', self):
            return True
        return False

    def starts_container(self):
        starters = ['[', '(']
        for starter in starters:
            if starter in self:
                return True
        return False

    def ends_container(self):
        enders = ["]", ')']
        for ender in enders:
            if ender in self:
                return True
        return False

    def starts_quotation(self):
        starters = ['``']
        for starter in starters:
            if starter in self:
                return True
        return False

    def ends_quotation(self):
        enders = ["''"]
        for ender in enders:
            if ender in self:
                return True
        return False

    def ends_sentence(self):
        enders = ['.', '!', '?']
        for ender in enders:
            if ender in self:
                return True
        return False

class RegexDetokenizer:
    def detokenize(self, tokens):
        '''
        A regex-based detokenizer.
    
        Pass a list of tokens, and you will receive a string formatted
        like a novel. Dialogue is placed on its own line.
    
        '''

        # check if the tokens are tagged; if they are, untag them.
        if isinstance(tokens[0], tuple):
            tokens = [token[0] for token in tokens]

        # turn the tokens into Tokens
        tokens = [Token(token) for token in tokens]
    
        output = ''
        for i, token in enumerate(tokens):
            # next token; previous token
            try:
                next_token = tokens[i+1]
            except IndexError:
                next_token = Token('')
            if i != 0:
                prev_token = tokens[i-1]
            else:
                prev_token = Token('')
    
            # skip double punctuation.
            if token == next_token and token in "!.?;":
                continue
    
            # add the token to the output.
            output += token
 
            # add spacing.
            if ((prev_token.ends_sentence() and token.ends_quotation()) or 
                (token.ends_sentence() and next_token.starts_quotation())):
                # this is dialogue, put it on its own line
                if len(next_token) != 0:
                    output += '\n\n'
            elif next_token.iscontraction():
                # don't put space in the middle of contractions
                output += ''
            elif next_token.islower() and len(next_token) == 1 and "'" in token:
                # don't put space before a lone lowercase character.
                output += ''
            elif next_token.starts_container():
                # put space before containers
                output += ' '
            elif next_token.ispunct() or token.starts_quotation() or token.starts_container():
                # punctuation does not require spacing
                output += ''
            else:
                # normal text; just add a space
                output += ' '
    
        return output
     
