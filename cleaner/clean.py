"""
Module for text cleaning.

This module provides a class and methods for preprocessing and cleaning text data, 
with specific functionalities tailored for siSwati text.
"""


import sys
import re
import string
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
sys.path.append("../utils/")
import stopwords as stop

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


class TextPreprocessor:
    """
        A siSwati-specific text cleaning module for NLP tasks. 

        This module provides various preprocessing methods tailored for cleaning siSwati text, 
        making it a useful resource for researchers and developers working with siSwati language data.
    """


    def __init__(self):
        self.stopwords = list(set(stopwords.words('english')))
        self.stopwords.extend(stop.STOPWORDS)

    def clean_text(self, text: str) -> str:
        """
            Clean and preprocess text data by applying various cleaning methods.

            Parameters:
            ----------
            text : str
                The text to be cleaned.

            Functionalities:
            ---------------
            1. Remove siSwati and English stopwords, and borrowed words.
            2. Resolve slang words.
            3. Resolve common typos found in dialect.
            4. Convert all characters to lowercase.
            5. Remove punctuation and extra white spaces.
            6. Remove numbers.
            7. Remove emojis and emoticons.
            8. Remove HTML tags and hyperlinks.
            9. Adds 'i' at the end of words without a vowel at the end.
        """


        try:

            path = '../data/'
            slang_data = pd.read_csv(path + 'Slang.csv', usecols=['slang', 'meaning'])
            typo_data = pd.read_csv(path + 'Typo.csv', usecols=['typo', 'correct_word'])
            borrowed_data = pd.read_csv(path + 'Borrowed.csv', usecols=['foreign', 'siswati_version'])

            slang_correction_map = dict(zip(slang_data['slang'].astype(str), slang_data['meaning'].astype(str)))
            typo_correction_map = dict(zip(typo_data['typo'].astype(str), typo_data['correct_word'].astype(str)))
            borrowed_correction_map = dict(zip(borrowed_data['foreign'].astype(str), borrowed_data['siswati_version'].astype(str)))

            text = text.lower()
            text = self.remove_punctuation_marks(text)
            text = self.remove_numbers(text)
            text = self.remove_extra_spaces(text)
            text = self.remove_emojis(text)
            text = self.remove_emoticons(text)
            text = self.remove_tags(text)
            text = self.remove_links(text)
            text = self.remove_unicode_character(text)
            text = self.remove_adjacent_vowels(text)
            text = self.add_i_end(text)
            text = self.resolve_typos(text, typo_correction_map)
            text = self.resolve_slang(text, slang_correction_map)
            text = self.remove_stopwords(text)
            text = self.resolve_borrowed_words(text, borrowed_correction_map)
            return text

        except Exception:
            return text

    def remove_punctuation_marks(self, text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def remove_numbers(self, text):
        return re.sub(r'\d', '', text)

    def remove_extra_spaces(self, text):
        return ' '.join(text.split())

    def remove_emojis(self, text):
        return text.encode('ascii', 'ignore').decode('ascii')

    def remove_emoticons(self, text):
        emoticon_pattern = r'[:;=][\-\^]?[D\)\]\(\]/\\OpP]'
        return re.sub(emoticon_pattern, '', text)

    def remove_stopwords(self, text):
        words = word_tokenize(text)
        filtered_words = [word for word in words if word not in self.stopwords]
        return ' '.join(filtered_words)

    def remove_tags(self, text):
        pattern = re.compile(r'<.*?>')
        cleaned_text = re.sub(pattern, '', text)
        return cleaned_text

    def remove_links(self, text):
        url_pattern = re.compile(r'https?://\S+|www\.\S+')
        text = url_pattern.sub('', text)
        return text

    def remove_unicode_character(self, text):
        return re.sub(r'[^\x00-\x7F]+', '', text)

    def add_i_end(self, text):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        words = text.split()
        corrected_words = [word + 'i' if word[-1].lower() not in vowels else word for word in words]
        return ' '.join(corrected_words)

    def resolve_slang(self, text, slang_correction_map: dict):
        for slang, meaning in slang_correction_map.items():
            text = text.replace(slang, meaning)
        return text

    def resolve_typos(self, text, typo_correction_map: dict):
        for typo, correction in typo_correction_map.items():
            text = text.replace(typo, correction)
        return text

    def resolve_borrowed_words(self, text, borrowed_correction_map: dict):
        for borrowed, correction in borrowed_correction_map.items():
            text = text.replace(borrowed, correction)
        return text

    def remove_adjacent_vowels(self, text):
        vowels = {'a', 'e', 'i', 'o', 'u'}
        result = []
        for i in range(len(text)):
            if i == 0 or text[i] not in vowels or text[i] != text[i-1]:
                result.append(text[i])
        return ''.join(result)
