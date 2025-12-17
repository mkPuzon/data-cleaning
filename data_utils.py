'''data_utils.py

Contains helpful functions for loading, cleaning, and preprocessing data for ML applications.

Dec 2025
'''
import pandas as pd
from pathlib import Path
from collections.abc import Callable # for typing

def load_with_encodings(loader_func: Callable, filepath: Path):
    ENCODINGS = ['utf-8', 'cp1252', 'latin1', 'iso-8859-1']

    for encoding in ENCODINGS:
        try:
            # print(f"Attempting to load {filepath.name} with {encoding}...")
            return loader_func(filepath, encoding=encoding)
        except UnicodeDecodeError:
            continue # move onto next encoding option
        except Exception as e:
            raise e # if syntax/file not found error
        
    raise ValueError(f"Failed to decode {filepath} with common encodings.")

def load_dataset_as_df(filepath: str) -> pd.DataFrame:
    '''
    Loads multiple types of datasets into a Pandas DataFrame. Currently supported filetypes: 
    csv, xlsx, xls, json, & pkl.
    
    :param filepath: String of local path to data.
    :type filepath: str
    :return: Data from filepath.
    :rtype: DataFrame
    '''
    path = Path(filepath)
    ext = path.suffix.lower()
    
    text_loaders = { # may raise encoding errors
        '.csv': pd.read_csv,
        '.txt': pd.read_excel,
        '.xml': pd.read_excel,
        '.json': pd.read_json
    }
    binary_loaders = { # don't raise encoding errors
        '.xlsx': pd.read_excel,
        '.xls': pd.read_excel,
        '.pkl': pd.read_pickle
    }
    if ext in binary_loaders:
        return binary_loaders[ext](filepath)
    elif ext in text_loaders:
        return load_with_encodings(loader_func=text_loaders[ext], filepath=path)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")
