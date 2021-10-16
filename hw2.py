#Task 1-1
import pandas as pd
df = pd.read_excel("C:/Users/khongorzul/Documents/Python/Week2/HW2/data.xlsx")

#Task 1-2
#25 buyu tuunees deesh nastai emegteichuudiin ners
df_female = df[(df["age"]>25) & (df["gender"] != "M")]["firstName"]
df_csv = df_female.to_csv(index = False)

#Task 1-3
#23 buyu tuunees doosh nastai eregteichuudin ners
df_male = df[(df["age"]<23) & (df["gender"] == "M")]["firstName"]

#save json
import json
df_json = df_male.to_json(orient = "split")

#Task 2-1
import numpy as np
df.iloc[16, 2:6] #17 dahi mur = 16 dahi mur, 2-5 dahi baganad 2,3,4,5 gsen baganiin utguud orno gej tootsoolov. 

#Task 2-2
df.loc[24:27,("firstName", "age")] 

#Task 2-3
df.groupby(['gender']).agg({'age': ["min", "mean","max"], 'salary': ["min", "mean", "max"]})

#Task 2-4
table = df.pivot_table(index = ['gender'],aggfunc = {'salary' : [min, max, np.mean], 'age': [min, max, np.mean]})
table

