import pdb

import numpy as np

# Funciones utilitarias


def input_int(message=""):
    return int(input(message))


def try_again():
    input_int("")

# class Step():
#     def __init__(self, idx, costo, previous):
#         self.idx = idx
#         self.costo = costo
#         self.previous = previous


class Conexion():
    def __init__(self, desde, hacia, costo):
        self.desde = desde
        self.hacia = hacia
        self.costo = costo


class RutaCorta():

    num_nodos = 0
    num_conexiones = 0
    conexiones = []

    def solicitar_datos(self):

        print("Vamos a buscar la ruta más corta de un nodo a otro.")
        print(
            "Para esto necesito sabes cuantos nodos hay en el problema y como se conectan")
        self.num_nodos = input_int("Dime ¿Cuantos nodos hay en tu problema?")
        print("Excelente ahora llenemos la matriz de costos.")
        print("Si una conexion no es valida inserta una x.")

        for i in np.arange(self.num_nodos):
            self.conexiones.append([])
            for j in np.arange(self.num_nodos):
                temp_conexion = input(
                    "Dime el costo del nodo {} al nodo {}".format(i, j))
                if temp_conexion == "x" or temp_conexion == "X":
                    pass
                temp_conexion = float(temp_conexion)
                self.conexiones.append(Conexion(i, j, temp_conexion))

    def solve(self):
        pass
