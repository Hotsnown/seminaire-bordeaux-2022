from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer

# @BEG@ name=tva
def tva(prix_brut, taux_tva, quantité):    
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
def dévolution(actif, passif, nombre_descendants, quotité_disponible):    
    return ((actif - passif) * quotité_disponible) / nombre_descendants
# @END@

dévolution_arguments = [
    Args(10_000, 3_000, 0.9, 3),
    ]

exo_dévolution = ExerciseFunction(
    dévolution,
    dévolution_arguments,
    result_renderer=PPrintRenderer(width=20),
)

# @BEG@ name=tva
def remise(prix, quantité, taux_remise, retenus):    
    return ((prix * taux_remise) * quantité) - retenus
# @END@

remise_arguments = [
    
    ]

exo_remise = ExerciseFunction(
    remise,
    tva_arguments,
    result_renderer=PPrintRenderer(width=20),
)