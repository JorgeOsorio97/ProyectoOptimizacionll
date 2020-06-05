from typing import Dict, Any, List
import pdb
from copy import copy

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

    def __str__(self):
        return ("Desde: {}\nHacia: {}\nCosto: {}".format(self.desde, self.hacia, self.costo))


class Floyd():

    num_nodos: int = 0
    conexiones: np.ndarray = []
    nodo_inicial: int = -1
    nodo_final: int = -1
    mat_dec: List[List[int]] = []
    z = 0

    def solicitar_datos(self):

        print("Vamos a buscar la ruta más corta de un nodo a otro.")
        print(
            "Para esto necesito sabes cuantos nodos hay en el problema y como se conectan")
        self.num_nodos = input_int("Dime ¿Cuantos nodos hay en tu problema?")
        print("Excelente ahora llenemos la matriz de costos.")
        print("Si una conexion no es valida inserta una x.")

        conexiones_M = []
        for i in np.arange(self.num_nodos):
            self.conexiones.append([])
            for j in np.arange(self.num_nodos):
                temp_conexion = input(
                    "Dime el costo del nodo {} al nodo {}: ".format(i+1, j+1))
                if temp_conexion == "x" or temp_conexion == "X":
                    conexiones_M.append([i, j])
                    temp_conexion = 0
                temp_conexion = float(temp_conexion)
                self.conexiones[i].append(temp_conexion)

        # self.conexiones = np.array(self.conexiones)

        for i in conexiones_M:
            self.conexiones[i[0]][i[1]] = None

        self.nodo_inicial = input_int("Dime en que nodo quieres iniciar: ") - 1
        self.nodo_final = input_int("Dime en que nodo quieres terminar: ") - 1

    def test_data(self, option):
        if option == 1:
            self.num_nodos = 5
            self.conexiones = [
                [None, 3, 10, None, None],
                [3, None, None, 5, None],
                [10, None, None, 6, 15],
                [None, 5, 6, None, 4],
                [None, None, 1, 4, None]
            ]
            self.nodo_inicial = 0
            self.nodo_final = 4

    def definir_ruta(self, inicio, fin):
        intermedio = self.mat_dec[inicio][fin]
        if intermedio == fin:
            self.z += self.conexiones[inicio][fin]
            return ([inicio, fin])
        agregar_ruta = self.definir_ruta(
            inicio, intermedio) + self.definir_ruta(intermedio, fin)
        return agregar_ruta

    def solve(self):
        list_nodos = np.arange(self.num_nodos)
        costos = copy(self.conexiones)
        for i in list_nodos:
            self.mat_dec.append(list_nodos)
        self.mat_dec = np.array(self.mat_dec)
        print(self.mat_dec)

        for k in np.arange(self.num_nodos):
            import pdb; pdb.set_trace()
            for i in list_nodos[list_nodos != k]:
                for j in list_nodos[list_nodos != k]:
                    if i == j:
                        continue
                    nuevo_costo = None
                    if costos[k][j] is None or costos[i][k] is None:
                        continue

                    nuevo_costo = costos[k][j]+costos[i][k]
                    if costos[i][j] is None:
                        costos[i][j] = nuevo_costo
                        self.mat_dec[i][j] = k
                        continue

                    if nuevo_costo < costos[i][j]:
                        costos[i][j] = nuevo_costo
                        self.mat_dec[i][j] = k
            # print(self.mat_dec+1)
        print("Matriz de transicion:")
        print(self.mat_dec+1)
        ruta = self.definir_ruta(self.nodo_inicial, self.nodo_final)
        # ruta = np.array(ruta)
        # print(ruta)
        to_pop = []
        for i in np.arange(len(ruta)):
            if i == 0:
                continue
            if ruta[i] == ruta[i-1]:
                to_pop.append(i)
        # print(to_pop)
        for i in np.arange(len(to_pop)-1, -1, -1):
            ruta.pop(to_pop[i])
        print("Z=", self.z)
        print("La ruta a seguir es:", np.array(ruta)+1)


if __name__ == "__main__":
    floyd = Floyd()
    floyd.solicitar_datos()
    # floyd.test_data(1)
    floyd.solve()
