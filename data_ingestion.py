print("Program Started")
import pandas as pd
import os

folder_path = "data/raw"

csv_files = [
    f for f in os.listdir(folder_path)
    if f.endswith(".csv")
]

if len(csv_files) == 0:
    print("No CSV files found in data/raw")
else:
    for file in csv_files:
        path = os.path.join(folder_path, file)

        df = pd.read_csv(path)

        print("\n" + "=" * 50)
        print(f"File: {file}")

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())