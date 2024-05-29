"""
Module for updating pre-processing datasets with relevant words to enhance the cleaning process.
"""

import os
import logging
import pandas as pd
from typos import TYPO
from borrowed import BORROWED
from slang import SLANG
from stopwords import STOPWORDS
logging.basicConfig(level=logging.INFO)


def load_data(name: str, path: str):
    """
    Load the dataset to work with.

    Parameters:
    ----------
    name : str
        The name of the file to load.
    path : str
        The directory path where the file is located (default is "").

    Returns:
    -------
    pd.DataFrame or None
        The loaded dataset as a pandas DataFrame, or None if an error occurs.
    """

    try:

        filepath = os.path.join(path, name)
        extension = os.path.splitext(filepath)[1]
        if extension == '.csv':
            return pd.read_csv(filepath, encoding='latin')
        return None

    except Exception:
        return None


def update_data_files():
    """
    Update the pre-processing datasets by adding new words to Slang.csv, Borrowed.csv, Stopwords.csv, and Typo.csv.

    This function checks for new values in the lists STOPWORDS, SLANG, TYPO, and BORROWED,
    and appends them to the respective columns in the corresponding CSV files.
    """

    try:

        path = '../data/'

        borrow_df = load_data(name='Borrowed.csv', path=path)
        borrow_df_new = pd.DataFrame(BORROWED, columns=['foreign', 'siswati_version'])
        borrow_df_combined = pd.concat([borrow_df, borrow_df_new]).drop_duplicates().reset_index(drop=True)
        borrow_df_combined.to_csv(path + "Borrowed.csv", index=False)

        slang_df = load_data(name='Slang.csv', path=path)
        slang_df_new = pd.DataFrame(SLANG, columns=['slang', 'meaning'])
        slang_df_combined = pd.concat([slang_df, slang_df_new]).drop_duplicates().reset_index(drop=True)
        slang_df_combined.to_csv(path + "Slang.csv", index=False)

        stop_df = load_data(name='Stopwords.csv', path=path)
        stop_df_new = pd.DataFrame(STOPWORDS, columns=['stopwords'])
        stop_df_combined = pd.concat([stop_df, stop_df_new]).drop_duplicates().reset_index(drop=True)
        stop_df_combined.to_csv(path + "Stopwords.csv", index=False)

        typo_df = load_data(name='Typo.csv', path=path)
        typo_df_new = pd.DataFrame(TYPO, columns=['typo', 'correct_word'])
        typo_df_combined = pd.concat([typo_df, typo_df_new]).drop_duplicates().reset_index(drop=True)
        typo_df_combined.to_csv(path + "Typo.csv", index=False)

    except Exception as e:
        logging.error("Exception occurred while updating data files: %s", str(e))

if __name__ == '__main__':
    update_data_files()
