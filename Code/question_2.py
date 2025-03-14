import pandas as pd
from data_processing import load_data # Import the load_data function to read Parquet files

def q_2():

    # Load DataFrames
    df_appearances, df_games, df_leagues, df_players, df_shots, df_teams, df_stats = load_data()

    #create a new column named "half" in df_shots dataframe and take 1 if the shot was taken in the first half  and "2" otherwise
    df_shots["half"] = df_shots['minute'].apply(lambda x: "1" if x <= 45 else "2")
    
    # Filter the shots DataFrame to include only shots taken from a corner that resulted in a goal
    goals_corners = df_shots[(df_shots["situation"]=="FromCorner")& (df_shots["shotResult"]=="Goal")]

    # Merge the filtered shots with game details using "gameID" 
    g_c_l = pd.merge(goals_corners,df_games,how="inner",on="gameID")

    # Merge the result with league information using "leagueID"
    f = pd.merge(g_c_l,df_leagues,how="inner",on="leagueID")

    # Select only the necessary columns for grouping
    a = f[["season", "leagueID", "half", "shotResult","name"]]

    # Group by season, leagueID, league name, and half to count the occurrences
    df_grouped = a.groupby(["season", "leagueID", "name", "half"]).size().reset_index(name="count")

    # For each season and league, determine the half with the maximum count
    df_max_half = df_grouped.loc[df_grouped.groupby(["season", "leagueID"])["count"].idxmax()]

    # Keep only relevant columns
    df_final = df_max_half[["season", "name", "half"]]

    #Rename the columns to match the desired output format
    df_final_q2 = df_final.rename(columns={
        'season': 'football_season',       
        'name': 'league_name'        
    })

    return df_final_q2