import csv
import numpy as np
import pandas as pd
from projects.complete import APP
insta_list = []
study_list = []
with open("digital_behaviour.csv","r","encoding=utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        insta_list.append(int(row[APP]))
        study_list.append(int(row["Study_Time"]))

insta_list = insta_list[:7]
study_list = study_list[:7]

insta_array = np.array(insta_list)  
study_array = np.array(study_list)

total = insta_array.sum()
print(total)

avg = insta_array.mean()
min = insta_array.min()
max = insta_array.max()

# Indexing

insta_array[0]
insta_array[-1] # vectors
insta_array[0:3] # slicing
insta_array[-2::] # slicing with step

insta_array[1:4]

# insta_array = [val/60 for val in insta_array]
hours = insta_array/60

diff = insta_array - study_array

# boolean Filtering

# [val>100 for val in insta_array]

greate_than_100 = insta_array>100


# [val for val in greater_than_100 if val>100]

# [val for val in insta_array if val>100]

greater = insta_array[insta_array > 100]

count = (insta_array>100).sum()

count1 = insta_array[insta_array > avg]


insta_array[0]
insta_array[::-1]
insta_array[2]


import numpy as np
import pandas as pd
from projects.complete import APP
insta_list = []
study_list = []
with open("degital_behaviour.csv","r","encoding=utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        insta_list.append(int(row[APP]))
        study_list.append(int(row["Study_Time"]))
    
insta_list = insta_list[0:7]
study_list = study_list[0:7]

insta_array = np.array(insta_list)
study_array = np.array(study_list)

total = insta_array.sum()

avg = insta_array.mean()
max = insta_array.max()
