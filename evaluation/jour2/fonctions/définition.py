from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer
import random

def plus_deux(x):
    return x + 2

arguments = [
    Args(0),
    Args(1),
    Args(2),
    Args(3),
    Args(4),
]

exo_plus_deux = ExerciceFunction(
    plus_deux,
    arguments
)

def est_chiffre(string):
    return string.isdigit()

est_chiffre_arguments=[
    Args(0),
    Args("Accessorium sequitur principale."),
    Args(1),
    Args("Affirmanti incumbit probatio."),
    Args(9),
    Args("Non bis in idem."),

]

exo_est_chiffre = ExerciceFunction(
    est_chiffre,
    est_chiffre_arguments
)