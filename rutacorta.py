from typing import Dict, Any
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

    def __str__(self):
        return ("Desde: {}\nHacia: {}\nCosto: {}".format(self.desde, self.hacia, self.costo))


class RutaCorta():

    num_nodos = 0
    conexiones = []
    nodo_inicial = -1
    nodo_final = -1

    def solicitar_datos(self):

        print("Vamos a buscar la ruta más corta de un nodo a otro.")
        print(
            "Para esto necesito sabes cuantos nodos hay en el problema y como se conectan")
        self.num_nodos = input_int("Dime ¿Cuantos nodos hay en tu problema?")
        print("Excelente ahora llenemos la matriz de costos.")
        print("Si una conexion no es valida inserta una x.")

        for i in np.arange(self.num_nodos):
            for j in np.arange(self.num_nodos):
                temp_conexion = input(
                    "Dime el costo del nodo {} al nodo {}: ".format(i+1, j+1))
                if temp_conexion == "x" or temp_conexion == "X":
                    continue
                temp_conexion = float(temp_conexion)
                self.conexiones.append(Conexion(i, j, temp_conexion))
        self.nodo_inicial = input_int("Dime en que nodo quieres iniciar: ") - 1
        self.nodo_final = input_int("Dime en que nodo quieres terminar: ") - 1

        self.conexiones = np.array(self.conexiones)

    def test_data(self, option):
        if option == 1:
            self.num_nodos = 8
            self.nodo_inicial = 0
            self.nodo_final = 7
            self.conexiones = [
                # Nodo 2
                Conexion(0, 1, 1),
                # Nodo 3
                Conexion(0, 2, 2),
                Conexion(1, 2, 1),
                # Nodo 4
                Conexion(1, 3, 5),
                Conexion(2, 3, 2),
                # Nodo 5
                Conexion(1, 4, 2),
                Conexion(2, 4, 1),
                Conexion(3, 4, 3),
                # Nodo 6
                Conexion(2, 5, 4),
                Conexion(3, 5, 6),
                Conexion(4, 5, 3),
                # Nodo 7
                Conexion(3, 6, 8),
                Conexion(4, 6, 7),
                Conexion(5, 6, 5),
                # Nodo 8
                Conexion(5, 7, 2),
                Conexion(6, 7, 6),
            ]

    @staticmethod
    def crear_nodo_alcazado(nodo: int, previo: int, costo_total: int) -> Dict[str, Any]:
        return({"nodo": nodo, "previo": previo, "costo": costo_total})

    def continua_ruta(self, nodos_alcanzados, nodos_posibles) -> bool:
        if all(x for x in nodos_alcanzados if x["nodo"] != self.nodo_final):
            return False
        final = next(
            (nodo for nodo in nodos_alcanzados if nodo["nodo"] == self.nodo_final), None)
        for i in [nodo for nodo in nodos_alcanzados if nodo["nodo"] == self.nodo_final]:
            if i["costo"] < final["costo"]:
                final = i

    def solve(self):
        nodos_alcanzados = np.array([])
        nodos_revisados = np.array([])

        nodos_alcanzados = np.append(
            nodos_alcanzados, RutaCorta.crear_nodo_alcazado(self.nodo_inicial, None, 0))

        counter = 0
        while True:
            pdb.set_trace()
            nodos_posibles = np.array([])
            for i in nodos_alcanzados[~np.isin(nodos_alcanzados, nodos_revisados)]:
                nuevas_conexiones = [
                    conx for conx in self.conexiones if conx.desde == i["nodo"]]
                for conexion in nuevas_conexiones:
                    print(conexion)

            counter += 1
            if counter > self.num_nodos+1:
                break


if __name__ == "__main__":
    ruta = RutaCorta()
    # ruta.solicitar_datos()
    ruta.test_data(1)
    ruta.solve()
