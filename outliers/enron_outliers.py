#!/usr/bin/python

import pickle
import matplotlib.pyplot
from tools.feature_format import featureFormat


### read in data dictionary, convert to numpy array
data_dict: dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
data_dict.pop("TOTAL")

features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
print(sorted(data, key=lambda entry: entry[0] + entry[1], reverse=True))


for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
