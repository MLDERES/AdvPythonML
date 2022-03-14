# Import relevant libraries
import pandas as pd
from pathlib import Path

DATA_DIR = Path("../data")
FALSE_VALUES = ["No", "no", "n", "N"]
TRUE_VALUES = ["Yes", "yes", "y", "Y"]


def load_data(fileName: str, **kwargs) -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / f"{fileName}.csv", **kwargs)


def load_excel(fileName: str, **kwargs) -> pd.DataFrame:
    return pd.read_excel(DATA_DIR / f"{fileName}.xlsx", **kwargs)


def normalize(data:pd.DataFrame, columns, drop_old=False)-> pd.DataFrame:
    for c in columns:
        new_column_name = f"{c}_NORM"
        data[new_column_name] = (data[c] - data[c].min()) / (data[c].max() - data[c].min())
    if drop_old:
        data.drop(columns=columns,inplace=True)
    return data


def standardize(data:pd.DataFrame, columns, drop_old=False)-> pd.DataFrame:
    for c in columns:
        new_column_name = f"{c}_STD"
        data[new_column_name] = (data[c] - data[c].mean()) / data[c].std()
    if drop_old:
        data.drop(columns=columns,inplace=True)
    return data
