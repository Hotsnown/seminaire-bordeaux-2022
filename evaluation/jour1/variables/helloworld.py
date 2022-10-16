from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer

# @BEG@ name=percentages
def helloworld():    
    return "Hello World"
# @END@

operands = [
    Args(),
]

exo_helloworld = ExerciseFunction(
    helloworld,
    operands,
    result_renderer=PPrintRenderer(width=20),
)