"""
Module for text cleaning.
This module provides a class and methods for preprocessing and cleaning text data, 
with specific functionalities tailored for siSwati text.
"""

import re
import string
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize

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
        '''
        Initialize some variable from the pre-processing dataset
        '''
        try:
            self.stopwords = list(set(stopwords.words('english')))
            path = '../data/'
            stop_data = pd.read_csv(path+"Stopwords.csv", usecols=['stopwords'])
            slang_data = pd.read_csv(path+'Slang.csv', usecols=['slang', 'meaning'])
            typo_data = pd.read_csv(path+'Typo.csv', usecols=['typo', 'correct_word'])
            borrowed_data = pd.read_csv(path+'Borrowed.csv', usecols=['foreign', 'siswati_version'])
            self.stopwords.extend((stop_data['stopwords'].astype(str)).to_list())
            self.slang_correction_map = dict(zip(slang_data['slang'].astype(str), slang_data['meaning'].astype(str)))
            self.typo_correction_map = dict(zip(typo_data['typo'].astype(str), typo_data['correct_word'].astype(str)))
            self.borrowed_correction_map = dict(zip(borrowed_data['foreign'].astype(str), borrowed_data['siswati_version'].astype(str)))
        except Exception:
            raise


    def clean_text(self, text: str) -> str:
        """
            Clean and preprocess text data by applying various cleaning methods.

            Args:
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
            text = text.lower()
            text = self.remove_extra_spaces(text)
            text = self.remove_links(text)
            text = self.remove_emojis(text)
            text = self.remove_emoticons(text)
            text = self.remove_tags(text)
            text = self.remove_unicode_character(text)
            text = self.remove_punctuation_marks(text)
            text = self.remove_adjacent_vowels(text)
            text = self.add_i_end(text)
            text = self.resolve_typos(text)
            text = self.resolve_slang(text)
            text = self.remove_stopwords(text)
            text = self.resolve_borrowed_words(text)
            text = self.remove_numbers(text)
            return text
        except Exception:
            raise


    def remove_punctuation_marks(self, text: str) -> str:
        try:
            return text.translate(str.maketrans('', '', string.punctuation))
        except Exception:
            raise

    def remove_numbers(self, text: str) -> str:
        try:
            return re.sub(r'\d', '', text)
        except Exception:
            raise

    def remove_extra_spaces(self, text: str) -> str:
        try:
            return ' '.join(text.split())
        except Exception:
            raise

    def remove_emojis(self, text: str) -> str:
        try:
            return text.encode('ascii', 'ignore').decode('ascii')
        except Exception:
            raise

    def remove_emoticons(self, text: str) -> str:
        try:
            emoticon_pattern = r'[:;=][\-\^]?[D\)\]\(\]/\\OpP]'
            return re.sub(emoticon_pattern, '', text)
        except Exception:
            raise

    def remove_tags(self, text: str) -> str:
        try:
            pattern = re.compile(r'<.*?>')
            cleaned_text = re.sub(pattern, '', text)
            return cleaned_text
        except Exception:
            raise

    def remove_links(self, text: str) -> str:
        try:
            url_pattern = re.compile(r'https?://\S+|www\.\S+')
            text = url_pattern.sub('', text)
            return text
        except Exception:
            raise

    def remove_unicode_character(self, text: str) -> str:
        try:
            return re.sub(r'[^\x00-\x7F]+', '', text)
        except Exception:
            raise


    def remove_stopwords(self, text: str) -> str:
        """
            Removes English and siSwati stopwords from text.
            Args:
            ----------
            text : str
                The text to be cleaned.
        """
        try:
            words = word_tokenize(text)
            filtered_words = [word for word in words if word not in self.stopwords]
            return ' '.join(filtered_words)
        except Exception:
            raise


    def add_i_end(self, text: str) -> str:
        """
            Adds the vowel 'i' at the end of words with no bowel at the end. 
            In siSwati we can never have a word which ends with no vowel.
            People, use dialect to interact with each other in social media.
            Args:
            ----------
            text : str
                The text to be cleaned.
        """
        try:
            vowels = {'a', 'e', 'i', 'o', 'u'}
            words = text.split()
            corrected_words = [word + 'i' if word[-1].lower() not in vowels else word for word in words]
            return ' '.join(corrected_words)
        except Exception:
            raise


    def resolve_slang(self, text: str) -> str:
        """
            Replaces the slang words with the corresponding siSwati word.
            Args:
            ----------
            text : str
                The text to be cleaned.
        """
        try:
            words = text.split()
            corrected_words = []
            for word in words:
                if word in self.slang_correction_map:
                    corrected_words.append(self.slang_correction_map[word])
                else:
                    corrected_words.append(word)
            return ' '.join(corrected_words)
        except Exception:
            raise


    def resolve_typos(self, text: str) -> str:
        """
            Removes English and siSwati stopwords from text.
            Args:
            ----------
            text : str
                The text to be cleaned.
        """
        try:
            words = text.split()
            corrected_words = []
            for word in words:
                if word in self.typo_correction_map:
                    corrected_words.append(self.typo_correction_map[word])
                else:
                    corrected_words.append(word)
            return ' '.join(corrected_words)
        except Exception:
            raise


    def resolve_borrowed_words(self, text: str) -> str:
        """
            Removes English and siSwati stopwords from text.
            Args:
            ----------
            text : str
                The text to be cleaned.
        """
        try:
            words = text.split()
            corrected_words = []
            for word in words:
                if word in self.borrowed_correction_map:
                    corrected_words.append(self.borrowed_correction_map[word])
                else:
                    corrected_words.append(word)
            return ' '.join(corrected_words)
        except Exception:
            raise


    def remove_adjacent_vowels(self, text: str) -> str:
        """
            Removes vowels that follow each other because in siSwati that is not the case and people
            tend to do it when they express their emotions and feelings. These removed vowels are the
            ones that are similar. 'aaaaaaaaeeeeiiiooouu' -> 'aeiou'
            Args:
            ----------
            text : str
                The text to be cleaned.
        """
        try:
            vowels = {'a', 'e', 'i', 'o', 'u'}
            result = []
            for i in range(len(text)):
                if i == 0 or text[i] not in vowels or text[i] != text[i-1]:
                    result.append(text[i])
            return ''.join(result)
        except Exception:
            raise
