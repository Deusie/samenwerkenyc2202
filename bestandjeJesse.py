import pandas as pd

def eenmethodeinbestand1():
    return "dit komt uit jesses bestandje ut methode 1"


def methodeMetReadFile():
    pokemons = pd.read_csv("Pokemon.csv")
    kolomnaam = pokemons.columns[4] 
    return kolomnaam


#methodeMetReadFile()