#Task 1-1
import pandas as pd
df = pd.read_excel("C:/Users/khongorzul/Documents/Python/Week2/HW2/data.xlsx")

#Task 1-2

#25 buyu tuunees deesh nastai emegteichuudiin ners
df=df[(df["age"]>25) & (df["gender"] != "M")]["firstName"]
df.csv = df.to_csv(index = False)