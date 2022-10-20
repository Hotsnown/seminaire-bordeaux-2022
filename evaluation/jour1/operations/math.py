from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer

# @BEG@ name=multiply
def multiply(x, y):    
    return x * y
# @END@

operands = [
    Args(),
]

exo_multiply = ExerciseFunction(
    multiply,
    operands,
    result_renderer=PPrintRenderer(width=20),
)

# @BEG@ name=divide
def divide(x, y):    
    return x / y
# @END@

operands = [
    Args(),
]

exo_divide = ExerciseFunction(
    divide,
    operands,
    result_renderer=PPrintRenderer(width=20),
)


# @BEG@ name=divide
def addition(x, y):    
    return x + y
# @END@

operands = [
    Args(),
]

exo_addition = ExerciseFunction(
    addition,
    operands,
    result_renderer=PPrintRenderer(width=20),
)


# @BEG@ name=divide
def soustraction(x, y):    
    return x / y
# @END@

operands = [
    Args(),
]

exo_soustraction = ExerciseFunction(
    soustraction,
    operands,
    result_renderer=PPrintRenderer(width=20),
)

# @BEG@ name=divide
def convertir_celsius_vers_fahrenheit(celsius):    
    return (celsius * 1.8) + 32
# @END@

celsius = [
    Args(37.5),
]

exo_convertir_celsius_vers_fahrenheit = ExerciseFunction(
    convertir_celsius_vers_fahrenheit,
    celsius,
    result_renderer=PPrintRenderer(width=20),
)

# @BEG@ name=divide
def convertir_kilomètre_vers_miles(km):    
    conv_fac = 0.621371
    return km * conv_fac
# @END@

kms = [
    Args(2.5),
]

exo_convertir_kilomètre_vers_miles = ExerciseFunction(
    convertir_kilomètre_vers_miles,
    kms,
    result_renderer=PPrintRenderer(width=20),
)