import pandas as pd
from pathlib import Path

df=pd.read_csv("data/sales.csv")
df["Total"]=df["Quantity"]*df["Price"]
print("Data:")
print(df)
print("\nSummary by Category")
summary=df.groupby("Category")[["Quantity","Total"]].sum()
print(summary)
Path("output").mkdir(exist_ok=True)
summary.to_csv("output/summary.csv")
print("\nSaved to output/summary.csv")
