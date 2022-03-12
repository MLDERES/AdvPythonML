# Import relevant libraries
import pandas as pd
from pathlib import Path
DATA_DIR = Path('../data')

def load_data(fileName:str) ->pd.DataFrame:
    return pd.read_csv(DATA_DIR/f'{fileName}.csv')
    