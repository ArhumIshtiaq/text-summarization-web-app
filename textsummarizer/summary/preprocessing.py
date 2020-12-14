import re
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


Stopwords = set(stopwords.words('english'))
wordlemmatizer = WordNetLemmatizer()


def remove_special_characters(text):
    regex = r'[^a-zA-Z0-9\s\n]'
    text = re.sub(regex, '', text)
    return text


def preprocess(text):
    text = remove_special_characters(str(text))
    text = re.sub(r'\d+', '', text)
    tokenized_words_with_stopwords = word_tokenize(text)
    tokenized_words = [
        word for word in tokenized_words_with_stopwords if word not in Stopwords]
    tokenized_words = [word for word in tokenized_words if len(word) > 1]
    tokenized_words = [word.lower() for word in tokenized_words]

    return tokenized_words
