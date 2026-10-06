import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('my_analysis.csv')
plt.figure(figsize=(12,5))
df["Day"] = [f"{i+1}"for i in range(len(df))]
Minutes = df[["Instagram_Minutes","YouTube_Minutes","WhatsApp_Minutes","LinkedIn_Minutes"]].sum(axis=1)
plt.xlabel("Day")
plt.ylabel("Minutes")
plt.bar(df["Day"],Minutes,color="blue")
plt.title("My Screen Time by Day")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()



plt.title("Total Time by App")
plt.xlabel("App")
plt.ylabel("Minutes")
App = ["Instagram","WatsApp","YouTube","Linkedin"]
Minutes= [
          df["Instagram_Minutes"].sum() , 
          df["YouTube_Minutes"].sum() ,
          df["WhatsApp_Minutes"].sum() , 
          df["LinkedIn_Minutes"].sum()
          ]
plt.bar(App,Minutes,color=["red","blue","green","Yellow"])
plt.show()


plt.title("Study versus screen")
plt.xlabel("Study_Minutes")
plt.ylabel("Total_Screen_Time")
App = ["Instagram","WatsApp","YouTube","Linkedin"]
Minutes= [
          df["Instagram_Minutes"].sum() , 
          df["YouTube_Minutes"].sum() ,
          df["WhatsApp_Minutes"].sum() , 
          df["LinkedIn_Minutes"].sum()
          ]
plt.plot(App,Minutes, label="Study Minutes", color="teal", marker="o", linewidth=2)
plt.plot(App,Minutes,label="Total Screen Time", color="crimson", marker="s", linewidth=2)
plt.legend(loc="upper right")
plt.show()



App = ["Instagram","WatsApp","YouTube","Linkedin"]
Minutes= [
          df["Instagram_Minutes"].sum() , 
          df["YouTube_Minutes"].sum() ,
          df["WhatsApp_Minutes"].sum() , 
          df["LinkedIn_Minutes"].sum()
          ]
custom_colors = ['red','green','blue','yellow']

plt.pie(
    Minutes, 
    labels=App, 
    colors=custom_colors,
    autopct='%1.1f%%',     
    startangle=140,         
    shadow=False              
)

plt.title("Daily Time Distribution", fontsize=14, fontweight='bold')
plt.legend(title="Activities", loc="upper left", bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()
