#!/usr/bin/env python
# generate random text using trigrams and markov chains
# this uses part-of-speech tagged data from the Brown corpus
import random
import nltk
import cPickle as pickle

def detokenize(tokens):
    ''' humble attempt at converting a list of tokens into text '''
    output = ''
    for i, token in enumerate(tokens):
        output += token
        try:
            next_word = tokens[i+1]
        except IndexError:
            next_word = ''

        if next_word in '.!?,\'\'"' or token == '``':
            output += ''
        else:
            output += ' '

    return output
 

class Markov:
    def __init__(self, tokens, use_cache=False):
        self.tokens = tokens
        self.trigrams = nltk.util.trigrams(self.tokens)
        self.cache = self.generate_cache(self.trigrams, use_cache)
        self.tagged = self.istagged()

    def generate_cache(self, trigrams, use_cache):
        # generate a dict 
        # where keys are (v1, v2) and value is list of 
        # possible v3's 
        try:
            if use_cache:
                print "loading markov cache..."
                cachefile = open('.markov_cache', 'rb')
                cache = pickle.load(cachefile)
                cachefile.close()
            else:
                raise Exception('Not using cache...')
        except:
            print "generating trigrams cache..."
            cache = {}
            for w1, w2, w3 in trigrams:
                key = (w1, w2)
                if key in cache:
                    cache[key].append(w3)
                else:
                    cache[key] = [w3]
            if use_cache:
                cachefile = open('.markov_cache', 'wb')
                pickle.dump(cache, cachefile, -1)
                cachefile.close()
        return cache
        
    def markov_text(self, w1=None, w2=None, length=100):
        if w1 is None and w2 is None:
            w1, w2 = self.get_starter()

        results = []
        search_for = None
        finished = False
        previous = None
        while not finished:
            if self.tagged:
                current_tag = w1[1]
                results.append(w1[0])
                if len(results) >= length and not search_for and '.' in w1[0]:
                    finished = True
            else:
                current_tag = w1
                results.append(w1)
                if len(results) >= length and not search_for and '.' in w1:
                    finished = True

            if current_tag == '(':
                search_for = ')'
            elif current_tag == "``":
                search_for = "''"

            if search_for:
                search_results = self.search_for(w1, w2, search_for)
                if search_results:
                    w1, w2 = w2, random.choice(search_results)
                    search_for = None
                else:
                    w1, w2 = w2, random.choice(self.cache[(w1, w2)])
            else:
                w1, w2 = w2, random.choice(self.cache[(w1, w2)])
    
        return detokenize(results)

    def search_for(self, w1, w2, search_for):
        ''' find a trigram of the form (w1, w2, search_for) '''
        results = []
        if self.tagged:
            for possibility in self.cache[(w1, w2)]:
                if possibility[1] == search_for:
                    results.append(possibility)
        else:
            for possibility in self.cache[(w1, w2)]:
                if possibility == search_for:
                    results.append(possibility)

        #print "searching for:"+search_for, "w1="+str(w1), "w2="+str(w2), "results="+str(results)
        return results
   
    def get_largest(self):
        ''' return the key of the item in the cache with the most possibilities '''
        most = 0
        largest = None
        for (key, possibilities) in self.cache.items():
            if len(possibilities) > most:
                most = len(possibilities)
                largest = key
        return largest

    def get_starter(self):
        ''' return the key of the item in the cache which is best suited for starting the text. '''
        most = 0
        best = None
        if self.istagged():
            for (key, possibilities) in self.cache.items():
                if key[0][0].istitle():
                    if len(possibilities) > most:
                        most = len(possibilities)
                        best = key
        else:
            for (key, possibilities) in self.cache.items():
                if key[0].istitle():
                    if len(possibilities) > most:
                        most = len(possibilities)
                        best = key
        return best

    def istagged(self):
        ''' determine whether our tokens are part-of-speech tagged or not '''
        try:
            if isinstance(self.get_largest()[0], tuple):
                return True
            else:
                return False
        except:
            return False

    def get_tags(self):
        ''' return the different part-of-speech tags in the cache'''
        tags = []
        if self.istagged():
            for possibilities in self.cache.values():
                for possibility in possibilities:
                    tags.append(possibility[1])
            return sorted(set(tags))
        return False

if __name__ == "__main__":
    markov = Markov(nltk.corpus.brown.tagged_words(categories='science_fiction'), use_cache=False)
    print markov.markov_text()
