#import libraries

import os

import pandas as pd



#READ IN THE DATA
full_path = os.path.realpath(__file__)
file_path = os.path.dirname(full_path)

result=pd.read_csv(file_path+"\\vgsales.csv")
df=pd.DataFrame(result)

print(df["Genre"].unique())
a=input("Pick a Genre: ")
print(df["Publisher"].unique())
b=input('Pick a Publisher: ')
aggfunc = {"Global_Sales": "sum"}
if a=="" and b=="":
    with pd.option_context("display.max_rows", None):
        df=df.groupby(df["Name"]).aggregate(aggfunc)
        print(df.sort_values("Global_Sales", ascending=False))

elif a=="" and b!="":
    with pd.option_context("display.max_rows", None):
        dfn=df.loc[df["Publisher"]==b, ["Global_Sales", "Name"]]
        dfn=dfn.groupby(dfn["Name"]).aggregate(aggfunc)
        print(dfn.sort_values("Global_Sales", ascending=False))

elif a!="" and b=="":
    with pd.option_context("display.max_rows", None):
        dfn=df.loc[df["Genre"]==a, ["Global_Sales", "Name"]]
        dfn=dfn.groupby(dfn["Name"]).aggregate(aggfunc)
        print(dfn.sort_values("Global_Sales", ascending=False))
else:
    filt=(df['Genre']==a) & (df['Publisher']==b)

    with pd.option_context("display.max_rows", None):
        dfn=df.loc[filt, ["Global_Sales", "Name"]]
        dfn=dfn.groupby(dfn["Name"]).aggregate(aggfunc)
        print(dfn.sort_values("Global_Sales",ascending=False))
