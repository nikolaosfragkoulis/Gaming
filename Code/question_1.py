import pandas as pd 
from data_processing import load_data # Import the load_data function to read Parquet files


def q_1():

    # Load DataFrames from Parquet files
    df_appearances, df_games, df_leagues, df_players, df_shots, df_teams, df_stats = load_data()


    # Merge the 'appearances' and 'games' DataFrames on 'gameID' and 'leagueID'
    # This combines details of player appearances with the corresponding game information
    appearances_games = pd.merge(df_appearances,df_games, on=["gameID","leagueID"], how="inner")

    # Group the merged DataFrame by season, league, and player; 
    # aggregate the total goals and shots for each player in each season and league 
    grp_app_games = appearances_games.groupby(["season","leagueID","playerID"]).agg({"goals":"sum", "shots":"sum"})

    # For each season and league combination, select the top 5 rows based on season, league, goals, shots
    grp1 = grp_app_games.groupby(["season","leagueID"]).head(5).reset_index(drop=False).sort_values(["season","leagueID","goals","shots"], ascending=[True,True,False,False])

    # Merge with the players DataFrame to get player names using 'playerID'
    grp1_player_name = pd.merge(grp1,df_players,on="playerID",how="left")
    
    # Merge with the leagues DataFrame to get league names using 'leagueID'
    grp1_league_name = pd.merge(grp1_player_name,df_leagues,on="leagueID",how="left")
    
    # Remove unnecessary columns
    df_q1 = grp1_league_name.drop(columns=["leagueID","playerID","understatNotation"])


    # Rename the columns of the final DataFrame to match the desired output format
    df_q1 = df_q1.rename(columns={
        'season': 'football_season',
        'name_y': 'league_name',       
        'name_x': 'player_name',     
        'goals': 'total_goals'        
    })

    # Define the desired order of columns in the final DataFrame
    new_column_order = [
        'football_season',
        'league_name',
        'player_name',
        'total_goals'
        # Add any other columns in the order you want them
    ]

    # Reorder the columns in the final DataFrame
    df_q1 = df_q1[new_column_order]
    df_q1.sort_values(["league_name","total_goals"], ascending=[True,False])

    return df_q1
