from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer

# @BEG@ name=project
def identifiant(defendant, plaintiff):
    defendant = defendant.strip().capitalize().replace("_", "Loring")
    plaintiff = plaintiff.strip().capitalize().replace("_", "Owners")

    return defendant + " " + "v." + " " + plaintiff
# @END@

operands = [
    Args("people", "      smith"),
    Args("    luther", "the Master & _ of Ship Apollo"),
    Args(" ladd", "      stevenson"),
    Args("_", "illsley"),
]

exo_identifiant = ExerciseFunction(
    identifiant,
    operands,
)