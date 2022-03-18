# Import relevant libraries
import pandas as pd
from pathlib import Path
from pandas.core.dtypes.inference import is_list_like

DATA_DIR = Path.cwd().parents[0]/'data'
FALSE_VALUES = ["No", "no", "n", "N"]
TRUE_VALUES = ["Yes", "yes", "y", "Y"]


def load_data(fileName: str, **kwargs) -> pd.DataFrame:
    data_file = DATA_DIR/f'{fileName}.csv'
    print(data_file)
    return pd.read_csv(DATA_DIR / f"{fileName}.csv", **kwargs)


def load_excel(fileName: str, **kwargs) -> pd.DataFrame:
    return pd.read_excel(DATA_DIR / f"{fileName}.xlsx", **kwargs)


def normalize(df:pd.DataFrame, columns, drop_old=False)-> pd.DataFrame:
    data = df.copy(deep=True)
    for c in columns:
        new_column_name = f"{c}_NORM"
        data[new_column_name] = (data[c] - data[c].min()) / (data[c].max() - data[c].min())
    if drop_old:
        data.drop(columns=columns,inplace=True)
    return data


def standardize(df:pd.DataFrame, columns, drop_old=False)-> pd.DataFrame:
    data = df.copy(deep=True)
    for c in columns:
        new_column_name = f"{c}_STD"
        data[new_column_name] = (data[c] - data[c].mean()) / data[c].std()
    if drop_old:
        data.drop(columns=columns,inplace=True)
    return data

def _get_list(item, errors='ignore'):
    """
    Return a list from the item passed.
    If the item passed is a string, put it in a list.
    If the item is list like, then return it as a list.
    If the item is None, then the return depends on the errors state
        If errors = 'raise' then raise an error if the list is empty
        If errors = 'ignore' then return None
        If errors = 'coerce' then return an empty list if possible
    :param item: either a single item or a list-like
    :param return_empty: if True then return an empty list rather than None
    :return:
    """
    retVal = None
    if item is None:
        if errors=='coerce':
            retVal = []
        elif errors=='raise':
            raise ValueError(f'Value of item was {item} expected either a single value or list-like')
    elif is_list_like(item):
        retVal = list(item)
    else:
        retVal = [item]
    return retVal

def _get_column_list(df, columns=None):
    '''
    Get a list of the columns in the dataframe df.  If columns is None, then return all.
    If columns has a value then it should be either a string (col-name) or a list
    :param df:
    :param columns:
    :return:
    '''
    cols = _get_list(columns)
    return list(df.columns) if cols is None else list(set(df.columns).intersection(cols))

