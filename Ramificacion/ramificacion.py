import typing
from enum import Enum, unique

import numpy as np
from scipy.optimize import linprog


# UTILIDADES

# Funciones utilitarias

def input_int(message=""):
    return int(input(message))


def try_again():
    input_int("")

# Enumeraciones


@unique
class Objetivo(Enum):
    MAXIMIZAR = 1
    MINIMIZAR = 2


class Ramificacion():

    # Variables ingresadas
    num_var = 0
    num_res = 0
    rest = []
    b = []
    c = []
    obj = 0

    def solicitar_datos(self) -> None:

        print("¿Que quieres hacer?")
        print("Maximizar: ingresa 1")
        print("Minimizar: ingresa 2")
        o = input_int("")
        if o == 1:
            self.obj = Objetivo.MAXIMIZAR
        elif o == 2:
            self.obj = Objetivo.MINIMIZAR

        self.num_var = input_int("¿Cuantas variables tiene el problema?")
        self.num_res = input_int("¿Cuantas restricciones tiene el problema?")

        print("Llenemos los coeficientes de la funcion objetivo")
        for i in np.arange(self.num_var):
            self.c.append(
                input_int("Dime el coeficiente de la variable x{}: ".format(i)))

        print("Es importante que debemos tener todas nuestras reestriciones de la forma:")
        print("Sum(xi*restricion_i) <=> b")
        for i in np.arange(self.num_res):
            self.rest.append([])
            print("Esta es una reestrcion mayor que (>) o menor que(<)?")
            print("<=: ingresa 1")
            print("=: ingresa 2")
            print(">=: ingresa 3")
            tipo_res = input_int()
            for j in np.arange(self.num_var):
                self.rest[i].append(input_int(
                    "Dime el coeficiente de la variable x{} en la reestricción {}: ".format(j, i)))
            self.b.append(
                input_int("Dime el valor b de la reestricción {}: ".format(i)))

            print("La reestricción queda: {} {} {}".format(
                "".join([" ({})x{} +".format(val, idx)
                         for idx, val in enumerate(self.rest[i])])[:-1],
                "<=" if tipo_res == 1 else ("=" if tipo_res == 2 else ">="),
                self.b[i]
            ))
            # TODO: Convertir en forma normal las reestricciones

    def solve_simplex(self):
        pass


if __name__ == "__main__":
    ram = Ramificacion()
    ram.solicitar_datos()
