import numpy as np
import pandas as pd

df = pd.read_csv('digital_behaviour.csv')

df.head()
df.tail()
df.shape
print(df.info())
print(df.describe())

print(df["Instagram_Minutes"])
print(df[["Instagram_Minutes","Date"]])

print(df["Instagram_Minutes"].sum())

print(df["Study_Minutes"].mean())

print(df[df["YouTube_Minutes"]>df["YouTube_Minutes"].mean()])

a = df[df["Instagram_Minutes"]>100]
print(a['Instagram_Minutes'])

b = df[df["Study_Minutes"]>180]
print(b['Study_Minutes'])

d = df[(df["Instagram_Minutes"]>180) & (df["Study_Minutes"]<100)]
print(d[["Date", "Instagram_Minutes", "Study_Minutes"]])

e = (df["Instagram_Minutes"].mean())
print(df[["Date","Instagram_Minutes"]])

heavy_instagram_days = df[df["Instagram_Minutes"] > df['Instagram_Minutes'].mean()]
print(heavy_instagram_days)

df["Instagram_Minutes"].sort_values()

g = df["Instagram_Minutes"].sort_values(ascending=True)
print(g)

print(df["Instagram_Minutes"].head(5))

best_study_days = df.sort_values(by="Study_Minutes", ascending=False)[["Date", "Study_Minutes"]].head(5)
print(best_study_days)


x = df.sort_values(by="Study_Minutes",ascending=False)[["Date","Study_Minutes"]].head(5)
print(x)

y = df["Study_Minutes"]

Total_Screen_Time = (df["Instagram_Minutes"] + df["YouTube_Minutes"] + df["WhatsApp_Minutes"] + df["LinkedIn_Minutes"]).sum()

df["Total_Screen_Time"]=Total_Screen_Time
print("Total_Screen_Time")

screen_Hours = Total_Screen_Time/60
df["Screen_Hours"]=screen_Hours
print("Screen_Hours")

digital_Balance = y/Total_Screen_Time
df["Digital_Balance"] = digital_Balance
print("Digital_Balance")

day_Type = np.where(
	df[["Instagram_Minutes", "YouTube_Minutes", "WhatsApp_Minutes", "LinkedIn_Minutes"]].sum(axis=1) > 300,
	"Heavy",
	"Normal",
)
df["Day_Type"] = day_Type
print(df["Day_Type"])    

df.to_csv('my_analysis.csv')