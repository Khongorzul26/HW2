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