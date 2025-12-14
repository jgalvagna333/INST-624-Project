from numpy.random import chisquare
import requests
import pandas as pd
import matplotlib.pyplot as plt
import scipy
import json
import os
from fbi_api import Fugitive

# url = "https://api.fbi.gov/wanted/v1/list"
# response = requests.get(url)
# fbi_data = json.loads(response.content)


fbii = Fugitive()

df = fbii.get_data()

print(df)

len(df)

fbii.get_data()
fbii.save_to_csv()




sex_all = df['sex'].value_counts()

male_count = sex_all.get("Male", 0)
print(male_count)

female_count = sex_all.get("Female", 0)
print(female_count)

all_fugitives = male_count + female_count
print(all_fugitives)

observed_counts = [male_count, female_count]

expected_counts = [(all_fugitives * .5), (all_fugitives * .5)]

print(observed_counts)
print(expected_counts)

chi_stat, p_val = scipy.stats.chisquare(f_obs = observed_counts, f_exp = expected_counts)

print(chi_stat)
print(p_val)

alpha = 0.05
if p_val < alpha:
    print("Reject H0 - Sex distribution is NOT 50/50.")
else:
    print("Fail to reject H0 - No evidence distribution differs from 50/50.")


