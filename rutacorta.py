from typing import Dict, Any, List
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


class ConexionR():
    def __init__(self, desde, hacia, costo):
        self.desde = desde
        self.hacia = hacia
        self.costo = costo

    def __str__(self):
        return ("Desde: {}\nHacia: {}\nCosto: {}".format(self.desde, self.hacia, self.costo))


class RutaCorta():

    num_nodos: int = 0
    nodos: np.ndarray = []
    conexiones: List[ConexionR] = []
    nodo_inicial: int = -1
    nodo_final: int = -1

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
                self.conexiones.append(ConexionR(i, j, temp_conexion))
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
                ConexionR(0, 1, 1),
                # Nodo 3
                ConexionR(0, 2, 2),
                ConexionR(1, 2, 1),
                # Nodo 4
                ConexionR(1, 3, 5),
                ConexionR(2, 3, 2),
                # Nodo 5
                ConexionR(1, 4, 2),
                ConexionR(2, 4, 1),
                ConexionR(3, 4, 3),
                # Nodo 6
                ConexionR(2, 5, 4),
                ConexionR(3, 5, 6),
                ConexionR(4, 5, 3),
                # Nodo 7
                ConexionR(3, 6, 8),
                ConexionR(4, 6, 7),
                ConexionR(5, 6, 5),
                # Nodo 8
                ConexionR(5, 7, 2),
                ConexionR(6, 7, 6),
            ]

    def crear_nodos(self,) -> None:
        for i in np.arange(self.num_nodos):
            self.nodos.append(
                {"id": i, "desde": None, "costo": 0, "alcanzado": False})
        self.nodos = np.array(self.nodos)

    def continua_ruta(self) -> bool:
        last = self.nodos[self.nodo_final]
        if last["alcanzado"] == False:
            return True

        for i in [nodo for nodo in self.nodos if nodo["id"] != self.nodo_final]:
            if i["costo"] < last["costo"]:
                return True
        return False

    def solve(self):
        self.crear_nodos()
        nodos_revisados = []

        self.nodos[self.nodo_inicial]["alcanzado"] = True

        counter = 0
        while True:
            # pdb.set_trace()
            nodos_posibles = [
                nodo for nodo in self.nodos if nodo["alcanzado"] == True and nodo["id"] not in nodos_revisados]
            for i in nodos_posibles:
                nuevas_conexiones = [
                    conx for conx in self.conexiones if conx.desde == i["id"]]
                for conexion in nuevas_conexiones:
                    # Nodo hacia el que llega la conexion
                    hacia = self.nodos[conexion.hacia]
                    desde = self.nodos[conexion.desde]
                    nuevo_costo = desde["costo"] + conexion.costo
                    if hacia["alcanzado"] == True:
                        if nuevo_costo < hacia["costo"]:
                            self.nodos[conexion.hacia]["desde"] = conexion.desde
                            self.nodos[conexion.hacia]["costo"] = nuevo_costo
                    else:
                        self.nodos[conexion.hacia]["alcanzado"] = True
                        self.nodos[conexion.hacia]["alcanzado"] = True
                        self.nodos[conexion.hacia]["desde"] = conexion.desde
                        self.nodos[conexion.hacia]["costo"] = nuevo_costo
                nodos_revisados.append(i["id"])

            counter += 1
            if not self.continua_ruta():
                break
            if counter > self.num_nodos+1:
                break

        nodo = self.nodos[self.nodo_final]
        str_ruta = "{}".format(nodo["id"]+1)
        # pdb.set_trace()
        while nodo["desde"] is not None:
            str_ruta = "{} -> {}".format(nodo["desde"]+1, str_ruta)
            nodo = self.nodos[nodo["desde"]]
        print("La mejor ruta es: {}".format(str_ruta))
        print("Y el costo es de: {}".format(
            self.nodos[self.nodo_final]["costo"]))


if __name__ == "__main__":
    ruta = RutaCorta()
    ruta.solicitar_datos()
    # ruta.test_data(1)
    ruta.solve()
