import numpy as np
import pandas as pd

df = pd.read_csv("Haberman.csv")
age = df["age"]
year = df["year"]
nodes = df["nodes"]

print("Descriptive info:\n")
print(df.head())
print(".\n.\n.")
print("Dimensions: ",df.shape)
print("Mean age: ",age.mean())
print("Std age: ",age.std())
print("Mean year: ",year.mean())
print("Std year: ",year.std())
print("Mean nodes: ",nodes.mean())
print("Std nodes: ",nodes.std())