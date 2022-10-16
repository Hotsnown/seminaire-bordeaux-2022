from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer
import random

def end_of_sentence_marker(character):
    if character == "?": return True
    return False

markers = [
    Args("?"),
    Args("."),
    Args("a")
]

exo_end_of_sentence_marker = ExerciseFunction(
    end_of_sentence_marker,
    markers,
)

def split_sentences(text):

    sentences = []
    start = 0
    for end, character in enumerate(text):
        if end_of_sentence_marker(character):
            sentence = text[start: end + 1]
            sentences.append(sentence)
            start = end + 1
    return sentences

text = [
    Args("This is a sentence. Should we seperate it from this one?")
]

exo_split_sentences = ExerciseFunction(
    split_sentences,
    text,
)