'''
Data profiling module.

This module is responsible for computing basic descriptive
data quality metrics for a CSV dataset. The results are used
as input for scoring and reporting.

Currently calculated metrics:
- Number of rows
- Duplicate row rate
- Null value rate per column
'''

import pandas as pd


def profile(csv):
    '''
    Profile a CSV dataset and return basic data quality metrics.

    Parameters
    ----------
    csv : str
        Path to the input CSV file.

    Returns
    -------
    dict
        Dictionary containing:
        - rows (int): total number of rows in the dataset
        - duplicate_rate (float): fraction of duplicate rows
        - null_rate (dict): null value rate per column
    '''

    # Load dataset into a pandas DataFrame
    df = pd.read_csv(csv)

    # Total number of rows
    rows = len(df)

    # Fraction of duplicate rows (0.0 = no duplicates, 1.0 = all duplicates)
    duplicate_rate = float(df.duplicated().mean())

    # Null value rate per column (share of missing values)
    null_rate = df.isna().mean().to_dict()

    return {
        "rows": rows,
        "duplicate_rate": duplicate_rate,
        "null_rate": null_rate,
    }
