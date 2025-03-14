import pandas as pd
from config import football_datasets_parquet_path


def load_data():
    """
    Function that Load data from Parquet files into dataframes from the directory specified by the config file.
    """

    df_appearances = pd.read_parquet(football_datasets_parquet_path + "appearances.parquet")
    df_games = pd.read_parquet(football_datasets_parquet_path + "games.parquet")
    df_leagues = pd.read_parquet(football_datasets_parquet_path + "leagues.parquet")
    df_players = pd.read_parquet(football_datasets_parquet_path + "players.parquet")
    df_shots = pd.read_parquet(football_datasets_parquet_path + "shots.parquet")
    df_teams = pd.read_parquet(football_datasets_parquet_path + "teams.parquet")
    df_stats = pd.read_parquet(football_datasets_parquet_path + "teamstats.parquet")
    
    return df_appearances, df_games, df_leagues, df_players, df_shots, df_teams, df_stats