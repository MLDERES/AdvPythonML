# Import relevant libraries
import pandas as pd
from pathlib import Path

DATA_DIR = Path("../data")
FALSE_VALUES = ["No", "no", "n", "N"]
TRUE_VALUES = ["Yes", "yes", "y", "Y"]


def load_data(fileName: str, **kwargs) -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / f"{fileName}.csv")


def load_excel(fileName: str, **kwargs) -> pd.DataFrame:
    return pd.read_excel(DATA_DIR / f"{fileName}.xlsx", **kwargs)
