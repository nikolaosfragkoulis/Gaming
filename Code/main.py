import pandas as pd
from config import (football_datasets_csv_path,football_datasets_parquet_path,csv_files)
from data_ingestion import convert_csv_to_parquet
from question_1 import q_1
from question_2 import q_2
from question_3 import q_3
from custom_insights import insights



# Main function to execute the CSV to Parquet conversion
def main():
    print("Converting CSV files to Parquet...")
    convert_csv_to_parquet(football_datasets_csv_path,football_datasets_parquet_path,csv_files)
    print("Converting Completed...")

    print("Processing data and retrieving top 5 players per league and season for Question 1...")
    answer_q1 = q_1()
    print(answer_q1.to_string())

    print("Processing data and retrieving in which half we had the most goals from corners for Question 2...")
    answer_q2 = q_2()
    print(answer_q2.to_string())

    print("Processing data and retrieving the average shots on target for every team in La Liga for Question 3...")
    answer_q3 = q_3()
    print(answer_q3.to_string())


    print("Processing data for Custom Insight...")
    print("Home vs. Away Performance!")
    answer_insights = insights()
    print(answer_insights.to_string())

# Execute the main function when the script is run
if __name__=="__main__":
    main()
