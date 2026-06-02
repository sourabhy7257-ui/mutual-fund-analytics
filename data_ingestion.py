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
        fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].nunique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nColumns in Fund Master:")
print(fund_master.columns.tolist())
print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())