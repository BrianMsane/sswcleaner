
SiSwati, or Swazi, is a Bantu language spoken by 4.7 million people in Eswatini, formerly known as Swaziland, and South Africa, as a first or second language. It is one of the African languages that are under-represented as far as NLP research is concerned. That necessitate this project. With it, we are building resources that can be used for research.


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
from sswcleaner.cleaner import TextPreprocessor
import pandas as pd

df = pd.read_csv("Enter you dataset!")
preprocessor = TextPreprocessor()
df['siSwati_text'] = df['siSwati_text'].apply(preprocessor.clean_text)

```

## Articles

