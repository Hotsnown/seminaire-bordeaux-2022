from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer

operands = [
    Args(),
]

def guillemets_dans_string():
    return 'Il y a des "doubles guillemets" dans ce string.'

exo_guillemets_dans_string = ExerciseFunction(
    guillemets_dans_string,
    operands
    )

def apostrophe_dans_string():
    return "Une apostrophe peut s'inclure dans un string."

exo_apostrophe_dans_string = ExerciseFunction(
    apostrophe_dans_string,
    operands
    )

def string_multi_ligne():
    return """Ce string a été écrit sur plusieurs lignes,
      et il s'affiche sur plusieurs lignes"""

exo_string_multi_ligne = ExerciseFunction(
    string_multi_ligne,
    operands
    )

# @BEG@ name=percentages
def concat():    
    return "Hello World"
# @END@

exo_concat = ExerciseFunction(
    concat,
    operands,
    result_renderer=PPrintRenderer(width=20),
)

def formatte(nom):
    return f"Bonjour {nom} !"

noms = [
    Args("Camille"),
    Args("Charlie"),
    Args("Alix"),
    Args("Andrea"),
    Args("Noa"),
    Args("Sasha"),
]

exo_formatte = ExerciseFunction(
    formatte,
    noms,
    result_renderer=PPrintRenderer(width=20),
)