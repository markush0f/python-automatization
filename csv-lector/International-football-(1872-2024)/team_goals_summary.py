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
all_goals = pd.concat([home_goals, away_goals])

grouped_goals = all_goals.groupby("team")["goals"].sum().reset_index()

total_goals = grouped_goals["goals"].sum()

total_goals_df = pd.DataFrame({"team": ["Total"], "goals": [total_goals]})
goals_each_team = pd.concat([grouped_goals, total_goals_df])
goals_each_team_sorted = goals_each_team.sort_values(
    by="goals", ascending=False
).reset_index(drop=True)

goals_each_team_sorted.to_csv("csv-lector/International-football-(1872-2024)/team_goals_summary.csv", index=False)


# for index, row in grouped_goals.iterrows():
#     team_goals = all_goals.loc[all_goals["team"] == row["team"], "goals"]
#     print(f"Goals of {row['team']}: {team_goals.sum()}")
