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
    Args(200, 0.2, 4),
    Args(1000, 0.05, 2)
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
    Args(10_000, 3_000, 0.9, 3),
    ]

exo_dévolution = ExerciseFunction(
    dévolution,
    dévolution_arguments,
    result_renderer=PPrintRenderer(width=20),
)