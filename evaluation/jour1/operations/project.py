from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer

# @BEG@ name=tva
def tva(prix_brut, produit, quantité):
    taux_tva = 0.20
    if produit == "électricité" or produit == "hébergement": taux_tva = 0.10
    if produit == "alimentaire": taux_tva = 0.055
    return (prix_brut * taux_tva) * quantité
# @END@

tva_arguments = [
    Args(200, "jouets", 4),
    Args(50, "électricité", 1),
    Args(25, "électricité", 2),
    Args(50, "alcool", 1),
    Args(330_000,  "hébergement", 1)
    ]

exo_tva = ExerciseFunction(
    tva,
    tva_arguments,
    result_renderer=PPrintRenderer(width=20),
)

# @BEG@ name=tva
def dévolution(actif, passif, nombre_descendants, libéralités):    
    return ((actif - passif) - libéralités) / nombre_descendants
# @END@

dévolution_arguments = [
    Args(10_000, 3_000, 3, 1_000),
    Args(100_000, 45_000, 1, 3_000),
    Args(30_000, 1_000, 4, 2_000),
    Args(70_000, 3_000, 3, 2_000),
    Args(10_000, 3_000, 4, 1_000),
    ]

exo_dévolution = ExerciseFunction(
    dévolution,
    dévolution_arguments,
    result_renderer=PPrintRenderer(width=20),
)