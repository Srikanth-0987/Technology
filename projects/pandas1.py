import pandas as pd
# Excel handles by python
df = pd.read_csv('digital_behaviour.csv')
print(df)
print(df.head()) ## function
print(df.tail()) # function
print(df.describe()) # attribute
print(df.info()) # attribute
print(df.shape)  # returns a tuple in rows and columns , # attribute
print(df.columns)
print(df[["Instagram_Minutes","Study_Minutes"]].describe())
print(df["WhatsApp_Minutes"]) # returns series
print(df[["Date","Instagram_Minutes"]])
col = ["Instagram_Minutes","Study_Minutes"]  # without using double square brackets
df[col]
print(df["Instagram_Minutes"].sum())
print(df["Instagram_Minutes"].mean())
print(df["YouTube_Minutes"].max())
print(round(df["Instagram_Minutes"].mean(),2))

print(df[df["Instagram_Minutes"]>100])