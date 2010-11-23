#!/usr/bin/env python
# generate random text using trigrams and markov chains
# this uses part-of-speech tagged data from the Brown corpus
import random
import nltk
import cPickle as pickle

class Markov:
    def __init__(self, tokens, use_cache=False):
        self.tokens = tokens
        self.trigrams = nltk.util.trigrams(self.tokens)
        self.cache = self.generate_cache(self.trigrams, use_cache)
        self.largest = None
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
            if not self.largest:
                self.largest = self.get_largest()
                print self.largest
            w1, w2 = self.largest

        results = []
        for i in range(length):
            if self.tagged:
                results.append(w1[0])
            else:
                results.append(w1)
            w1, w2 = w2, random.choice(self.cache[(w1, w2)])
        if self.tagged:
            results.append(w2[0])
        else:
            results.append(w2)
        return ' '.join(results)
    
    def get_largest(self):
        ''' return the key of the item in the cache with the most possibilities '''
        most = 0
        largest = None
        for (key, possibilities) in self.cache.items():
            if len(possibilities) > most:
                most = len(possibilities)
                largest = key
        return largest

    def istagged(self):
        ''' determine whether our tokens are part-of-speech tagged or not '''
        try:
            if isinstance(self.get_largest()[0], tuple):
                return True
            else:
                return False
        except:
            return False

if __name__ == "__main__":
    markov = Markov(nltk.corpus.brown.tagged_words(), use_cache=True)
    print markov.markov_text()
