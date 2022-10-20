from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer
import random

def tokenize_by_space(text):
    return text.split(" ")

arguments = [
    Args("qzdqzd  qzdqzdq ")
]

exo_tokenize_by_space = ExerciseFunction(
    tokenize_by_space,
    arguments
)


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

def tokenization_fr(text):
    return word_tokenize(text, language="french")

content_french = [
    Args("Les astronomes amateurs jouent également un rôle important en recherche; les plus sérieux participant couramment au suivi d'étoiles variables, à la découverte de nouveaux astéroïdes et de nouvelles comètes, etc."), 
    Args('Séquence vidéo.'), 
    Args("John Richard Bond explique le rôle de l'astronomie.")
    ]

exo_tokenize_fr = ExerciseFunction(
    tokenization_fr,
    content_french,
)