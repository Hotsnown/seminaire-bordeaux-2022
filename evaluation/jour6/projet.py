from nbautoeval import ExerciseFunction, Args
from nbautoeval import CallRenderer, PPrintRenderer

# @BEG@ name=project
def identifiant(cour, date, numero):
    cour = cour.replace("paris", "Paris")
    cour = cour.replace("Pris", "Paris")

    date = date.strip()

    return cour + " " + date + " " + numero    
# @END@

operands = [
    Args("CA Paris","   10 janvier 2018","n° 15/17379"),
    Args("CA Paris","12 janvier 2018","n° 15/20452*"),
    Args("CA Paris","12 janvier 2018","n° 15/22694"),
    Args("CA Paris","17 janvier 2018","n° 15/17101"),
    Args("CA paris","17 janvier 2018","n° 15/17249"),
    Args("CA Paris","18 janvier 2018","n° 15/13129"),
    Args("CA Pris","19 janvier 2018","n° 15/10939"),
    Args("CA Paris","   19 janvier 2018","n° 17/11354"),
    Args("CA Paris","19 janvier 2018","n° 15/23767"),
    Args("CA Paris","   25 janvier 2018","n° 15/16368"),
    Args("CA paris","1er février 2018","n° 15/13726"),
    Args("CA Paris","7 février 2018	","n° 12/07788"),
    Args("CA Pris","7 février 2018	","n° 15/05318"),
    Args("CA Paris","7 février 2018	","n° 16/00080"),
    Args("CA paris","8 février 2018	","n° 15/12544"),
    Args("Cass. com.","14 février 2018","n° 16-24667"),
    Args("CA Paris","15 février 2018","n° 15/10066"),
    Args("CA paris","15 février 2018","n° 15/13088"),
    Args("CA Pris","    21 février 2018","n° 15/05499"),
    Args("CA Paris","21 février 2018","n° 15/06721"),
    Args("CA Paris","21 février 2018","n° 15/08409"),
]

exo_identifiant = ExerciseFunction(
    identifiant,
    operands,
)