"""
Module for running unit tests.
"""

import sys
import logging
import pandas as pd
sys.path.append('../cleaner/')
from clean import TextPreprocessor

try:

    cleaner = TextPreprocessor()
    df = pd.read_csv("a.csv", usecols=['text'])
    df['text'] = df['text'].apply(cleaner.clean_text)

except Exception:
    logging.info("Test Filed! %s")
