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
    Args("Bonjour ! !!, comment allez-vous ? -J'espère que ça va bien.")
]

exo_remove_ponctuation = ExerciseFunction(
    remove_punct,
    strings,
)

def remove_emojis(string):

    emojis = "⛔👮🚫🎮🚣🏻⛽😤👐⛵👉😎👈🤔🤷👊📝📓🙉👀👗🤔💭👋🏽⏳😜👣🔖💪😩🐝🐝😈🎉👰🤵🚫🥖😂👵🔞"
   
    no_emojis = ""
    for char in string:
        if char not in emojis:
            no_emojis = no_emojis + char

    return no_emojis

strings = [
    Args("La loi ⛔👮 régit l'association conjugale, en ce qui concerne les biens, 🚫🎮🚣🏻⛽ seulement 😤👐 en ⛵⛵🇺🇸 l'absence de conventions spéciales 👉😎👈 que 🤔 les époux peuvent 🤷 faire 👊📝📓 comme ils 🙉 le jugent 👀 opportun, 👗 à condition 🤔💭 que 👋 elles 🏽 ne soient pas ⏳ contraires aux bonnes 😜 mœurs ou aux dispositions suivantes 👣."),
    Args("Le prix 🔖 de la vente doit 💪😩 être 🐝🐝 déterminé et désigné par 😈 les parties. 🎉"),
    Args("Le mariage 👰🤵 ne peut 🚫 être 🥖 contracté avant 😂 l'âge 👵 de dix-huit ans révolus. 🔞")
]

exo_remove_emojis = ExerciseFunction(
    remove_emojis,
    strings,
)

def inverser_string(string):
    return "".join(reversed(string))

strings = [
    Args("Accessorium sequitur principale."),
    Args("Affirmanti incumbit probatio."),
    Args("Non bis in idem."),
]

exo_inverser_string = ExerciseFunction(
    inverser_string,
    strings
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
        return False

strings = [
    Args("reifier"),
    Args("shahs"),
    Args("pyramide"),
    Args("horizon"),
    Args("essayasse"),
    Args("coffre"),
    Args("fugace"),
    Args("solos"),
    Args("été"),
    Args("kayak"),
    Args("antarctique"),
    Args("louer"),
    Args("gag"),
    Args("rythme"),
    Args("selles"),
    Args("radar"),
    Args("ana"),
    Args("stats"),
    Args("tôt"),
    Args("coloc"),
    Args("verdure"),
    Args("snobons"),
    Args("narine"),
    Args("elle"),
    Args("brouette"),
    Args("aviva"),
    Args("sexes"),
    Args("pep"),
]

exo_palindrome = ExerciseFunction(
    est_palindrome,
    strings,
)