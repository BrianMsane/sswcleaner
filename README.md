
SiSwati, or Swazi, is a Bantu language spoken by 4.7 million people in Eswatini, formerly known as Swaziland, and South Africa, as a first or second language.
It is one of the African languages that are under-represented as far as NLP research is concerned. That necessitate this project. With it, we are building resources that can be used for research.


We propose three works:

  a. Siswati sentiment analysis dataset that is open-source.
  b. Python library for cleaning siSwati text.
  c. Pre-processing datasets for siSwatin (stopwords, slang words, typos, and borrowed words)

Features

  a. Removes all the stop words for siSwati and English.
  b. Replaces the common slang words with the approriate and official words.
  c. Replaces the common typos with the approriate and official words.
  d. Replaces borrowed words with the siSwati equivalence.
  e. Ensure that vowels do not follow each other, removes adjacent vowels
  f. Adds 'i' at the end of words that do no end with a vowel  
  g. Does the other typical preprocessing that are not language specific.


Install

pip install sswcleaner
pip install git+https://github.com/BrianMsane/ssw-cleaner.git

Usage

from sswcleaner import TextPreprocessor
import pandas as pd

df = pd.read_csv("Enter you dataset")
preprocessor = TextPreprocessor()
df['siSwati_text] = df['siSwati_text].apply(preprocessor.clean_text)
