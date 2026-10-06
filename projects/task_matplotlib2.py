import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv('day02_usage.csv')
a = df["Chat"].to_numpy()
b = df["Video"].to_numpy()
c = df["Study"].to_numpy()
d = df["Games"].to_numpy()
e = a+b+c+d
asum =  df["Chat"].sum()
bsum = df["Video"].sum()
csum = df["Study"].sum()
dsum = df["Games"].sum()

avg = df[e].sum(axis=1)/4
print(avg)