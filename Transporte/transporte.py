# Std library
import itertools
from typing import Tuple, List
from enum import Enum, unique

import numpy as np
import pandas as pd


# UTILIDADES

# Funciones utilitarias

def input_int(message):
    return int(input(message))


def try_again():
    input_int("")

# Enumeraciones


@unique
class Artificial(Enum):
    ORIGENES = 1
    DESTINOS = 2


@unique
class Objetivo(Enum):
    MAXIMIZAR = 1
    MINIMIZAR = 2


# Tipos
Coord = Tuple[int, int]
Ruta = List[Coord]


class Transporte():

    # Varibles ingresadas
    obj: Objetivo = 0
    oferta_origenes = []
    demanda_destinos = []
    num_origenes = 0
    num_destinos = 0
    num_transbordos = 0
    mat_costo = []
    mat_dec = []

    # Variables calculadas
    mat_base = []
    artificial: Artificial = 0
    mat_sombra = []
    u = []
    v = []

    def inicializar_variables(self) -> None:
        self.obj = 0
        self.oferta_origenes = []
        self.demanda_destinos = []
        self.num_origenes = 0
        self.num_destinos = 0
        self.num_transbordos = 0
        self.mat_costo = []
        self.mat_sombra = []
        self.mat_dec = []
        self.mat_base = []
        self.artificial = 0
        self.u = []
        self.v = []

    def print_all_data(self) -> None:
        print(self.obj)
        print(self.oferta_origenes)
        print(self.demanda_destinos)
        print(self.num_origenes)
        print(self.num_destinos)
        print(self.num_transbordos)
        print(self.mat_costo)
        print(self.mat_sombra)
        print(self.mat_dec)
        print(self.mat_base)
        print(self.artificial)
        print(self.u)
        print(self.v)

    def solicitar_datos(self) -> None:
        """Esta función es para llenar los datos usados en el modelo.
        Se solicita mediante input en consola.
        Pedimos 3 cosas:
         * Pedimos la cantidad de origenes, destinos y transbordos.
         * Pedimos las ofertas de cada origen y demandas de cada destino.
         * Pedimos el costo de de cada posible transicion.
        """
        print("Vamos a resolver un problemas de transporte.")
        try:
            print("¿Que quieres hacer?")
            print("Maximizar: ingresa 1")
            print("Minimizar: ingresa 2")
            o = input_int("")
            if o == 1:
                self.obj = Objetivo.MAXIMIZAR
            elif o == 2:
                self.obj = Objetivo.MINIMIZAR

            # Cantidad de orignes, destinos y transbordos.
            self.num_origenes = input_int(
                "¿Cuantos origenes tiene tu problema?")
            self.num_destinos = input_int(
                "¿Cuantos destinos tiene tu problema?")
            self.num_transbordos = input_int(
                "¿Cuantos transbordos?\n(Si no tiene transbordo pon 0)")

            # Ofertas de cada origen y demandas de cada destino
            for i in range(self.num_origenes):
                self.oferta_origenes.append(
                    input_int("¿Cuál es la oferta de tu origen #{}: ".format(i+1)))

            self.oferta_transbordos = [
                sum(self.oferta_origenes)]*self.num_transbordos
            self.oferta_origenes += self.oferta_transbordos

            self.demanda_destinos += self.oferta_transbordos
            for i in range(self.num_destinos):
                self.demanda_destinos.append(
                    input_int("¿Cuál es la demanda de tu destino #{}: ".format(i+1)))

#             print(self.oferta_origenes, self.demanda_destinos)

            # Matriz de costos
            print("Excelente ahora llenemos la matriz de costos.")
            print("Si una conexion no es valida inserta una x.")
            for i in range(self.num_destinos + self.num_transbordos):
                self.mat_costo.append([])

            num_cols = self.num_destinos + self.num_transbordos
            num_filas = self.num_origenes + self.num_transbordos
            max_cant_conexiones = (num_filas) * (num_cols)

            for i in range(max_cant_conexiones):
                fila = i//num_filas  # ORIGENES
                col = i % num_cols  # DESTINOS
                origen = "origen" if fila < self.num_origenes else "transbordo"
                n_origen = fila+1 if fila < self.num_origenes else fila+1-self.num_origenes
                destino = "transbordo" if col < self.num_transbordos else "destino"
                n_destino = col+1 if col < self.num_transbordos else col+1-self.num_transbordos
                temp_val = input("Costo de {} #{} al {} #{} es:".format(
                    origen, n_origen, destino, n_destino))
                # TODO: Validaciones de la entrada de costos
                temp_val = int(
                    temp_val) if temp_val != "x" or temp_val == "X" else -1
                temp_val = temp_val if temp_val >= 0 else -1

                self.mat_costo[i//num_filas].append(temp_val
                                                    )
            if sum(self.oferta_origenes) > sum(self.demanda_destinos):
                self.artificial = Artificial.DESTINOS
                self.demanda_destinos.append(
                    sum(self.oferta_origenes)-sum(self.demanda_destinos))
                for i in range(num_filas):
                    self.mat_costo[i].append(0)

            elif sum(self.oferta_origenes) < sum(self.demanda_destinos):
                self.artificial = Artificial.ORIGENES
                self.oferta_origenes.append(
                    sum(self.demanda_destinos)-sum(self.oferta_origenes))
                self.mat_costo.append([0]*num_cols)

            self.oferta_origenes = np.array(self.oferta_origenes)
            self.demanda_destinos = np.array(self.demanda_destinos)
            self.mat_costo = np.array(self.mat_costo)

            max_costo = self.mat_costo.max()

            self.mat_costo = np.where(
                self.mat_costo == -1, max_costo + 1000, self.mat_costo)

            # self.print_all_data()
            # input()

        except ValueError:
            print("No entendí eso. :( Porfavor solo inserta valores numéricos")
            print("Enter para intentar otra vez.")
            self.inicializarVariables()
            input()
            self.solicitarDatos()
        except BaseException as e:
            print("Ups parece que hubo un error!")
            print(e)
            e.traceback()
            print("Enter para intentar otra vez.")
            self.inicializarVariables()
            input()
            self.solicitarDatos()

    def test_data(self, case: int) -> None:
        if case == 1:  # Caso transbordo con artificial en destinos
            self.num_origenes = 2
            self.num_destinos = 2
            self.num_transbordos = 2
            self.oferta_origenes = np.array([150, 200, 350, 350])  # Total 350
            self.demanda_destinos = np.array(
                [350, 350, 130, 130, 90])  # Total 260 + 90
            self.artificial = Artificial.DESTINOS

            self.mat_costo = np.array([
                [8, 13, 25, 28, 0],
                [15, 12, 26, 25, 0],
                [0, 6, 16, 17, 0],
                [6, 0, 14, 16, 0]
            ])
        elif case == 2:  # Caso transporte con artificial en destinos
            self.num_origenes = 3
            self.num_destinos = 5
            self.num_transbordos = 0
            self.oferta_origenes = np.array([1000, 1500, 750])  # Total 3,250
            self.demanda_destinos = np.array(
                [2000, 500, 400, 10, 100, 240])  # 3,010 + 240
            self.artificial = Artificial.DESTINOS

            self.mat_costo = np.array([
                [3, 20, 25, 75, 45, 0],
                [20, 15, 2, 50, 80, 0],
                [15, 2, 10, 40, 60, 0]
            ])

    # Funciones iniciales
    def noroeste(self) -> Tuple[np.ndarray, np.ndarray]:
        ofertas = self.oferta_origenes
        demandas = self.demanda_destinos
        transbordos = self.num_transbordos
        sobrante_oferta = ofertas.sum()
        origen_idx = 0
        destino_idx = 0

        self.mat_dec = np.zeros((len(ofertas), len(demandas)))
        self.mat_base = np.full((len(ofertas), len(demandas)), False)

        while sobrante_oferta > 0:
            current = min(ofertas[origen_idx], demandas[destino_idx])
            self.mat_dec[origen_idx][destino_idx] = current
            self.mat_base[origen_idx][destino_idx] = True
            sobrante_oferta -= current
            ofertas[origen_idx] -= current
            demandas[destino_idx] -= current
            if ofertas[origen_idx] <= demandas[destino_idx]:
                origen_idx += 1
            else:
                destino_idx += 1
        return self.mat_dec, self.mat_base

    def costo_minimo(self) -> Tuple[np.ndarray, np.ndarray]:
        ofertas = self.oferta_origenes
        demandas = self.demanda_destinos
        costos = self.mat_costo
        transbordos = self.num_transbordos
        # print("ofertas", ofertas)
        # print("demandas", demandas)
        # print("costos", costos)
        # print("trasnbordos", transbordos)

        sobrante_oferta = ofertas.sum()
        sobrante_origenes = ofertas[0:len(ofertas)-transbordos].sum()
        origenes_disponibles = [True]*len(ofertas)
        destinos_disponibles = [True]*len(demandas)

        self.mat_dec = np.zeros((len(ofertas), len(demandas)))
        self.mat_base = np.full((len(ofertas), len(demandas)), False)

        counter = 0

        while sobrante_origenes > 0 and counter < (len(ofertas)+len(demandas) + 5):

            costos_origenes = costos[0:len(ofertas)-transbordos, ]
            costos_origenes = costos_origenes[origenes_disponibles[0:len(
                ofertas)-transbordos]]
            costos_origenes = costos_origenes[:, destinos_disponibles]
            minimo = costos_origenes.min()
            if minimo == 0 and costos_origenes.sum() > 0:
                minimo = minimo if minimo > 0 else np.partition(
                    np.unique(costos_origenes), 1)[1]
            fila = np.where(costos_origenes == minimo)[0]
            fila = fila[0]
            col = np.where(costos_origenes[fila] == minimo)[0][0]

            current = min(ofertas[origenes_disponibles]
                          [fila], demandas[destinos_disponibles][col])

            campos_disponibles = [x[0] and x[1] for x in itertools.product(
                origenes_disponibles, destinos_disponibles)]
            campos_disponibles = np.array(campos_disponibles).reshape(
                len(ofertas), len(demandas))
            fila = np.where(np.logical_and(
                costos == minimo, campos_disponibles))[0][0]
            col = np.where(costos[fila] == minimo)[0][0]
            self.mat_dec[fila][col] = current
            self.mat_base[fila][col] = True

            sobrante_oferta -= current
            sobrante_origenes -= current
            ofertas[fila] -= current
            demandas[col] -= current
            if ofertas[fila] <= demandas[col]:
                origenes_disponibles[fila] = False
            else:
                destinos_disponibles[col] = False
            counter += 1

        counter = 0

        sobrante_demandas = demandas[transbordos:-1].sum(
        ) if self.artificial == Artificial.DESTINOS else demandas[transbordos:].sum()

        while sobrante_demandas > 0 and counter < (len(ofertas)+len(demandas) + 5):
            costos_demandas = costos[:, transbordos:]
            costos_demandas = costos_demandas[origenes_disponibles, :]
            costos_demandas = costos_demandas[:,
                                              destinos_disponibles[transbordos:]]

            minimo = costos_demandas.min()
            minimo = minimo if minimo > 0 else np.partition(
                np.unique(costos_demandas), 1)[1]
            fila = np.where(costos_demandas == minimo)[0]
            fila = fila[0]
            col = np.where(costos_demandas[fila] == minimo)[0][0]

            current = min(ofertas[origenes_disponibles][fila],
                          demandas[destinos_disponibles][transbordos:][col])

            campos_disponibles = [x[0] and x[1] for x in itertools.product(
                origenes_disponibles, destinos_disponibles)]
            campos_disponibles = np.array(campos_disponibles).reshape(
                len(ofertas), len(demandas))
            fila = np.where(np.logical_and(
                costos == minimo, campos_disponibles))[0][0]
            col = np.where(costos[fila] == minimo)[0][0]
            self.mat_dec[fila][col] = current
            self.mat_base[fila][col] = True

            sobrante_oferta -= current
            sobrante_demandas -= current
            ofertas[fila] -= current
            demandas[col] -= current
            if ofertas[fila] <= demandas[col]:
                origenes_disponibles[fila] = False
            else:
                destinos_disponibles[col] = False
            counter += 1

        counter = 0

        while sobrante_oferta > 0 and counter < (len(ofertas)+len(demandas) + 5):

            costos_sobrantes = costos[origenes_disponibles, :]
            costos_sobrantes = costos_sobrantes[:, destinos_disponibles]

            minimo = costos_sobrantes.min()
            # minimo = minimo if minimo > 0 else np.partition(np.unique(costos_sobrantes), 1)[1]
            fila = np.where(costos_sobrantes == minimo)[0]
            fila = fila[0]
            col = np.where(costos_sobrantes[fila] == minimo)[0][0]

            current = min(ofertas[origenes_disponibles]
                          [fila], demandas[destinos_disponibles][col])

            campos_disponibles = [x[0] and x[1] for x in itertools.product(
                origenes_disponibles, destinos_disponibles)]
            campos_disponibles = np.array(campos_disponibles).reshape(
                len(ofertas), len(demandas))
            fila = np.where(np.logical_and(
                costos == minimo, campos_disponibles))[0][0]
            col = np.where(np.logical_and(
                costos == minimo, campos_disponibles))[1][0]
            self.mat_dec[fila][col] = current
            self.mat_base[fila][col] = True

            sobrante_oferta -= current
            sobrante_demandas -= current
            ofertas[fila] -= current
            demandas[col] -= current
            if ofertas[fila] <= demandas[col]:
                origenes_disponibles[fila] = False
            else:
                destinos_disponibles[col] = False
            # print(self.mat_dec)
            # print(self.mat_base)
            # print("origenes disponibles: ", origenes_disponibles)
            # print("destinos disponibles: ", destinos_disponibles)

        return self.mat_dec, self.mat_base

    def costos_sombra(self) -> Tuple[np.ndarray, np.ndarray]:
        self.u = np.array([0] + [None] * (len(self.oferta_origenes) - 1))
        self.v = np.array([None] * len(self.demanda_destinos))

        for i in np.where(self.mat_base[0])[0]:
            self.v[i] = self.mat_costo[0][i]

        while(np.any(self.u == None) or np.any(self.v == None)):
            base = np.where(self.mat_base)
            for i in range(len(base[0])):
                fila = base[0][i]
                col = base[1][i]
                if self.u[fila] is not None and self.v[col] is None:
                    self.v[col] = self.mat_costo[fila][col] - self.u[fila]
                elif self.v[col] is not None and self.u[fila] is None:
                    self.u[fila] = self.mat_costo[fila][col] - self.v[col]
        self.mat_sombra = np.zeros(
            (len(self.u), len(self.v)))
        not_base = np.where(np.logical_not(self.mat_base))
        for i in np.arange(len(not_base[0])):
            fila = not_base[0][i]
            col = not_base[1][i]
            self.mat_sombra[fila][col] = self.u[fila] + \
                self.v[col] - self.mat_costo[fila][col]

        return(self.mat_sombra)

    def encontrar_poligono(self):
        sombra_piv = self.mat_sombra.max(
        ) if self.obj == Objetivo.MINIMIZAR else self.mat_sombra.min()
        pivote = (np.where(self.mat_sombra == sombra_piv)[
                  0][0], np.where(self.mat_sombra == sombra_piv)[1][0])

        route = [pivote]

        def look_row(mat_base: np.ndarray, route: Ruta) -> Tuple[bool, List]:
            # print("ruta", route)
            base = mat_base.copy()
            base[route[-1][0]][route[-1][1]] = False
            posible_options = np.where(base[route[-1][0], :])
            for i in np.arange(len(posible_options[0])):
                fila = route[-1][0]
                col = posible_options[0][i]
                if (fila, col) in route:
                    if (fila, col) == route[0]:
                        return True, route
                    return False, route
                else:
                    valid, route2 = look_col(base, route + [(fila, col)])
                    if valid:
                        return True, route2
            return False, route

        def look_col(mat_base: np.ndarray, route: Ruta) -> Tuple[bool, Ruta]:
            # print("Ruta", route)
            base = mat_base.copy()
            base[route[-1][0]][route[-1][1]] = False
            posible_options = np.where(base[:, route[-1][1]])
            for i in np.arange(len(posible_options[0])):
                fila = posible_options[0][i]
                col = route[-1][1]
                if (fila, col) in route:
                    if (fila, col) == route[0]:
                        return True, route
                    return False, route
                else:
                    valid, route2 = look_row(base, route + [(fila, col)])
                    if valid:
                        return True, route2
            return False, route

        base = self.mat_base.copy()
        base[pivote[0]][pivote[1]] = True
        posible_options = np.where(base[:, route[-1][1]])
        for i in np.arange(len(posible_options[0])):
            current = (posible_options[0][i], route[-1][1])
            valid, route = look_row(base, route + [current])

            if valid:
                if route[0] == route[1]:
                    route.pop(1)
                current_x = -1
                current_y = -1
                cont_x = 1
                cont_y = 1
                to_pop = []
                for i in range(len(route)):
                    if route[i][0] == current_x:
                        cont_x += 1
                    else:
                        cont_x = 1
                        current_x = route[i][0]

                    if route[i][1] == current_y:
                        cont_y += 1
                    else:
                        cont_y = 1
                        current_y = route[i][1]
                    if cont_x > 2 or cont_y > 2:
                        to_pop += [i-1]
                for i in to_pop:
                    route.pop(i)
                return np.array(route)

    def decision_posicion(self, pos: Coord) -> float:
        return self.mat_dec[pos[0]][pos[1]]

    def pivotear(self):
        ruta = self.encontrar_poligono()
        values = np.apply_along_axis(self.decision_posicion, 1, ruta)
        pivote = np.array([values[x] for x in range(1, len(values), 2)]).min()
        pos_min = ruta[np.where(values == pivote)[0][0]]
        self.mat_base[pos_min[0]][pos_min[1]] = False
        self.mat_base[ruta[0][0]][ruta[0][1]] = True
        # print(ruta)
        for i in range(len(ruta)):
            if i % 2 == 0:
                self.mat_dec[ruta[i][0]][ruta[i][1]] += pivote
            else:
                self.mat_dec[ruta[i][0]][ruta[i][1]] -= pivote

    def z(self):
        return (self.mat_dec * self.mat_costo).sum()

    def hay_mas_iteraciones(self):
        if self.obj == Objetivo.MAXIMIZAR:
            return self.mat_sombra.min() < 0
        else:
            return self.mat_sombra.max() > 0

    def __init__(self) -> None:
        self.solicitar_datos()
        # self.obj = Objetivo.MAXIMIZAR
        # self.test_data(1)
        print("¿Cuál metodo quieres usar para iniciar?")
        print("Esquina Noroeste: ingresa 1")
        print("Consto Mínimo: ingresa 2")
        o = input_int("")
        if o == 1:
            self.noroeste()
        elif o == 2:
            self.costo_minimo()
        print("Costo minimo")
        print(self.mat_dec)

        self.costos_sombra()
        while self.hay_mas_iteraciones():
            # print(transporte.mat_sombra.max())
            self.pivotear()
            self.costos_sombra()
            print("Decision")
            print(self.mat_dec)
            print("Sombra")
            print(self.mat_sombra)
            print("Z = ", self.z())
        print()
        print("RESULTADO")
        print("Decision")
        print(self.mat_dec)
        print("Sombra")
        print(self.mat_sombra)
        print("Z = ", self.z())


if __name__ == "__main__":
    transporte = Transporte()
