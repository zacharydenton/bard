#!/usr/bin/env python
# generate random text using trigrams and markov chains
# this uses part-of-speech tagged data from the Brown corpus
import random
import nltk
import cPickle as pickle

class Markov:
    def __init__(self, tokens):
        self.tokens = tokens
        self.trigrams = nltk.util.trigrams(self.tokens)
        self.cache = self.generate_cache(self.trigrams)

    def generate_cache(self, trigrams):
        # generate a dict 
        # where keys are (v1, v2) and value is list of 
        # possible v3's 
        try:
            print "loading markov cache..."
            cachefile = open('.markov_cache', 'rb')
            cache = pickle.load(cachefile)
            cachefile.close()
        except:
            print "generating trigrams cache..."
            cache = {}
            for w1, w2, w3 in trigrams:
                key = (w1, w2)
                if key in cache:
                    cache[key].append(w3)
                else:
                    cache[key] = [w3]
            cachefile = open('.markov_cache', 'wb')
            pickle.dump(cache, cachefile, -1)
            cachefile.close()
        return cache
        
    def markov_text(self, w1=('being', 'BEG'), w2=('in', 'IN'), length=100):
        results = []
        for i in range(length):
            results.append(w1[0])
            w1, w2 = w2, random.choice(self.cache[(w1, w2)])
        results.append(w2[0])
        return ' '.join(results)

if __name__ == "__main__":
    markov = Markov(nltk.corpus.brown.tagged_words())
    print markov.markov_text()
