from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer
import random

#Split

def split_espace(text):
    return text.split()

arguments = [
    Args("Accessorium sequitur principale."),
    Args("Affirmanti incumbit probatio."),
    Args("Non bis in idem."),
]

exo_split_espace = ExerciceFunction(
    split_espace,
    arguments
)

def split_douple_point(text):
    return text.split(":")

arguments = [
    Args("20:00"),
    Args("8:45"),
    Args("18:30"),
]

exo_split_douple_point = ExerciceFunction(
    split_douple_point,
    arguments
)

def split_articles(text):
    texts = text.split("\n")
    result = []
    for item in texts:
        if item.startswith("Article"):
            result.append(item)
    return result

arguments = [
    Args(
"""Article 1240
Tout fait quelconque de l'homme, qui cause à autrui un dommage, oblige celui par la faute duquel il est arrivé à le réparer.
Article 1241
Chacun est responsable du dommage qu'il a causé non seulement par son fait, mais encore par sa négligence ou par son imprudence.
Article 1242
On est responsable non seulement du dommage que l'on cause par son propre fait, mais encore de celui qui est causé par le fait des personnes dont on doit répondre, ou des choses que l'on a sous sa garde.
Article 1243
Le propriétaire d'un animal, ou celui qui s'en sert, pendant qu'il est à son usage, est responsable du dommage que l'animal a causé, soit que l'animal fût sous sa garde, soit qu'il fût égaré ou échappé.
Article 1244
Le propriétaire d'un bâtiment est responsable du dommage causé par sa ruine, lorsqu'elle est arrivée par une suite du défaut d'entretien ou par le vice de sa construction."""),
]


exo_split_articles = ExerciceFunction(
    split_articles,
    arguments
)

# JOIN

def liste_vers_string_avec_espaces(liste):
    return " ".join(liste)

arguments = [
    Args(['Tout', 'fait', 'quelconque', 'de', "l'homme,", 'qui', 'cause', 'à', 'autrui', 'un', 'dommage,', 'oblige', 'celui', 'par', 'la', 'faute', 'duquel', 'il', 'est', 'arrivé', 'à', 'le', 'réparer.']),
    Args(['Chacun', 'est', 'responsable', 'du', 'dommage', "qu'il", 'a', 'causé', 'non', 'seulement', 'par', 'son', 'fait,', 'mais', 'encore', 'par', 'sa', 'négligence', 'ou', 'par', 'son', 'imprudence.']),
    Args(['On', 'est', 'responsable', 'non', 'seulement', 'du', 'dommage', 'que', "l'on", 'cause', 'par', 'son', 'propre', 'fait,', 'mais', 'encore', 'de', 'celui', 'qui', 'est', 'causé', 'par', 'le', 'fait', 'des', 'personnes', 'dont', 'on', 'doit', 'répondre,', 'ou', 'des', 'choses', 'que', "l'on", 'a', 'sous', 'sa', 'garde.']),
    Args(['Le', 'propriétaire', "d'un", 'animal,', 'ou', 'celui', 'qui', "s'en", 'sert,', 'pendant', "qu'il", 'est', 'à', 'son', 'usage,', 'est', 'responsable', 'du', 'dommage', 'que', "l'animal", 'a', 'causé,', 'soit', 'que', "l'animal", 'fût', 'sous', 'sa', 'garde,', 'soit', "qu'il", 'fût', 'égaré', 'ou', 'échappé.']),
    Args(['Le', 'propriétaire', "d'un", 'bâtiment', 'est', 'responsable', 'du', 'dommage', 'causé', 'par', 'sa', 'ruine,', "lorsqu'elle", 'est', 'arrivée', 'par', 'une', 'suite', 'du', 'défaut', "d'entretien", 'ou', 'par', 'le', 'vice', 'de', 'sa', 'construction.'])
]

exo_liste_vers_string_avec_espaces = ExerciceFunction(
    liste_vers_string_avec_espaces,
    arguments
)

def liste_vers_string_avec_virgules(liste):
    return "Les articles sur la responsabilité contractuelle sont :" + ", ".join(liste)

arguments = [
    Args(["Article 1240", "Article 1241", "Article 1242", "Article 1243", "Article 1244" ])
]

exo_liste_vers_string_avec_virgules = ExerciceFunction(
    liste_vers_string_avec_virgules,
    arguments
)

def liste_vers_string_avec_retour_ligne(liste):
    return "\n".join(liste)

arguments = [
    Args([
        "Article 1240",
        "Tout fait quelconque de l'homme, qui cause à autrui un dommage, oblige celui par la faute duquel il est arrivé à le réparer.",
        "Article 1241",
        "Chacun est responsable du dommage qu'il a causé non seulement par son fait, mais encore par sa négligence ou par son imprudence.",
        "Article 1242",
        "On est responsable non seulement du dommage que l'on cause par son propre fait, mais encore de celui qui est causé par le fait des personnes dont on doit répondre, ou des choses que l'on a sous sa garde.",
        "Article 1243",
        "Le propriétaire d'un animal, ou celui qui s'en sert, pendant qu'il est à son usage, est responsable du dommage que l'animal a causé, soit que l'animal fût sous sa garde, soit qu'il fût égaré ou échappé.",
        "Article 1244",
        "Le propriétaire d'un bâtiment est responsable du dommage causé par sa ruine, lorsqu'elle est arrivée par une suite du défaut d'entretien ou par le vice de sa construction.",
    ])
]

exo_liste_vers_string_avec_retour_ligne = ExerciceFunction(
    liste_vers_string_avec_retour_ligne,
    arguments
)