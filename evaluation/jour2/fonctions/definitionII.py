
from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer
import random


def est_chiffre(string):
    return string.isdigit()

est_chiffre_arguments()

exo_est_chiffre = ExerciceFunction(
    est_chiffre,
    est_chiffre_arguments
)