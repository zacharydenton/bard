#!/usr/bin/env python
# classify dialogue act types
import nltk

def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains(%s)' % word.lower()] = True

    return features

posts = nltk.corpus.nps_chat.xml_posts()[:10000]

featuresets = [(dialogue_act_features(post.text), post.get('class'))
               for post in posts]
size = int(len(featuresets) * 0.1)
train_set, test_set = featuresets[size:], featuresets[:size]
classifier = nltk.NaiveBayesClassifier.train(train_set)

errors = []
for post in posts[:size]:
    guess = classifier.classify(dialogue_act_features(post.text))
    tag = post.get('class')
    if guess != tag:
        errors.append( (tag, guess, post.text) )

for (tag, guess, name) in sorted(errors):
    print 'correct=%-8s guess=%-8s name=%-30s' % (tag, guess, name)

classifier.show_most_informative_features(10)
print "accuracy:", nltk.classify.accuracy(classifier, test_set)
print "# errors:", len(errors), 'out of', len(test_set)
