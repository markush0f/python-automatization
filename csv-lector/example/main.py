import pandas as pd

df = pd.read_csv("csv-lector/example/example.csv")


df["Goals+Asists"] = df["Goals"] + df["Asists"]
total = df.groupby("Name")["Goals+Asists"].sum().reset_index()
print(total)
total.to_csv('csv-lector/example/goals_plus_asists.csv', index=False)