from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer

# @BEG@ name=upper
def upper(string):    
    return string.upper()
# @END@

lowercase_string = [
    Args("Accessorium sequitur principale."),
    Args("Affirmanti incumbit probatio."),
    Args("Non bis in idem."),
]

exo_upper = ExerciseFunction(
    upper,
    lowercase_string,
)

# @BEG@ name=upper
def lower(string):    
    return string.lower()
# @END@

uppercase_string = [
    Args("ACCESSORIUM SEQUITUR PRINCIPALE."),
    Args("AFFIRMANTI INCUMBIT PROBATIO."),
    Args("NON BIS IN IDEM."),
]

exo_lower = ExerciseFunction(
    lower,
    uppercase_string,
)

# @BEG@ name=upper
def strip(string):    
    return string.strip()
# @END@

unstripped_string = [
    Args("    Accessorium sequitur principale."),
    Args("             Affirmanti incumbit probatio."),
    Args("   Non bis in idem."),
]

exo_stripped = ExerciseFunction(
    strip,
    unstripped_string,
)

# @BEG@ name=capitalize
def capitalize(string):    
    return string.capitalize()
# @END@

to_capitalize_string = [
    Args("accessorium sequitur principale."),
    Args("affirmanti incumbit probatio."),
    Args("non bis in idem."),
]

exo_capitalize= ExerciseFunction(
    capitalize,
    to_capitalize_string,
)

# @BEG@ name=replace
def replace(string):
    return string.replace("_", "sequitur")
# @END@

to_replace_string = [
    Args("Accessorium _ principale."),
]

exo_replace = ExerciseFunction(
    replace,
    to_replace_string,
)