import pandas as pd

dfResults = pd.read_csv("csv-lector/International-football-(1872-2024)/CSV/results.csv")
allRows = dfResults.shape[0] + 1
pd.set_option("display.max_rows", allRows)

