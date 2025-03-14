import pandas as pd

"""
This code defines a function that reads each CSV file in a given list and then saves each as a Parquet file.
Iterates over a list of CSV filenames.
Attempts to read each file using UTF-8, then Latin-1, and finally Windows-1252 if previous encodings fail.
Converts each successfully read DataFrame into Parquet format and writes it to a specified output directory.
"""

# Function to convert CSV files to Parquet format
def convert_csv_to_parquet (input_dir, output_dir, list_files):
    # Iterate through the list of files
    for i in list_files:
        # Try to read the CSV file with UTF-8 encoding
        try:
            df = pd.read_csv(input_dir+i,encoding="utf-8")
        # If UTF-8 decoding fails, try with Latin-1 encoding
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(input_dir+i,encoding="latin-1")
            # If Latin-1 decoding fails, try with Windows-1252 encoding
            except  UnicodeDecodeError:
                df = pd.read_csv(input_dir+i,encoding="windows-1252")
        # Convert the DataFrame to Parquet format and save it to the declared directory
        df.to_parquet(output_dir+i.replace(".csv",".parquet"))   
        
        # print(df)
