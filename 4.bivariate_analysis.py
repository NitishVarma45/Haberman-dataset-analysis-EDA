import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Haberman.csv")

sns.pairplot(
    df,
    vars=["age", "nodes", "year"],
    hue="status",
    diag_kind="kde",
    height=2.5
)
plt.show()

plt.figure(figsize=(7,5))
sns.boxplot(x="status", y="nodes", data=df)
plt.xlabel("Survival Status")
plt.ylabel("Number of Positive Nodes")
plt.title("Nodes vs Survival Status")
plt.xticks([0, 1], ["Survived", "Not Survived"])
plt.show()

plt.figure(figsize=(7,5))
sns.violinplot(x="status", y="nodes", data=df)
plt.xlabel("Survival Status")
plt.ylabel("Number of Positive Nodes")
plt.title("Nodes vs Survival Status")
plt.xticks([0, 1], ["Survived", "Not Survived"])
plt.show()