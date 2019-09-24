#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""

from time import time
from tools.email_preprocess import preprocess
from sklearn.naive_bayes import GaussianNB

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

t0 = time()

classifier = GaussianNB()
classifier.fit(features_train, labels_train)

print("Training time: ", round(time() - t0, 3), "s", sep='')

t0 = time()
classifier.predict(features_test)
print("Predicting time: ", round(time() - t0, 3), "s", sep='')

accuracy = classifier.score(features_test, labels_test)
print("Accuracy:", accuracy)  # 0.9732650739476678

#########################################################
