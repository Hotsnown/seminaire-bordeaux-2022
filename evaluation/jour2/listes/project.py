from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer


def remove_punct(string):

    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
   
    no_punct = ""
    for char in string:
        if char not in punctuations:
            no_punct = no_punct + char

    return no_punct

strings = [
    Args("Hello!!!, how are you? -Hope doing well.")
]

exo_remove_ponctuation = ExerciseFunction(
    remove_punct,
    strings,
)

def est_palindrome(string):
    # make it suitable for caseless comparison
    string = string.casefold()

    # reverse the string
    rev_str = reversed(string)

    # check if the string is equal to its reverse
    if list(string) == list(rev_str):
        return True
    else:
        False

strings = [
    Args("aIbohPhoBiA"),
]

exo_palindrome = ExerciseFunction(
    est_palindrome,
    strings,
)