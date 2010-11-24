#!/usr/bin/env python
import re

class RegexDetokenizer:
    def detokenize(self, tokens):
        '''
        A regex-based detokenizer.
    
        Pass a list of tokens, and you will receive a string formatted
        like a novel. Dialogue is placed on its own line.
    
        '''
        #print >> sys.stderr, "detokenizing tokens..."

        # check if the tokens are tagged; if they are, untag them.
        if isinstance(tokens[0], tuple):
            tokens = [token[0] for token in tokens]
    
        output = ''
        for i, token in enumerate(tokens):
            # next token; previous token
            try:
                next_token = tokens[i+1]
            except IndexError:
                next_token = ''
            if i != 0:
                prev_token = tokens[i-1]
            else:
                prev_token = ''
    
            # skip double punctuation.
            if token == next_token and token in "!.?;":
                continue
    
            # add the token to the output.
            output += token
    
            # add spacing.
            if next_token in '...!?.,\'\')";:' or token in '(``':
                # punctuation does not require spacing
                output += ''
            elif re.search("\'\w+", next_token):
                # don't put space in the middle of contractions
                output += ''
            elif ((token in "!?." and prev_token == "''") or 
                  (token in "!?." and next_token == "``") or
                  (token in "''" and prev_token in "!?.")):
                # this is dialogue, put it on its own line
                output += '\n\n'
            else:
                # normal text; just add a space
                output += ' '
    
        return output
     
