import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Haberman.csv")

#Histogram/pdf of "age"
plt.figure(figsize=(8,5))
sns.histplot(df["age"], bins=15, kde=True, color="skyblue")
plt.title("Distribution of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
#cdf of "age"
age_sorted = np.sort(df["age"])
cdf = np.arange(1, len(age_sorted) + 1) / len(age_sorted)
plt.figure(figsize=(8,5))
plt.plot(age_sorted, cdf)
plt.xlabel("Age")
plt.ylabel("CDF")
plt.title("CDF of Age")
plt.grid(True)
plt.show()
#box-plot of "age"
plt.figure(figsize=(6,4))
sns.boxplot(x=df["age"])
plt.title("Box Plot of Age")
plt.xlabel("Age")
plt.show()
#violin-plot of "age"
plt.figure(figsize=(6,4))
sns.violinplot(x=df["age"])
plt.title("Violin Plot of Age")
plt.xlabel("Age")
plt.show()

#Histogram/pdf of "year"
plt.figure(figsize=(8,5))
sns.histplot(df["year"], bins=15, kde=True, color="orange")
plt.title("Year of Operation")
plt.xlabel("Year")
plt.ylabel("Frequency")
plt.show()
#cdf of "year"
year_sorted = np.sort(df["year"])
cdf = np.arange(1, len(year_sorted) + 1) / len(year_sorted)
plt.figure(figsize=(8,5))
plt.plot(year_sorted, cdf)
plt.xlabel("year")
plt.ylabel("CDF")
plt.title("CDF of year")
plt.grid(True)
plt.show()
#box-plot of "year"
plt.figure(figsize=(6,4))
sns.boxplot(x=df["year"])
plt.title("Box Plot of year")
plt.xlabel("year")
plt.show()
#violin-plot of "year"
plt.figure(figsize=(6,4))
sns.violinplot(x=df["year"])
plt.title("Violin Plot of year")
plt.xlabel("year")
plt.show()

# Histogram/pdf of "nodes"
plt.figure(figsize=(8,5))
sns.histplot(df["nodes"], bins=15, kde=True, color="orange")
plt.title("Nodes")
plt.xlabel("Nodes")
plt.ylabel("Frequency")
plt.show()
# cdf of "nodes"
nodes_sorted = np.sort(df["nodes"])
cdf = np.arange(1, len(nodes_sorted) + 1) / len(nodes_sorted)
plt.figure(figsize=(8,5))
plt.plot(nodes_sorted, cdf)
plt.xlabel("nodes")
plt.ylabel("CDF")
plt.title("CDF of nodes")
plt.grid(True)
plt.show()
# box-plot of "nodes"
plt.figure(figsize=(6,4))
sns.boxplot(x=df["nodes"])
plt.title("Box Plot of nodes")
plt.xlabel("nodes")
plt.show()
# violin-plot of "nodes"
plt.figure(figsize=(6,4))
sns.violinplot(x=df["nodes"])
plt.title("Violin Plot of nodes")
plt.xlabel("nodes")
plt.show()

#Histogram/pdf of "status"
plt.figure(figsize=(8,5))
sns.histplot(df["status"], bins=15, kde=True, color="orange")
plt.title("status")
plt.xlabel("status")
plt.ylabel("Frequency")
plt.show()
# cdf of "status"
status_sorted = np.sort(df["status"])
cdf = np.arange(1, len(status_sorted) + 1) / len(status_sorted)
plt.figure(figsize=(8,5))
plt.plot(status_sorted, cdf)
plt.xlabel("status")
plt.ylabel("CDF")
plt.title("CDF of status")
plt.grid(True)
plt.show()