import pandas as pd
from data_processing import load_data # Import the load_data function to read Parquet files

def q_3():
    
    # Load all DataFrames from the Parquet files
    df_appearances, df_games, df_leagues, df_players, df_shots, df_teams, df_stats = load_data()

    # Merge the games DataFrame with leagues to include league information for each game
    df_games_league = pd.merge(df_games[["gameID","leagueID"]],df_leagues,how="inner",on="leagueID")

    # Filter the merged DataFrame to include only games from "La Liga"
    df_la_liga = df_games_league[df_games_league["name"] == "La Liga"]

    # Create a new column in df_stats representing the month extracted from the "date" column
    df_stats['month_date'] = pd.to_datetime(df_stats['date']).dt.month

    # Merge La Liga games with game statistics based on "gameID"
    df_la_liga_Stats = pd.merge(df_la_liga,df_stats, how="inner", on= "gameID")

    # Filter the La Liga statistics to include only games where the result was a win ('W')
    wins = df_la_liga_Stats[df_la_liga_Stats["result"] == "W"]

    # Count the number of wins for each team
    wins_count = wins["teamID"].value_counts().reset_index()
    
    # Merge the wins count with team details to get team names
    wins_count_nm = pd.merge(wins_count,df_teams,how="inner",on="teamID")

    # Rename columns
    wins_count_nm.columns = ["teamID",  "wins" ,"name"]
    
    # Select the top 3 teams with the highest number of wins
    teams  = wins_count_nm.nlargest(3, 'wins')

    # Calculate total shots on target per team and month in La Liga stats
    shots_on_target = df_la_liga_Stats.groupby(["teamID", "month_date"])["shotsOnTarget"].sum().reset_index()

    # Rename
    shots_on_target = shots_on_target.rename(columns={"shotsOnTarget": "total_shotsOnTarget"}) 

    # For each team, calculate a 1-month moving average of total shots on target using a rolling window of 2 (current and previous month)
    shots_on_target["moving_avg_1_month"] = shots_on_target.groupby("teamID")["total_shotsOnTarget"].rolling(window=2, min_periods=1).mean().reset_index(0, drop=True)

    # Merge the shots on target statistics with the top 3 teams based on wins
    final = pd.merge(shots_on_target,teams,how="inner",on="teamID").sort_values(["wins"], ascending=[False])

    # Select and rename columns for the final output
    q2 = final[['name', 'month_date', 'total_shotsOnTarget', 'moving_avg_1_month']].reset_index(drop=True)
    q2.columns = ['team_name', 'month_date', 'total_shotsOnTarget', 'moving_avg_1_month']

    return q2