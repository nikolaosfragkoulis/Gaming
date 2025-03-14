# Football Analytics Project

This project processes football data from CSV files, converts them to Parquet, and then answers several questions about player performance, league stats, and custom insights.
The project is structured to make it easy to maintain, extend, and run on any machine with Python 3 and the necessary dependencies installed.

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


## Documentation


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
