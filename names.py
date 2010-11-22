#!/usr/bin/env python
# classify a name by gender
import random
import re
import nltk

def vowels(word):
    vowels = re.findall('(?i)[aeiouy$]', word)
    return len(vowels)

def gender_features(word):
    return {
        'prefix1': word[:1],
        'prefix2': word[:2],
        'prefix2': word[:3],
        'suffix1': word[-1:],
        'suffix2': word[-2:],
        'suffix3': word[-3:],
        #'length': len(word),
        #'vowels': vowels(word),
    }

names = ([(name, 'male') for name in nltk.corpus.names.words('male.txt')] + 
         [(name, 'female') for name in nltk.corpus.names.words('female.txt')])

random.shuffle(names)

train_names = names[1500:]
test_names = names[:500]
devtest_names = names[500:1500]

train_set = [(gender_features(name), gender) for (name, gender) in train_names]
test_set = [(gender_features(name), gender) for (name, gender) in test_names]
devtest_set = [(gender_features(name), gender) for (name, gender) in devtest_names]

classifier = nltk.NaiveBayesClassifier.train(train_set)

errors = []
for (name, tag) in devtest_names:
    guess = classifier.classify(gender_features(name))
    if guess != tag:
        errors.append( (tag, guess, name) )

for (tag, guess, name) in sorted(errors):
    print 'correct=%-8s guess=%-8s name=%-30s' % (tag, guess, name)

classifier.show_most_informative_features(10)
print "accuracy:", nltk.classify.accuracy(classifier, devtest_set)
print "# errors:", len(errors), 'out of', len(devtest_names)
