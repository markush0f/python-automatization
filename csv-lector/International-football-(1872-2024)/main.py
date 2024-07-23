import pandas as pd

dfResults = pd.read_csv("csv-lector/International-football-(1872-2024)/CSV/results.csv")
allRows = dfResults.shape[0] + 1
pd.set_option("display.max_rows", allRows)
print(dfResults.shape[0] + 1)


def sumData(df, *datas):
    sum = 0
    for data in datas:
        sum += df[data].sum()
    print("Result of sum: ", sum)
    return sum

totalGoals = sumData(dfResults, "home_score", "away_score")
print("All matchs of history in international: ", allRows)
print("All goals of history in international: ", totalGoals)
