from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer

# CREATE LIST

def create_list_3(a, b, c):
    return [a, b, c]

arguments_3 = [
    Args("a", "b", "c"),
    Args(1, 2, 3)
]

exo_create_list_3 = ExerciseFunction(
    create_list_3,
    arguments_3,
)

def create_list_4(a, b, c, d):
    return [a, b, c, d]


arguments_4 = [
    Args("a", "b", "c", "d"),
    Args(1, 2, 3, 4)
]

exo_create_list_4 = ExerciseFunction(
    create_list_4,
    arguments_4,
)

def create_list_5(a, b, c, d, e):
    return [a, b, c, d, e]

arguments_5 = [
    Args("a", "b", "c", "d", "e"),
    Args(1, 2, 3, 4, 5)
]

exo_create_list_5 = ExerciseFunction(
    create_list_5,
    arguments_5,
)

# ADD LIST

def add_list(list, x):
    liste.append(x)

    # Ne rien changer après cette ligne
    return liste

arguments = [
    Args(["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre"], "décembre")
]

exo_add_list = ExerciseFunction(
    add_list,
    arguments,
)

## LENGHT

def lenght(list):
    return len(list)

arguments = [
    Args(["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"])
]

exo_lenght = ExerciseFunction(
    lenght,
    arguments,
)

def is_empty(list):
    return len(list) == 0

arguments = [
    Args([]),
    Args(["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"])
]

exo_is_empty = ExerciseFunction(
    is_empty,
    arguments,
)


## ACCESSING ITEM

def get_item(liste, x):
    return liste[x]

arguments = [
    Args(["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"], 1),
    Args(["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"], 6),
    Args(["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"], 12),
]

exo_get_item = ExerciseFunction(
    get_item,
    arguments,
)

def select_second(L):
    """Return the second element of the given list. If the list has no second
    element, return None.
    """
    if len(L) > 1:
        return L[1]

arguments = [
    Args(["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"], 1),
    Args([0, 1, 2, 3, 4])
]

exo_select_second = ExerciseFunction(
    select_second,
    arguments,
)

def get_lastitem(liste):
    return liste[-1]

arguments = [
    Args(["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]),
    Args(sorted(["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"])),
    Args(random.shuffle(["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]))
]

exo_get_lastitem = ExerciseFunction(
    get_lastitem,
    arguments,
)

def first_last(liste):
    return [liste[0], liste[-1]]

arguments = [
    Args([5, 10, 15, 20, 25])
]

exo_first_last = ExerciseFunction(
    first_last,
    arguments,
)

## LOOPING OVER LIST

def trois_existe_dans_liste(liste):
    for x in liste:
        if x == 3:
            return True
    return False

listes = [
    Args([1, 6, 3, 5, 3, 4]),
    Args([2, 4, 6, 8, 10, 12]),
    Args([1, 3, 5, 7, 9, 11]),
    Args([-1, -6, -3, -5, -3, -4]),
    Args([3, 5, 3, 9, 3, 4])
]

exo_trois_existe_dans_liste = ExerciseFunction(
    trois_existe_dans_liste,
    listes
)

def less_than_5(list):
    ret = []
    for i in list:
        if i < 5:
            ret.append(i)
    return ret
            
input_list = [
    Args([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]),
]

exo_less_than_5 = ExerciseFunction(
    less_than_5,
    input_list,
)
