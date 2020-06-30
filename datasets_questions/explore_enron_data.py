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
import pandas as pd

#enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


enron_df = pd.DataFrame.from_dict(enron_data, orient = 'index')
print(enron_df)
print(list(enron_df.columns))
print(enron_df['poi'])
print(sum(enron_df['poi']))

print(enron_df['from_this_person_to_poi'][20:30])

print(enron_data["SKILLING JEFFREY K"]["exercised_stock_options"])



print(enron_df[['total_payments']].sort_values(by=['total_payments']))

print(enron_df[['salary']].sort_values(by=['salary']))


print(enron_df[enron_df.salary.dropna()])

filtered_df = enron_df[enron_df['salary'].isnotnull()]
print(filtered_df)

enron_df.salary.dropna()

print(enron_df[['salary']].dropna().sort_values(by=['salary']))
