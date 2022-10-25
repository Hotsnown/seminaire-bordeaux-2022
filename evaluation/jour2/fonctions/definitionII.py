from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer
import random

def max_entre_3(x):
    return x + 2

arguments = [
    Args(0, 1, 2),
    Args(1, -6, 100),
    Args(3, 2, 1),
]

exo_max_entre_3 = ExerciseFunction(
    max_entre_3,
    arguments
)

def est_pair(x):
    if x%2==0:
        return True
    else:
        return False

arguments = [
   Args(0),
   Args(1),
   Args(2),
   Args(3),
   Args(4),
   Args(5),
   Args(6),
]

exo_max_entre_3 = ExerciseFunction(
    est_pair,
    arguments
)