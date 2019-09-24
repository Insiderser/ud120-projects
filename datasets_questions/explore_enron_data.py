#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data: dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

personsOfInterest = { key: value for key, value in enron_data.items() if value["poi"] }
knownEmailAddress = { key: value for key, value in enron_data.items() if value["email_address"] != "NaN" }
quantifiedSalary = { key: value for key, value in enron_data.items() if value["salary"] != "NaN" }
unknownTotalPayments = { key: value for key, value in enron_data.items() if value["total_payments"] == "NaN" }

for dictionary in [personsOfInterest, knownEmailAddress, quantifiedSalary, unknownTotalPayments]:
    print(len(dictionary))
