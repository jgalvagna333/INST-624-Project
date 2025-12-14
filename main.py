import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
import numpy
import scipy
from fbi_api import Fugitive


# USES MODULES I CREATED TO GET DATA USING FBI API AND SAVE DATA TO CSV

print("Getting FBI data using API...\n")

f = Fugitive()
df = f.get_data()

f.save_to_csv("fbi_fugitives.csv")

print("\n")

# USES DATA RETRIEVED FROM FBI API TO RUN A CHI SQUARE TEST TO ANSWER HYPOTHESIS

print("Running Chi Square Test...\n")

sex_all = df['sex'].value_counts()

male_count = sex_all.get("Male", 0)
print(male_count)

female_count = sex_all.get("Female", 0)
print(female_count)

all_fugitives = male_count + female_count
print(all_fugitives)

observed_counts = [male_count, female_count]

expected_counts = [(all_fugitives * .5), (all_fugitives * .5)]

print("\n")

chi_stat, p_val = scipy.stats.chisquare(f_obs = observed_counts, f_exp = expected_counts)

print(f"Chi Stat: {chi_stat:.2f}")
print("P-value: ", p_val, "\n")

alpha = 0.05
if p_val < alpha:
    print("Reject H0 - Sex distribution is NOT 50/50.\n")
else:
    print("Fail to reject H0 - No evidence distribution differs from 50/50.\n")



# CREATES VISULAIZATION OF FBI DATA USED IN PROGRAM AND SAVES IT

print("Creating visualization...\n")

labels = ["Male", "Female"]
values = observed_counts
plt.figure(figsize=(6, 4))

plt.bar(labels, values)

plt.title("Sex Distribution of FBI Fugitives")
plt.xlabel("Sex")
plt.ylabel("Count")

plt.savefig("sex_distribution.png")
plt.close()

print("Done!")