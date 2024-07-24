import pandas as pd
import sys

sys.stdout.reconfigure(encoding="utf-8")

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

home_teams = set(dfResults["home_team"])
away_teams = set(dfResults["away_team"])

dfResults["home_team_goals"] = (
    dfResults["home_team"] + "" + dfResults["home_score"].astype(str)
)
dfResults["away_team_goals"] = (
    dfResults["away_team"] + " " + dfResults["away_score"].astype(str)
)

teams_with_goals = list(zip(dfResults["home_team_goals"], dfResults["away_team_goals"]))
# print(teams_with_goals)

home_goals = dfResults[["home_team", "home_score"]].rename(
    columns={"home_team": "team", "home_score": "goals"}
)
away_goals = dfResults[["away_team", "away_score"]].rename(
    columns={"away_team": "team", "away_score": "goals"}
)

print(away_goals)

all_teams = list(home_teams.union(away_teams))
# print(all_teams)
