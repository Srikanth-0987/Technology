import numpy as np 
import pandas as pd
df = pd.read_csv('placement_readiness.csv')
# print(df)

# avg = df.groupby("Branch")["Python_Score"].mean()
# print(avg)

# high = df["Aptitude_Score"].max()
# print(high)

# low = df["Aptitude_Score"].min()
# print(low)

# a =(df["Communication_Score"]>70).sum()
# print(a)
# a = df[["Python_Score","SQL_Score","Aptitude_Score","Communication_Score"]].max(axis=1)
# b = df[["Python_Score","SQL_Score","Aptitude_Score","Communication_Score"]].min(axis=1)
# df['gap'] = a - b
# print(df[['Student_ID','gap']])


# print(df.head())
# print(df.shape)
# print(df.info())
# print(df.describe())

# x = (df["Python_Score"]>75).sum()
# print(x)

# y = df.sort_values("Aptitude_Score",ascending=False)
# print(y["Aptitude_Score"])

# z = (df["Python_Score"]).head(10)
# print(z)

# a = df[(df["Python_Score"]>70) & (df["Communication_Score"]<60)]
# print(a["Student_ID"])

# total_score = df[["Python_Score", "SQL_Score", "Aptitude_Score", "Communication_Score"]].sum(axis=1)
# df['Total_Score'] = total_score
# print(df)

# avg = total_score/4
# df['Average_Score'] = avg
# print(df)

# weak = df[["Python_Score","SQL_Score","Aptitude_Score","Communication_Score"]].min(axis=1)
# df['Weak_Skill_Score']=weak
# print(df)

avg_score = df[["Python_Score", "SQL_Score", "Aptitude_Score", "Communication_Score"]].mean(axis=1)
df['Readiness_Score'] = (avg_score + (df["Projects_Completed"]*2) + (df["Mock_Interviews_Attended"]*1)).clip(upper=100)
print(df)
