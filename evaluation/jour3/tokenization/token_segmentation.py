from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer
import random

def tokenize_by_space(text):
    return text.split(" ")

arguments = [
    Args("accessorium sequitur principale."),
    Args("affirmanti incumbit probatio."),
    Args("non bis in idem."),
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

exo_tokenization_en = ExerciseFunction(
    tokenization_en,
    arguments,
)

def tokenization_fr(text):
    return word_tokenize(text, language="french")

content_french = [
        Args("Article 1240"),
        Args("Tout fait quelconque de l'homme, qui cause à autrui un dommage, oblige celui par la faute duquel il est arrivé à le réparer."),
        Args("Article 1241"),
        Args("Chacun est responsable du dommage qu'il a causé non seulement par son fait, mais encore par sa négligence ou par son imprudence."),
        Args("Article 1242"),
        Args("On est responsable non seulement du dommage que l'on cause par son propre fait, mais encore de celui qui est causé par le fait des personnes dont on doit répondre, ou des choses que l'on a sous sa garde."),
        Args("Article 1243"),
        Args("Le propriétaire d'un animal, ou celui qui s'en sert, pendant qu'il est à son usage, est responsable du dommage que l'animal a causé, soit que l'animal fût sous sa garde, soit qu'il fût égaré ou échappé."),
        Args("Article 1244"),
        Args("Le propriétaire d'un bâtiment est responsable du dommage causé par sa ruine, lorsqu'elle est arrivée par une suite du défaut d'entretien ou par le vice de sa construction."),
    ]

exo_tokenization_fr = ExerciseFunction(
    tokenization_fr,
    content_french,
)