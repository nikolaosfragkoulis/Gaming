import pandas as pd
import numpy as np
from data_processing import load_data # Import the load_data function to read Parquet files


"""
This code analyzes match outcomes to determine which teams perform significantly better at home compared to away. 
It calculates total home wins and away wins for each team, computes win percentages for both situations.

This insight is useful for bettors and analysts to gauge the impact of home support, and for team managers 
to identify if a team might be struggling in away games.
"""

def insights():

    # Load all DataFrames from the Parquet files
    df_appearances, df_games, df_leagues, df_players, df_shots, df_teams, df_stats = load_data()

    # Determine the winner for each game:
    # If the home team scored more than the away team, record the homeTeamID as the winner.
    # Otherwise, if the away team scored more, record the awayTeamID as the winner.
    # If it's a draw, assign 0.
    df_games["winner_home"] = np.where(df_games["homeGoals"] > df_games["awayGoals"],df_games["homeTeamID"],0)
    df_games["winner_away"] = np.where(df_games["homeGoals"]< df_games["awayGoals"],df_games["awayTeamID"],0)

    # Count the number of home wins for each team (ignore 0 which indicates no win)
    distinct_home = df_games["winner_home"].value_counts().reset_index()
    distinct_home.columns = ["winner_home_teamID", "count_home_wins"]
    distinct_home = distinct_home[distinct_home["winner_home_teamID"] > 0] #remove the teamID 0

    # Count the number of away wins for each team (ignore 0)
    distinct_away = df_games["winner_away"].value_counts().reset_index()
    distinct_away.columns = ["winner_away_teamID", "count_away_wins"]
    distinct_away = distinct_away[distinct_away["winner_away_teamID"] > 0] #remove the teamID 0

    # Merge the home and away win counts to create a single DataFrame for each team’s performance
    df_performance = pd.merge(distinct_away,distinct_home,how="outer",left_on="winner_away_teamID",right_on="winner_home_teamID").fillna(0)

    #rename the column
    df_performance.rename(columns={"winner_home_teamID": "teamID"}, inplace=True)
    
    # Merge with the teams DataFrame to include team names
    df_performance = pd.merge(df_performance,df_teams,how="inner",on="teamID")

    #remove unnecessary columns
    df_performance.drop(columns=["winner_away_teamID","teamID"], inplace=True)

    # print(df_performance)
    
    # Calculate the total number of wins (home wins + away wins) for each team
    df_performance["total_wins"] = df_performance["count_away_wins"] + df_performance["count_home_wins"]

    #calculate the percentages for home wins and away wins respectively
    df_performance["home_win_percentage"] = (df_performance["count_home_wins"] / df_performance["total_wins"]) * 100
    df_performance["away_win_percentage"] = (df_performance["count_away_wins"] / df_performance["total_wins"]) * 100

    # Sort the performance DataFrame by home win percentage in descending order 
    df_performance = df_performance.sort_values(by="home_win_percentage", ascending=False)

    return df_performance
