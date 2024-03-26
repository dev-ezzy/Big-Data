def Libraries():
    import pandas as pd
    import numpy as np
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    
    
    
import pandas as pd

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


# EDA
#writting helper function to help us make x-axis countplots in our EDA process
def sns_xcount(column , data):
    sns.countplot(x = column, data = data)
    plt.title(f"{column} count in our data set")
    plt.show();

#writting helper function to help us make y-axis countplots in our EDA process
def sns_ycount(column , data):
    sns.countplot(y = column, data = data)
    plt.title(f"{column} count in our data set")
    plt.show();
    
#helper function for plotting multivariate countplots
def multivariate_ycountplot(column, data):
    sns.countplot(y = column, data = data, hue= "status_group", palette= "bright");
    plt.legend(loc= "best")

def multivariate_xcountplot(column, data):
    sns.countplot(x = column, data = data,  hue= "status_group", palette= "bright");
    plt.xticks(rotation = 45)
    plt.legend(loc= "best")