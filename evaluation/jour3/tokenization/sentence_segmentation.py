from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer
import random

from nltk.tokenize import sent_tokenize

# ENG SENT TOKEN

def sent_tokenization_en(text):
    return sent_tokenize(text)

arguments = [
    Args('''
    Joe waited for the train. The train was late. 
    Mary and Samantha took the bus. 
    I looked for Mary and Samantha at the bus station.
    '''),
]

exo_sent_tokenization_en = ExerciseFunction(
    sent_tokenization_en,
    arguments,
)

# FR SENT TOKEN

def sent_tokenization_fr(text):
    return sent_tokenize(text, language='german')

arguments = [
    Args('''
    NLTK ist Open Source Software. Der Quellcode wird unter den Bedingungen der Apache License Version 2.0 vertrieben.  
    Die Dokumentation wird unter den Bedingungen der Creative Commons-Lizenz Namensnennung - Nicht kommerziell - Keine 
    abgeleiteten Werke 3.0 in den Vereinigten Staaten verteilt.
    '''),
]

exo_sent_tokenization_fr = ExerciseFunction(
    sent_tokenization_fr,
    arguments,
)

# Tokenization Sentence Wise

from nltk.tokenize import sent_tokenize, word_tokenize

def sent_by_word(text):
    return [word_tokenize(t) for t in sent_tokenize(text)]

arguments = [
    Args("Joe waited for the train. The train was late. Mary and Samantha took the bus. I looked for Mary and Samantha at the bus station."),
]

exo_sent_by_word = ExerciseFunction(
    sent_by_word,
    arguments,
)

# 

import nltk.data
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

def ex_8(text):
    return '\n==============\n'.join(sent_detector.tokenize(text.strip()))

arguments = [Args('''
Mr. Smith waited for the train. The train was late.
Mary and Samantha took the bus. I looked for Mary and
Samantha at the bus station.
''')]

exo_8 = ExerciseFunction(
    ex_8,
    arguments,
)