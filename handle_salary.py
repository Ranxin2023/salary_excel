import pandas as pd

df1 = pd.read_excel("workers.xlsx")
df2 = pd.read_excel("salaries_sample.xlsx")
df1 = df1[["name", "level", "hours"]]
df = pd.merge(df1, df2, on=["level", "hours"], how="left")
df = df.set_index("name")
df.to_excel("salaries.xlsx")
