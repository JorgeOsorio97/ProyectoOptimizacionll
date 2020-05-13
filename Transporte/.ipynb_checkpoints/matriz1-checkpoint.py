import numpy as np
from random import *

fil=int (input('Inserte el número de filas: '))
col=int (input('Inserte el número de columnas: '))


matrix = np.random.randint(1, 15, size=(fil, col))
print("La matriz: \n")
print (matrix)
print("\n")

minimo=matrix.min(1);

print("Lós términos minimos por renglón son: \n")
print (minimo)
print("\n")


matrix2=np.transpose(matrix)-minimo;
matrix21=np.transpose(matrix2)
print (matrix21)
print("\n")

minimo2=matrix21.min(0);

print("Lós términos minimos por columna son: \n")
print(minimo2)
print("\n")

matrix3=matrix21-minimo2;
print (matrix3)
print("\n")

for f in range (fil):
    for c in range (col):
        print("logical",(matrix3[:,c]==0))
        print("logical_len",len(matrix3[:,c]==0))
        print("logical_filter",(matrix3[matrix3[:,c]==0]))
        print("logical_filter_len",len(matrix3[matrix3[:,c]==0]))
        matrix3=matrix3[np.logical_not(matrix3[:,c]==0)]
print (matrix3)

"""
boolarr=(matrix3>0)
print (boolarr[:,boolarr[1]!=False])"""