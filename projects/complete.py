# import csv
# import numpy as np
# APP="Instagram"
# minutes = []
# with open('digital_behaviour.csv','r') as f:
#     reader = csv.DictReader(f)  ## read the file in dictionary format
#     for row in reader:
#         minutes.append(int(row["Instagram_Minutes"]))
# ## minutes[start:stop:step]
# minutes[:7]
# total=sum(minutes)
# print(total)
# avg = total/len(minutes)
# print(avg)
# avg = total//len(minutes)   
# print(avg)
# maximum = max(minutes)
# print(maximum)
# minimum = min(minutes)
# print(minimum)
# c=0
# for i in minutes:
#     if i>avg:
#         c+=1
# print(f"count is {total} {maximum} {minimum} {avg} {c}") 

# s = "GRIET college Nizampet Hyderabad"
# ans = s.split()
# print(ans)

# " ".join(word[::-1] for word in s.split())

s = [int(num) for num in input().split() if num&1]   ## give even if given number is even other wise zero

s = list(filter(lambda x:x%2, [int(num) for num in input().split()]))

# lambda functions are anonymous functions that can take any number of arguments but can only have one expression.
