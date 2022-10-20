from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer

# @BEG@ name=divide
def est_positif(x):  
    if x > 0:
        return "Positif"
    else:
        return "Négatif"
# @END@

chiffres = [
    Args(-100),
    Args(-20),
    Args(1),
    Args(10),
    Args(1000)
]

exo_est_positif = ExerciseFunction(
    est_positif,
    chiffres,
    result_renderer=PPrintRenderer(width=20),
)

def est_pair(x):
    if (x % 2) == 0:
        return "Pair"
    else:
        return "Impair"

chiffres = [
    Args(-4),
    Args(-3),
    Args(0),
    Args(1),
    Args(100),
    Args(87756)
]

exo_est_pair = ExerciseFunction(
    est_pair,
    chiffres,
    result_renderer=PPrintRenderer(width=20),
)

def est_bissextile(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return "Bissextile"
            else:
                return "Normal"
        else:
            return "Bissextile"
    else:
        return "Normal"

années = [
    Args(2016),
    Args(2017),
    Args(2018),
    Args(2019),
    Args(2020),
    Args(2021),
    Args(2022),
    Args(2023),
    Args(2024),
]

exo_est_bissextile = ExerciseFunction(
    est_bissextile,
    années
)