# Football Analytics Project

This project processes football data from raw CSV files, converts them to Parquet, and then answers several questions about player performance, league stats, and custom insights.
The project is structured to make it easy to maintain, extend, and run on any machine with Python 3 and the necessary dependencies installed.

```
  Insights Provided:
  
  Question 1: Top 5 players with most goals (and shots) per league and season.
  Question 2: Analysis of corner-related goal statistics by half.
  Question 3: La Liga team performance with rolling averages for shots on target.
  Custom Insight: Comparison of team performance at home versus away.

```


## Documentation - Steps Taken to Reach the Final Solution

1. ### Dynamic Configuration of File Paths
    **Modular Configuration:**
    To enhance portability, we created a **config.py** file that dynamically determines the project's root folder and constructs paths for both the CSV and Parquet directories.
    This ensures that the project works correctly regardless of the computer or directory in which it is placed.

    **Centralized Settings:**
    The configuration file also includes a list of CSV filenames to be processed, keeping all file path settings in one centralized location.

2. ### Data Ingestion and Preparation
    **Raw Data:**
    We began with raw football data provided in CSV format stored in the football_datasets/ folder.
   
    **Handling Different Encodings:**
    During initial testing, it was discovered that some CSV files used different character encodings.
    To address this, the data ingestion process was designed to attempt multiple encodings (UTF-8, Latin-1, and Windows-1252) to ensure that all files were read correctly..

3. ### Conversion to Parquet Format
    **Rationale:**
    Converting CSV files to Parquet improves data loading speeds and reduces storage overhead.
   
    **Implementation:**
    In **data_ingestion.py**, a function was created to loop through each CSV file, try the various encodings if needed, and convert the successfully read DataFrames into Parquet files stored in the Parquet_files/ folder.

4. ### Data Loading and Processing
    **Loading Parquet Files:**
    In **data_processing.py**, the load_data() function reads the Parquet files from the directory specified in **config.py** and loads them into pandas DataFrames for analysis.

    **Modular Design:**
    Separating data ingestion and loading into different modules allows for easier maintenance and extension of the project.

5. ### Analysis and Insights Generation

    **Question 1:**
    We merged player appearances with game data to calculate total goals and shots per player for each season and league, and then extracted the top 5 performers.

    **Question 2:**
    We analyzed corner-related goals by filtering shots based on their originating situation and match half, determining which half yielded more corner goals.

    **Question 3:**
    Focusing on La Liga, we merged game statistics with league information and calculated performance metrics such as total shots on target and moving averages(used a rolling window of 2 current and previous month).

    **Custom Insights:**
    An additional analysis compared teams' home and away performances by computing win percentages.
    This could help bettors and analysts understand home-field advantage and team managers to analyze if they struggle in away games.
    Could indicate fan support impact or stadium conditions influencing results.
    Implementation Logic:
    Use the games table to count total home wins vs. away wins for each team.
    Calculate win rate (%) for home vs. away games.

## Folder Structure

```
  Gaming/                       Root Folder
  ├── football_datasets/        Raw CSV files
  ├── Parque_files/             Generated Parquet files
  ├── Code/
  │   ├── config.py             Configuration file
  │   ├── custom_insights.py    Custom Insights
  │   ├── data_ingestion.py     Contains functions to convert CSV files to Parquet format.
  │   ├── data_processing.py    Load Parquet files into Pandas DataFrames
  │   ├── main.py               Main script that orchestrates the project workflow
  │   ├── question_1.py         Answer of Question 1
  │   ├── question_2.py         Answer of Question 2
  │   └── question_3.py         Answer of Question 3
  └── requirements.txt          Code dependencies needed to run the project
```






## Steps to Run the Project

  1. **Clone the Repository**

   Open your terminal or command prompt and navigate to the directory where you want to store the project. Then, run the following command to clone the Git repository:

   ```bash
   git clone https://github.com/nikolaosfragkoulis/Gaming.git
   ```

  2. **Navigate to the Project Directory**

   Change your current directory to the newly cloned project:

   ```bash
   cd Gaming
   ```

  3. **Create and Activate a virtual environment (Optional)**
  
   - **Create a new environment**:
     ```bash
     python -m venv venv
     ```
   - **Activate the environment**:
     ```bash
     venv\Scripts\activate
     ```

  4. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

  4. **Run the code**
   ```bash
   python Code\main.py
   ```
