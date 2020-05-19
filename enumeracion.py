import numpy as np
from random import *
import itertools as it

seed(1)
np.random.seed(1)

variables=0
res=0
restricciones=[]
funobj=[]
condicional=[]

def input_int(message=""):
    return int(input(message))


    
print("¿Que quieres hacer?")
print("Maximizar: ingresa 1")
print("Minimizar: ingresa 2")
tipo = input("")

variables = input_int("¿Cuantas variables tiene el problema?\n")
res = input_int("¿Cuantas restricciones tiene el problema?\n")

print("Llenemos los coeficientes de la funcion objetivo")
for i in np.arange( variables):
    funobj.append(
    input_int("Dime el coeficiente de la variable x{}: ".format(i)))

print("Es importante que debemos tener todas nuestras reestriciones de la forma:")
print("Sum(xi*restricion_i) <= b")

for i in np.arange(res):
    temp_rest = []
    temp_b = 0
    for j in np.arange( variables):
        temp_rest.append(input_int(
        "Dime el coeficiente de la variable x{} en la reestricción {}: ".format(j, i)))
    temp_b = input_int(
        "Dime el valor b de la reestricción {}: ".format(i))

    print("La reestricción queda: {} {} {}".format(
        "".join([" ({})x{} +".format(val, idx)
            for idx, val in enumerate(temp_rest)])[:-1],
        "<=",
        temp_b
    ))
    restricciones.append(temp_rest)
    condicional.append(temp_b)
    
funobj = np.array(funobj)
restricciones = np.array(restricciones)
condicional = np.array(condicional)    


print('Max Z=', funobj,'\n')
print('s.a\n')

print(restricciones,condicional)

binarios=np.array(list(it.product([0, 1], repeat=variables)))

z=np.array(funobj*binarios);

divres=np.split(restricciones, res) 

rs=np.array(divres*binarios);

sumz=[sum(z[i]) for i in range (len(z))]
sumz=np.array(sumz)
print (sumz)

lista_vacia_grande=[]  
for j in range(len(rs)):
    lista_vacia=[]
    lista_vacia_grande.append(lista_vacia)
    for l in range(len(rs[j])):
        sumrs=sum(rs[j][l])
        np.array(sumrs)
        print (sumrs,'<=', condicional[j])
        
        candidatos=np.all(sumrs <= condicional[j])
        lista_vacia.append(candidatos)
    print(lista_vacia)
    
lista_vacia_grande=np.array(lista_vacia_grande)
lista_vacia_grande=np.transpose(lista_vacia_grande)


lista_vacia2=[]
for j in lista_vacia_grande:
    lista_vacia2.append(np.all(j==True))


maximo=sumz[lista_vacia2].max() if (tipo==1) else sumz[lista_vacia2].min()
print(maximo)

index_max=np.where(sumz[lista_vacia2]==maximo)[0][0]
print ((binarios[lista_vacia2][index_max]))
