import numpy as np
from random import *
import itertools as it

seed(1)
np.random.seed(1)


def input_int(message=""):
    return int(input(message))


def hungaro():
    filas=0
    columnas=0

    matriz=[]

    filas = input_int("¿Cuantas filas tiene el problema?\n")
    columnas = input_int("¿Cuantas columnas tiene el problema?\n")
    for i in np.arange(filas):
        temp_rest = []

        for j in np.arange(columnas):
            temp_rest.append(input_int(
                "Dime el valor de la posicion {}: ".format(i)))

        
        matriz.append(temp_rest)
        matriz=np.array(matriz)
    print("La matriz queda: \n", matriz)


if __name__ == "__main__":
    hungaro()