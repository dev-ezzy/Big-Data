def Libraries():
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt

def analyze_df(df):
    """
    This function analyzes a pandas DataFrame and prints various details about it.

    Args:
        df: A pandas DataFrame.
    """

    # Print the DataFrame
    print("DataFrame:")
    print(df)
    print("\n")

    # Print DataFrame info
    print("DataFrame Info:")
    print(df.info())
    print("\n")

    # Print summary statistics for numeric columns
    print("Summary Statistics:")
    print(df.describe(include='all'))  # Include all data types in describe
    print("\n")

    # Print missing values
    print("Missing Values:")
    print(df.isnull().sum())  # Count missing values by column
    print("\n")

    # Print number of duplicate rows
    print("Number of Duplicate Rows:")
    print(df.duplicated().sum())  # Count duplicates
    print("\n")

    # Print data types of each column
    print("Column Data Types:")
    print(df.dtypes)

