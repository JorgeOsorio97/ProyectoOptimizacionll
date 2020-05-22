import numpy as np
from random import *
import itertools as it

seed(1)
np.random.seed(1)


def input_int(message=""):
    return int(input(message))


def enumeracion():
    variables = 0

    res = 0
    restricciones = []
    funobj = []
    condicional = []

    print("¿Que quieres hacer?")
    print("Maximizar: ingresa 1")
    print("Minimizar: ingresa 2")
    tipo = input_int("")

    variables = input_int("¿Cuantas variables tiene el problema?\n")
    res = input_int("¿Cuantas restricciones tiene el problema?\n")

    print("Llenemos los coeficientes de la funcion objetivo")
    for i in np.arange(variables):
        funobj.append(
            input_int("Dime el coeficiente de la variable x{}: ".format(i)))

    print("Es importante que debemos tener todas nuestras reestriciones de la forma:")
    print("Sum(xi*restricion_i) <= b")

    for i in np.arange(res):
        temp_rest = []
        temp_b = 0
        for j in np.arange(variables):
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
   
    binarios = np.array(list(it.product([0, 1], repeat=variables)))

    z = np.array(funobj*binarios)

    divres = np.split(restricciones, res)

    rs = np.array(divres*binarios)

    valores_z = [sum(z[i]) for i in range(len(z))]
    valores_z = np.array(valores_z)
    print(valores_z)

    lista_candidatos = []
    for j in range(len(rs)):
        lista_vacia = []
        lista_candidatos.append(lista_vacia)
        for l in range(len(rs[j])):
            sumrs = sum(rs[j][l])
            np.array(sumrs)
            print(sumrs, '<=', condicional[j])

            candidatos = np.all(sumrs <= condicional[j])
            lista_vacia.append(candidatos)
        # print(lista_vacia)

    lista_candidatos = np.array(lista_candidatos)
    lista_candidatos = np.transpose(lista_candidatos)

    for i in np.arange(len(lista_candidatos)):
        print(binarios[i], lista_candidatos[i], valores_z[i])

    lista_vacia2 = []
    for j in lista_candidatos:
        lista_vacia2.append(np.all(j == True))
    maximo = valores_z[lista_vacia2].max() if (
        tipo == 1) else valores_z[lista_vacia2].min()
    print(maximo)

    index_max = np.where(valores_z[lista_vacia2] == maximo)[0][0]
    print((binarios[lista_vacia2][index_max]))


if __name__ == "__main__":
    enumeracion()
