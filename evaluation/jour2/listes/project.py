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
    Args("Bonjour ! !!, comment allez-vous ? -J'espรจre que รงa va bien.")
]

exo_remove_ponctuation = ExerciseFunction(
    remove_punct,
    strings,
)

def remove_emojis(string):

    emojis = "โ๐ฎ๐ซ๐ฎ๐ฃ๐ปโฝ๐ค๐โต๐๐๐๐ค๐คท๐๐๐๐๐๐๐ค๐ญ๐๐ฝโณ๐๐ฃ๐๐ช๐ฉ๐๐๐๐๐ฐ๐คต๐ซ๐ฅ๐๐ต๐"
   
    no_emojis = ""
    for char in string:
        if char not in emojis:
            no_emojis = no_emojis + char

    return no_emojis

strings = [
    Args("La loi โ๐ฎ rรฉgit l'association conjugale, en ce qui concerne les biens, ๐ซ๐ฎ๐ฃ๐ปโฝ seulement ๐ค๐ en โตโต๐บ๐ธ l'absence de conventions spรฉciales ๐๐๐ que ๐ค les รฉpoux peuvent ๐คท faire ๐๐๐ comme ils ๐ le jugent ๐ opportun, ๐ ร  condition ๐ค๐ญ que ๐ elles ๐ฝ ne soient pas โณ contraires aux bonnes ๐ mลurs ou aux dispositions suivantes ๐ฃ."),
    Args("Le prix ๐ de la vente doit ๐ช๐ฉ รชtre ๐๐ dรฉterminรฉ et dรฉsignรฉ par ๐ les parties. ๐"),
    Args("Le mariage ๐ฐ๐คต ne peut ๐ซ รชtre ๐ฅ contractรฉ avant ๐ l'รขge ๐ต de dix-huit ans rรฉvolus. ๐")
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
    Args("รฉtรฉ"),
    Args("kayak"),
    Args("antarctique"),
    Args("louer"),
    Args("gag"),
    Args("rythme"),
    Args("selles"),
    Args("radar"),
    Args("ana"),
    Args("stats"),
    Args("tรดt"),
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