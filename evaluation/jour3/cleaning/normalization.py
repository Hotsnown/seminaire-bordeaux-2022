from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer
import random

# clean_word_list

import nltk
import pandas as pd
from nltk.stem import PorterStemmer

# init stemmer
porter_stemmer=PorterStemmer()

def stemmer(word):
    return porter_stemmer.stem(word=word)

arguments = [
    Args("connect"),
    Args("connected"),
    Args("connection"),
    Args("connections"),
    Args("connects"),
]

exo_stemmer = ExerciseFunction(
    stemmer,
    arguments,
)

# clean_word_list

from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')

# init lemmatizer
lemmatizer = WordNetLemmatizer()

def lemmatize(word):
    return lemmatizer.lemmatize(word=word,pos='v')

arguments = [
    Args("trouble"),
    Args("troubling"),
    Args("troubled"),
    Args("troubles"),
    Args("goose"),
    Args("geese")
]

exo_lemmatize = ExerciseFunction(
    lemmatize,
    arguments,
)

# remove special characters

def clean(sentence):
    return ' '.join(sentence.split())

arguments = [
    Args(' this is \n a sample\t sentence. '),
]

exo_clean = ExerciseFunction(
    clean,
    arguments,
)

