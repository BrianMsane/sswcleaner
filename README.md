
SiSwati, or Swazi, is a Bantu language spoken by 2.4 million people in Eswatini, formerly known as Swaziland, and South Africa, specifically the Mpumalanga Province, as a first or second language. It is one of the African languages that are under-represented as far as NLP research is concerned. That necessitate this project. With this project, we are building resources that can be used for research. 

In this repository we are creating a python package that can be used by individuals and researchers
as they clean siSwati text. I has the general cleaning or pre-processing steps and the siSwati specific cleaning
steps.


## Features

- Removes all the stop words for siSwati and English.
- Replaces the common slang words with the appropriate and official words.
- Replaces the common typos with the appropriate and official words.
- Replaces borrowed words with the siSwati equivalents.
- Ensures that vowels do not follow each other, removes adjacent vowels.
- Adds 'i' at the end of words that do not end with a vowel.
- Performs other typical preprocessing tasks that are not language-specific.


## Install

```bash
pip install sswcleaner
```

Or get the latest changes made in the repo.

```bash
pip install git+https://github.com/BrianMsane/ssw-cleaner.git
```

## Usage

```python
from sswcleaner import TextPreprocessor
import pandas as pd

df = pd.read_csv("Enter you dataset!")
preprocessor = TextPreprocessor()
df['siSwati_text'] = df['siSwati_text'].apply(preprocessor.clean_text)

```

## Contribution

In siSwati we have quite a number of borrowed words, slang words, and people tend to 
communicate in various typos in social media. The lists are huge such that we could not be able
to exhaust them by ourselves. We would like to invite your contribution as well if you know some
of these words that we have omitted here. 
Edit the python scripts that have lists of the words you would like to add and then make a Pull Request
to ###main
You contributon will make a huge difference. Thanks!!