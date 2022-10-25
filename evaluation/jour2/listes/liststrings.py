from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer
import random

#String as lists

def première_lettre(string):
    return string[0]

première_lettre_arguments = [
    Args("Demandeur"),Args("Défendeur"),Args("Partie"),Args("Ministère public (parquet)"),Args("Tiers"),Args("Juge"),Args("Avocat"),Args("Greffier"),Args("Arbitre"),Args("Médiateur"),Args("Procureur")
]

exo_première_lettre = ExerciseFunction(
    première_lettre,
    première_lettre_arguments
)

def indexe_string(string, k):
    return string[k]

indexe_string_arguments = [
    Args("Demandeur", 0),Args("Défendeur", 1),Args("Partie", 2),Args("Ministère public (parquet)", 3),Args("Tiers", 4),Args("Juge", 5),Args("Avocat", 6),Args("Greffier", 7),Args("Arbitre", 8),Args("Médiateur", 9),Args("Procureur", 10)
]

exo_indexe_string = ExerciseFunction(
    indexe_string,
    indexe_string_arguments
)

def longueur_string(string):
    return len(string)

longueur_string_arguments = [
    Args("Demandeur"),Args("Défendeur"),Args("Partie"),Args("Ministère public (parquet)"),Args("Tiers"),Args("Juge"),Args("Avocat"),Args("Greffier"),Args("Arbitre"),Args("Médiateur"),Args("Procureur")
]

exo_longueur_string = ExerciseFunction(
    longueur_string,
    longueur_string_arguments
)

def loop_over_string(string, fonction):
    ret = []
    for letter in string:
        ret.append(fonction(letter))
    return ret

loop_over_string_arguments = [
    Args("Demandeur", isalpha),Args("Défendeur", isdigit),Args("Partie", isalpha),Args("Ministère public (parquet)", isspace),Args("Tiers", isupper),Args("Juge", isupper),Args("Avocat", islower),Args("Greffier", islower),Args("Arbitre", isalnum),Args("Médiateur", isalnum),Args("Procureur", isupper)
]

exo_loop_over_string = ExerciseFunction(
    loop_over_string,
    loop_over_string_arguments
)

def in_operator(string, mots):
    return string in mots

in_operator_arguments = [
    Args("Cour de cassation",  ["Demandeur","Défendeur","Partie","Ministère public (parquet)","Tiers","Juge","Avocat","Arbitre","Médiateur","Procureur","Greffier"]),
    Args("Conseil constitutionnel",  ["Demandeur","Défendeur","Partie","Ministère public (parquet)","Tiers","Juge","Avocat","Arbitre","Médiateur","Procureur","Greffier"]),
    Args("Demandeur",  ["Demandeur","Défendeur","Partie","Ministère public (parquet)","Tiers","Juge","Avocat","Arbitre","Médiateur","Procureur","Greffier"]),
    Args("Tribunal",  ["Demandeur","Défendeur","Partie","Ministère public (parquet)","Tiers","Juge","Avocat","Arbitre","Médiateur","Procureur","Greffier"]),
    Args("Défendeur",  ["Demandeur","Défendeur","Partie","Ministère public (parquet)","Tiers","Juge","Avocat","Arbitre","Médiateur","Procureur","Greffier"]),
    Args("Conseil d'État",  ["Demandeur","Défendeur","Partie","Ministère public (parquet)","Tiers","Juge","Avocat","Arbitre","Médiateur","Procureur","Greffier"]),
    Args("Partie",  ["Demandeur","Défendeur","Partie","Ministère public (parquet)","Tiers","Juge","Avocat","Arbitre","Médiateur","Procureur","Greffier"]),
    Args("Ministère public (parquet)",  ["Demandeur","Défendeur","Partie","Ministère public (parquet)","Tiers","Juge","Avocat","Arbitre","Médiateur","Procureur","Greffier"]),
    Args("Tiers",  ["Demandeur","Défendeur","Partie","Ministère public (parquet)","Tiers","Juge","Avocat","Arbitre","Médiateur","Procureur","Greffier"]),
    Args("Cour d'appel",  ["Demandeur","Défendeur","Partie","Ministère public (parquet)","Tiers","Juge","Avocat","Arbitre","Médiateur","Procureur","Greffier"]),
]

exo_in_operator = ExerciseFunction(
    in_operator,
    in_operator_arguments
)

#Split

def split_espace(text):
    return text.split()

arguments = [
    Args("Accessorium sequitur principale."),
    Args("Affirmanti incumbit probatio."),
    Args("Non bis in idem."),
]

exo_split_espace = ExerciseFunction(
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

exo_split_douple_point = ExerciseFunction(
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


exo_split_articles = ExerciseFunction(
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

exo_liste_vers_string_avec_espaces = ExerciseFunction(
    liste_vers_string_avec_espaces,
    arguments
)

def liste_vers_string_avec_virgules(liste):
    return "Les articles sur la responsabilité contractuelle sont :" + ", ".join(liste)

arguments = [
    Args(["Article 1240", "Article 1241", "Article 1242", "Article 1243", "Article 1244" ])
]

exo_liste_vers_string_avec_virgules = ExerciseFunction(
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

exo_liste_vers_string_avec_retour_ligne = ExerciseFunction(
    liste_vers_string_avec_retour_ligne,
    arguments
)