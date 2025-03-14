
import os

"""
This code dynamically determines file paths based on the location of config.py.
It identifies the parent directory (project root) of the current scripts folder, then constructs paths to the football_datasets and Parque_files folders.
Finally, it defines a list of CSV file names to be processed elsewhere in the project.
"""

#Go one level up directory (the Scripts folder)
scripts_dir = os.path.dirname(os.path.abspath(__file__))
#print(scripts_dir)

#Reference the parent folder NOVIBET
project_root = os.path.dirname(scripts_dir)

#print(project_root)

#Construct the paths for football_datasets and Parquet_files:
football_datasets_csv_path = os.path.join(project_root, "football_datasets") + os.sep
football_datasets_parquet_path = os.path.join(project_root, "Parquet_files") + os.sep

# List of CSV files to be processed
csv_files = ["appearances.csv"
            ,"games.csv"
            ,"leagues.csv"
            ,"players.csv"
            ,"shots.csv"
            ,"teams.csv"
            ,"teamstats.csv"]