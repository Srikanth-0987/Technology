import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
df = pd.read_csv('day02_usage.csv')
a = df["Chat"].to_numpy()
b = df["Video"].to_numpy()
c = df["Study"].to_numpy()
d = df["Games"].to_numpy()

asum = df["Chat"].sum()
bsum = df["Video"].sum()
csum = df["Study"].sum()
dsum = df["Games"].sum()

aavg = df["Chat"].mean()
bavg = df["Video"].mean()
cavg = df["Study"].mean()
davg = df["Games"].mean()

balance = a - d
# print(balance.argmax())
print(balance.argmax())
print(balance.argmin())
print(balance.max())
print(balance.min())

z = df.idxmax(axis=1)
print(z)
