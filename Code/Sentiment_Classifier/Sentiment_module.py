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
import time

class VoteClassifier(ClassifierI):
    def __init__(self, *classifiers):
        self._classifiers = classifiers

    def classify(self, features, time_analysis):
        votes = []
        times = []
        for c in self._classifiers:
            if time_analysis: start_t = time.clock()
            v = c.classify(features)
            if time_analysis: 
                end_t = time.clock()
                times.append(end_t - start_t)
            votes.append(v)
        votes.append(mode(votes))
        return votes, times

    def confidence(self, features):
        votes = []
        votes_re = []
        for c in self._classifiers:
            v = c.classify(features)
            votes.append(v)
        #print(votes)
        choice_votes = votes.count(mode(votes))
        conf = choice_votes / len(votes)
        return conf

documents_f = open("pickled_models/documents.pickle", "rb")
documents = pickle.load(documents_f, encoding='iso-8859-1')
documents_f.close()

word_features_f = open("pickled_models/word_features.pickle", "rb")
word_features = pickle.load(word_features_f, encoding='iso-8859-1')
word_features_f.close()


def find_features(document):
    words = word_tokenize(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)

    return features



featuresets_f = open("pickled_models/featuresets.pickle", "rb")
featuresets = pickle.load(featuresets_f, encoding='iso-8859-1')
featuresets_f.close()

random.shuffle(featuresets)
print(len(featuresets))

#index = round(len(featuresets) * 0.8)
#testing_set = featuresets[index:]
#training_set = featuresets[:index]

open_file = open("pickled_models/originalnaivebayes.pickle", "rb")
classifier = pickle.load(open_file, encoding='iso-8859-1')
open_file.close()


open_file = open("pickled_models/MNB_classifier.pickle", "rb")
MNB_classifier = pickle.load(open_file, encoding='iso-8859-1')
open_file.close()
"""
open_file = open("pickled_models/randomForest_classifier.pickle", "rb")
randomForest_classifier = pickle.load(open_file, encoding='iso-8859-1')
open_file.close()
"""
open_file = open("pickled_models/BernoulliNB_classifier.pickle", "rb")
BernoulliNB_classifier = pickle.load(open_file, encoding='iso-8859-1')
open_file.close()


open_file = open("pickled_models/LogisticRegression_classifier.pickle", "rb")
LogisticRegression_classifier = pickle.load(open_file, encoding='iso-8859-1')
open_file.close()


open_file = open("pickled_models/LinearSVC_classifier.pickle", "rb")
LinearSVC_classifier = pickle.load(open_file, encoding='iso-8859-1')
open_file.close()


open_file = open("pickled_models/SGDC_classifier.pickle", "rb")
SGDC_classifier = pickle.load(open_file, encoding='iso-8859-1')
open_file.close()




voted_classifier = VoteClassifier(
                                  classifier,
                                  LinearSVC_classifier,
                                  MNB_classifier,
                                  BernoulliNB_classifier,
                                  #randomForest_classifier,
                                  LogisticRegression_classifier)




def sentiment(text):
    feats = find_features(text)
    return voted_classifier.classify(feats),voted_classifier.confidence(feats)

def sentiment_file(file, time_analysis):
    text = open(file,"r", encoding='iso-8859-1').read()
    words = word_tokenize(text)
    feats = {}
    for w in word_features:
        feats[w] = (w in words)
    return voted_classifier.classify(feats, time_analysis)#,voted_classifier.confidence(feats)

