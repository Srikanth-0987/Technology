import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('digital_behaviour.csv')
plt.figure(figsize=(12,5))
# df["Day"] = [f"{i+1}"for i in range(len(df))]
# Minutes = df[["Instagram_Minutes","YouTube_Minutes","WhatsApp_Minutes","LinkedIn_Minutes"]].sum(axis=1)
# plt.xlabel("Day")
# plt.ylabel("Minutes")
# plt.bar(df["Day"],Minutes,color="blue")
# plt.title("My Screen Time by Day")
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()


# minutes= df[["Instagram_Minutes","YouTube_Minutes","WhatsApp_Minutes","LinkedIn_Minutes"]].sum(axis=1)

# plt.bar(x,minutes,color=["blue"])





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