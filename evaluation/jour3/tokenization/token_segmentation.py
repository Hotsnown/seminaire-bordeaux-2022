from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer
import random

from nltk.tokenize import word_tokenize

# ENG SENT TOKEN

def tokenization_en(text):
    return word_tokenize(text)

arguments = [
    Args('''
    Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station.
    '''),
]

exo_tokenize_en = ExerciseFunction(
    tokenization_en,
    arguments,
)

from nltk.tokenize import WordPunctTokenizer

def tokenize_by_punct(text):
    return WordPunctTokenizer().tokenize(text)

arguments = [
    Args("Reset your password if you just can't remember your old one."),
]

exo_tokenize_by_punct = ExerciseFunction(
    tokenize_by_punct,
    arguments,
)
