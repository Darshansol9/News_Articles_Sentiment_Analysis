# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 13:42:25 2019

@author: Mike
"""

import nltk
import random
#from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC
from nltk.classify import ClassifierI
from statistics import mode
from nltk.tokenize import word_tokenize



class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        return mode(votes)

    def confidence(self, features):
        votes = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)

        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf
    
#short_pos = open("positive.txt","r", encoding="utf-8").read()
#short_neg = open("negative.txt","r", encoding="utf-8").read()
short_pos = open("trainning_files/positive.txt","r", encoding='iso-8859-1').read()
short_neg = open("trainning_files/negative.txt","r", encoding='iso-8859-1').read()
#short_pos = [line.rstrip('\n') for line in open('short_reviews/positive.txt', 'r', encoding='ISO-8859-1')]
#short_neg = [line.rstrip('\n') for line in open('short_reviews/positive.txt', 'r', encoding='ISO-8859-1')]
#short_pos = open("positive.txt","r", encoding='iso-8859-1').read()
#short_neg = open("negative.txt","r", encoding='iso-8859-1').read()

# move this up here
all_words = []
documents = []


#  j is adject, r is adverb, and v is verb
#allowed_word_types = ["J","R","V"]
allowed_word_types = ["J"]

for p in short_pos.split('\n'):
#for p in short_pos.rstrip('\n'):
    documents.append( (p, "pos") )
    words = word_tokenize(p) #@
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())

    
for p in short_neg.split('\n'):
#for p in short_neg.rstrip('\n'):
    documents.append( (p, "neg") )
    words = word_tokenize(p) #@
    pos = nltk.pos_tag(words)
    for w in pos:
        if w[1][0] in allowed_word_types:
            all_words.append(w[0].lower())


#save_documents = open("pickled_models/documents.pickle","wb")
save_documents = open("pickled_models/documents.pickle","wb")
pickle.dump(documents, save_documents)
save_documents.close()

all_words = nltk.FreqDist(all_words)

word_features = list(all_words.keys())[:5000]

save_word_features = open("pickled_models/word_features.pickle","wb")
pickle.dump(word_features, save_word_features)
save_word_features.close()


def find_features(document):
    #words = word_tokenize(document)
    words = document
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features

featuresets = [(find_features(rev), category) for (rev, category) in documents]

random.shuffle(featuresets)
print("total length (surpervised learning): ", len(featuresets))

#@
save_featuresets = open("pickled_models/featuresets.pickle","wb")
pickle.dump(featuresets, save_featuresets)
save_featuresets.close()

#testing_set = featuresets[10000:]
#training_set = featuresets[:10000]
index = round(len(featuresets) * 0.8)
testing_set = featuresets[index:]
training_set = featuresets[:index]

print("trainning set number (80%): ", len(training_set))
print("testing set number (20%): ", len(testing_set))

############### 1st Original Naive Bayes classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naive Bayes model accuracy percent:", (nltk.classify.accuracy(classifier, testing_set))*100)
classifier.show_most_informative_features(15)

save_classifier = open("pickled_models/originalnaivebayes.pickle","wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()

############### 2nd MultinomialNB classifier
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent:", (nltk.classify.accuracy(MNB_classifier, testing_set))*100)

save_classifier = open("pickled_models/MNB_classifier.pickle","wb")
pickle.dump(MNB_classifier, save_classifier)
save_classifier.close()

############### 3rd BernoulliNB classifier
BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier accuracy percent:", (nltk.classify.accuracy(BernoulliNB_classifier, testing_set))*100)

save_classifier = open("pickled_models/BernoulliNB_classifier.pickle","wb")
pickle.dump(BernoulliNB_classifier, save_classifier)
save_classifier.close()

############### 4th LogisticRegression classifier
LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy percent:", (nltk.classify.accuracy(LogisticRegression_classifier, testing_set))*100)

save_classifier = open("pickled_models/LogisticRegression_classifier.pickle","wb")
pickle.dump(LogisticRegression_classifier, save_classifier)
save_classifier.close()

############### 5th LinearSVC classifier
LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:", (nltk.classify.accuracy(LinearSVC_classifier, testing_set))*100)

save_classifier = open("pickled_models/LinearSVC_classifier.pickle","wb")
pickle.dump(LinearSVC_classifier, save_classifier)
save_classifier.close()

##NuSVC_classifier = SklearnClassifier(NuSVC())
##NuSVC_classifier.train(training_set)
##print("NuSVC_classifier accuracy percent:", (nltk.classify.accuracy(NuSVC_classifier, testing_set))*100)

SGDC_classifier = SklearnClassifier(SGDClassifier())
SGDC_classifier.train(training_set)
print("SGDClassifier accuracy percent:",nltk.classify.accuracy(SGDC_classifier, testing_set)*100)

save_classifier = open("pickled_models/SGDC_classifier.pickle","wb")
pickle.dump(SGDC_classifier, save_classifier)
save_classifier.close()