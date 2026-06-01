import pandas as pd
import os

folder_path = "data/raw"

csv_files = [f for f in os.listdir(folder_path) if f.endswith(".csv")]

for file in csv_files:

    path = os.path.join(folder_path, file)

    df = pd.read_csv(path)

    print("\n" + "=" * 60)
    print(f"FILE: {file}")

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nData Types:")
    print(df.dtypes)

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nFirst 5 Rows:")
    print(df.head())