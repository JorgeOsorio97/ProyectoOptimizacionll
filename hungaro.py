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
                "Dime el valor de la posicion {} de la fila {}: ".format(j,i)))

        
        matriz.append(temp_rest)
    matriz=np.array(matriz)

    print("La matriz queda: \n", matriz)

    minimo=matriz.min(1);

    print("Lós términos minimos por renglón son: \n")
    print (minimo)
    print("\n")


    matrix2=np.transpose(matriz)-minimo;
    matrix21=np.transpose(matrix2)
    print (matrix21)
    print("\n")

    minimo2=matrix21.min(0);

    print("Los terminos minimos por columna son: \n")
    print(minimo2)
    print("\n")

    matrix3=matrix21-minimo2;
    print (matrix3)
    print("\n")
    
    ceros_filas = []
    for f in range (len(matrix3)):
        lista_vacia=[]
        lista_taches=[]
        lista_taches.append(lista_vacia)
        for c in range (len(matrix3[f])):
            candidatos = matrix3[f][c] == 0
            lista_vacia.append(candidatos)
        x=lista_vacia.count(True)
        lista_vacia=np.array(lista_vacia) 
        ceros_filas.append(x)
        print ("listavacia", lista_vacia)
        print(x)
    print(ceros_filas)

    ceros_cols = []
    for c in range(len(matrix3)):
        lista_vacia=[]
        lista_taches=[]
        lista_taches.append(lista_vacia)
        for f in range (len(matrix3[:,c])):
            candidatos = matrix3[f][c] == 0
            lista_vacia.append(candidatos)
        x=lista_vacia.count(True)
        lista_vacia=np.array(lista_vacia) 
        ceros_cols.append(x)
        print ("listavacia", lista_vacia)
        print(x)
    print(ceros_cols)
    
    asignaciones=[]
    for j in lista_vacia:
        asignaciones.append(np.all(j == True))
    print()
    
        


if __name__ == "__main__":
    hungaro()