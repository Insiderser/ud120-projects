#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

from time import time

from sklearn.svm import SVC

from tools.email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# features_train = features_train[:int(len(features_train) / 100)]
# labels_train = labels_train[:int(len(labels_train) / 100)]

#########################################################
### your code goes here ###

classifier = SVC(C=10000, kernel="rbf")

t0 = time()
classifier.fit(features_train, labels_train)
print("Training time: ", round(time() - t0, 3), "s", sep='')

t0 = time()
classifier.predict(features_test)
print("Predicting time: ", round(time() - t0, 3), 's', sep='')

print("Accuracy:", classifier.score(features_test, labels_test))  # 0.9908987485779295

#########################################################
