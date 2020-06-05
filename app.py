
import math
from random import *
import itertools as it
from typing import Dict, Any, List, Tuple
import pdb
from copy import copy
from enum import Enum, unique

import numpy as np
from scipy.optimize import linprog
from binarytree import Node

def input_int(message=""):
    return int(input(message))

def lista_vaciaM(lista_1):
    return not lista_1

def arbol_exp_minima():
    num_nodos=int(input("Dame la cantidad de nodos de tu grafo: "))
    
    #Ascii de 65(A) a 90(Z) chr(65)=A


    red=np.ones((num_nodos,num_nodos)) #Se crea una matriz de incidencia de nxn con 10**8  en cada espacio
    
    aristas= np.ones((num_nodos**2,3))
    aristas_modificaciones=np.ones((num_nodos**2,3))
    print(f"Nombremos a tus nodos desde A hasta {chr(64+num_nodos)};\n")

    print("Procederemos a llenar tus aristas, AB quiere decir que pregunto por el \n"
        "precio de ir de A a B. Es importante notar que AB no es lo mismo que BA en un grafo dirigido\n\n"
        "0 representa que no tiene costo mientras que None representa que no hay camino de A a B\n"
        "Si precionas enter sin dejar un valor se pondra None automaticamente y se entendera que no hay camino")
    n=0
    for i in range(num_nodos):
        for j in range(num_nodos):
            try:
                red[i,j]=input((f"Valor de {chr(65+i)} a {chr(65+j)}: "))
                aristas[n,0]=65+i
                aristas[n,1]=red[i,j]
                aristas[n,2]=65+j

            except:
                red[i,j]= 10**8
                aristas[n,0]=65+i
                aristas[n,1]=10**8
                aristas[n,2]=65+j
            n=n+1



            print("\n")



    lista_nodos = np.array(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
                    'S','T','U','V','W','X','Y','Z'])
    print("Tu matriz de incidencia es: ")
    print(f"  {lista_nodos[0:num_nodos]}")
    for i in range(num_nodos):
        print(f"{chr(65+i)} {red[i,0:]}") 

    for i in range(n):
        print(chr(int(aristas[i,0])),aristas[i,1], chr(int(aristas[i,2])))
    aristas_modificaciones=aristas
    
    metodo2(red, aristas_modificaciones)

def metodo2(matriz, lista_modificaciones):
    print("Metodo del arbol de expansion minima")
    #print(matriz)
    
    print(lista_modificaciones)
    
    #lista de nodos que no pertene aun al grafo final
    n= int(math.sqrt(matriz.size)) 
    arbol_minimo=np.ones((n,n))
    for i in range(n):
        for j in range(n):
            arbol_minimo[i,j]=10**8
    no_final=np.ones((1, n ))
    menor=[]
    minimo=10**8
    for i in range(n):
        no_final[0,i]=65+i
    #lista de nodos que ya pertenecen al grafo final
    si_final=[]
    index=10**8
    nodo_valido=0

    
    while (int(no_final.sum()) != n):#mientras existan nodos sueltos (o sea no se encuentren en el grafo final)
                                #el programa seguira buscando la siguiente mejor arista que complete el arbol
        for i in range(matriz.size):#valida si los nodos que una la arista ya estan contemplados en el arbol final
            for j in range(len(si_final)):
                if (lista_modificaciones[i,0] == si_final[j]):
                    nodo_valido=nodo_valido+1
                if (lista_modificaciones[i,2] == si_final[j]):
                    nodo_valido=nodo_valido+1
            print(f"nodo valido vale {nodo_valido}")
            if(nodo_valido==2):
                lista_modificaciones[i,1]=10**8 #si ambos nodos ya estan en el arbol entonces la arista ya no es relevante
            nodo_valido=0                           #y podemos igualarla a M (10**8) 
        minimo=10**8
        menor=[]
        index=10**8
        for i in range(matriz.size):
            if (lista_vaciaM(si_final)==True):
                menor.append(lista_modificaciones[i,1])
            else:
                for j in range(len(si_final)):
                    if (lista_modificaciones[i,0]==si_final[j] or lista_modificaciones[i,2]== si_final[j]):
                        menor.append(lista_modificaciones[i,1])

        minimo=min(menor)
        print(minimo)
        
        for i in range(matriz.size):
            print(f"minimo= {minimo}")
            print(f"tiene que ser igual a {lista_modificaciones[i,1]}")
            if (minimo==lista_modificaciones[i,1]):
                if (lista_vaciaM(si_final)==True):
                    index=i
                else:
                    for j in range(len(si_final)):
                        if (lista_modificaciones[i,0]==si_final[j] or lista_modificaciones[i,2]== si_final[j]):
                            index=i


        if (index==10**8):
            print("Algo salio muy mal  CORREEEEE")#significaria que aun no se conecta todo el arbol pero ya no hay aristas factibles
        arbol_minimo[(int(lista_modificaciones[index,0])-65), (int(lista_modificaciones[index,2])-65)]=float(lista_modificaciones[index,1])
        si_final.append(lista_modificaciones[index,0])
        si_final.append(lista_modificaciones[index,2])
        lista_modificaciones[index,1]=10**8
        for k in range(n):
            if (int(no_final[0,k])==int(lista_modificaciones[index,0])):
                no_final[0,k]=1
            if (int(no_final[0,k])==int(lista_modificaciones[index,2])):
                no_final[0,k]=1


        si_final=list(set(si_final))
        print("Iniciamos el rellenado de la matriz\n\n\n\n")
        print("matriz")
        print(arbol_minimo)
        print("nodos finales")
        for i in range(len(si_final)):
            print(chr(int(si_final[i])))
        print("nodos no finales")
        print(no_final)
    
        print(f"la condicion se rompe cuando {int(no_final.sum())} ={n}")

    print("Matriz final\n\n\n\n")
    print(arbol_minimo)
    for i in range(len(si_final)):
        print(chr(int(si_final[i])))
    print(no_final)
    print(f"lista modificaciones\n {lista_modificaciones}")
    lista_nodos = np.array(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
                    'S','T','U','V','W','X','Y','Z'])
    z=0
    contador=0
    for i in range(n):
        for j in range(n):
            if (arbol_minimo[i,j] == 10**8):
                contador=contador+1

    matriz_imp=np.full((n,n),"espero_funcione_lo_que_voy_a_intentar")
    for i in range(n):
        for j in range(n):
            if (matriz[i,j] ==10**8):
                matriz_imp[i,j]="X"
            else:
                matriz_imp[i,j]=str(matriz[i,j])

    print("Tu matriz de incidensia inicial es:\n")
    print(f"  {lista_nodos[0:n]}")
    for i in range(n):
        print(f"{chr(65+i)} {matriz_imp[i,0:]}")

    z=arbol_minimo.sum()-(contador*(10**8))
    arbol_minimo_imp=np.full((n,n),"espero_funcione_lo_que_voy_a_intentar")
    for i in range(n):
        for j in range(n):
            if (arbol_minimo[i,j] == 10**8):
                arbol_minimo_imp[i,j]="X"
            else:
                arbol_minimo_imp[i,j]=str(arbol_minimo[i,j])

    print("Resultado final, arbol de expansion minida del grafo:\n")
    print(f"  {lista_nodos[0:n]}")
    for i in range(n):
        print(f"{chr(65+i)} {arbol_minimo_imp[i,0:]}")

    print(f"Z={z}")

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
    '''print(valores_z)'''

    lista_candidatos = []
    for j in range(len(rs)):
        lista_vacia = []
        lista_candidatos.append(lista_vacia)
        for l in range(len(rs[j])):
            sumrs = sum(rs[j][l])
            np.array(sumrs)
            '''print(sumrs, '<=', condicional[j])'''

            candidatos = np.all(sumrs <= condicional[j])
            lista_vacia.append(candidatos)
        # print(lista_vacia)

    lista_candidatos = np.array(lista_candidatos)
    lista_candidatos = np.transpose(lista_candidatos)

    for i in np.arange(len(lista_candidatos)):
        '''print(binarios[i], lista_candidatos[i], valores_z[i])'''

    lista_vacia2 = []
    for j in lista_candidatos:
        lista_vacia2.append(np.all(j == True))
    maximo = valores_z[lista_vacia2].max() if (
        tipo == 1) else valores_z[lista_vacia2].min()
    print("La solucion Z= ", maximo)

    index_max = np.where(valores_z[lista_vacia2] == maximo)[0][0]
    print("El vector de solucion es: \n")
    print((binarios[lista_vacia2][index_max]))





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

        # costo_maximo = self.conexiones.max()
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
    
    numero_cortes=[]

@unique
class Objetivo(Enum):
    MAXIMIZAR = 1
    MINIMIZAR = 2


# Utils class
class Branch(Node):
    x = []
    z = None
    valid = False
    bounds = []

    def __init__(self, x, bounds, valid=False, z=0):
        super().__init__(z)
        self.x = x
        self.bounds = bounds
        self.valid = valid
        self.z = z

    def __bool__(self):
        return self.valid

    def __str__(self):
        return ("Limites: {} \n"
                "Valido: {} \n"
                "X: {}\n"
                "Z={}").format(self.bounds, self.valid, self.x, self.z)

    def print_tree(self):
        return print(super().__str__())


class Ramificacion():

    # Variables ingresadas
    num_vars = 0
    num_res = 0
    rest_uq = []
    rest_eq = []
    b_uq = []
    b_eq = []
    c = []
    obj = 0

    # Variables calculadas
    x = []
    bounds = []
    root: Branch

    def print_all_data(self):
        print("Objetivo", self.obj)
        print("num_vars: ", self.num_vars)
        print("num_restricciones", self.num_res)
        print("c")
        print(self.c)
        print("Resticciones desigualdad:")
        print(self.rest_uq)
        print("b desigualdad:")
        print(self.b_uq)
        print("Resticciones igualdad:")
        print(self.rest_eq)
        print("b igualdad:")
        print(self.b_eq)

    def solicitar_datos(self) -> None:

        print("¿Que quieres hacer?")
        print("Maximizar: ingresa 1")
        print("Minimizar: ingresa 2")
        o = input_int("")
        if o == 1:
            self.obj = Objetivo.MAXIMIZAR
        elif o == 2:
            self.obj = Objetivo.MINIMIZAR

        self.num_vars = input_int("¿Cuantas variables tiene el problema?\n")
        self.num_res = input_int("¿Cuantas restricciones tiene el problema?\n")

        print("Llenemos los coeficientes de la funcion objetivo")
        for i in np.arange(self.num_vars):
            self.c.append(
                input_int("Dime el coeficiente de la variable x{}: ".format(i)))

        print("Es importante que debemos tener todas nuestras reestriciones de la forma:")
        print("Sum(xi*restricion_i) <=> b")

        for i in np.arange(self.num_res):
            temp_rest = []
            temp_b = 0
            print("Esta es una reestrcion mayor que (>) o menor que(<)?")
            print("<=: ingresa 1")
            print("=: ingresa 2")
            print(">=: ingresa 3")
            tipo_res = input_int()
            for j in np.arange(self.num_vars):
                temp_rest.append(input_int(
                    "Dime el coeficiente de la variable x{} en la reestricción {}: ".format(j, i)))
            temp_b = input_int(
                "Dime el valor b de la reestricción {}: ".format(i))

            print("La reestricción queda: {} {} {}".format(
                "".join([" ({})x{} +".format(val, idx)
                         for idx, val in enumerate(temp_rest)])[:-1],
                "<=" if tipo_res == 1 else ("=" if tipo_res == 2 else ">="),
                temp_b
            ))
            if tipo_res == 1:
                self.rest_uq.append(temp_rest)
                self.b_uq.append(temp_b)
            if tipo_res == 2:
                self.rest_eq.append(temp_rest)
                self.b_eq.append(temp_b)
            if tipo_res == 3:
                self.rest_uq.append([x*(-1) for x in temp_rest])
                self.b_uq.append(temp_b*(-1))

        self.c = np.array(self.c)
        self.rest_uq = np.array(self.rest_uq)
        self.b_uq = np.array(self.b_uq)
        self.rest_eq = np.array(self.rest_eq)
        self.b_eq = np.array(self.b_eq)

        self.print_all_data()

    def test_data(self, option):
        if option == 1:
            self.obj = Objetivo.MAXIMIZAR
            self.num_vars = 2
            self.num_res = 3
            self.c = np.array([300, 168])
            self.rest_uq = np.array([
                [2, 4],
                [6, 8],
                [3, 1]
            ])
            self.b_uq = np.array([40, 92, 32])
        elif option == 2:
            self.obj = Objetivo.MAXIMIZAR
            self.num_vars = 3
            self.num_res = 3
            self.c = np.array([1, 2, 3])
            self.rest = np.array([
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ])
            self.b = np.array([100, 200, 300])
        elif option == 3:
            self.obj = Objetivo.MINIMIZAR
            self.num_vars = 6
            self.num_res = 6
            self.c = np.array([1, 1, 1, 1, 1, 1])
            self.rest_uq = np.array([
                [-1, -1, 0, 0, 0, 0],
                [-1, -1, 0, 0, 0, -1],
                [0, 0, -1, -1, 0, 0],
                [0, 0, -1, -1, -1, 0],
                [0, 0, 0, -1, -1, 0],
                [0, -1, 0, 0, -1, -1]
            ])
            self.b_uq = np.array([-1, -1, -1, -1, -1, -1])

    def option_valid(self) -> bool:
        # pdb.set_trace()
        uq = np.all([i.sum()
                     for i in self.rest_uq*self.x] <= self.b_uq)
        eq = np.all([i.sum() for i in self.rest_eq * self.x == self.b_eq])
        return np.all()

    def z(self) -> float or None:
        return (self.c*self.x).sum()

    def is_better_solution(self, branch) -> bool:
        if self.z() is None:
            return True
        # if self.obj == Objetivo.MAXIMIZAR:
        #     return self.z() < branch.z
        # if self.obj == Objetivo.MINIMIZAR:
        return self.z() > branch.z

    # def set_initial_bounds(self) -> None:
    #     for i in np.arange(self.num_vars):
    #         lower = 0
    #         upper = 0
    #         self.x = [0]*self.num_vars
    #         while self.option_valid():
    #             self.x[i] += 1
    #         self.bounds.append([0, self.x[i]])
    #     print(self.bounds)

    def solve_simplex(self, bounds=[]) -> Branch:

        for i in bounds:
            if i[0] is not None and i[1] is not None:
                if i[0] > i[1]:
                    return Branch([], bounds, False)

        temp_c = self.c if self.obj == Objetivo.MINIMIZAR else [
            i*(-1) for i in self.c]
        # pdb.set_trace()
        if len(self.rest_uq) > 0 and len(self.rest_eq) > 0:
            res = linprog(c=temp_c, A_ub=self.rest_uq, b_ub=self.b_uq, A_eq=self.rest_eq, b_eq=self.b_eq,
                          bounds=bounds, method="simplex")
        elif len(self.rest_uq) > 0:
            res = linprog(c=temp_c, A_ub=self.rest_uq,
                          b_ub=self.b_uq, bounds=bounds, method="simplex")
        elif len(self.rest_eq) > 0:
            res = linprog(c=temp_c, A_eq=self.rest_eq, b_eq=self.b_eq,
                          bounds=bounds, method="simplex")

        return Branch(res["x"], bounds, res["success"], res["fun"] if res["success"] else 0)

    @staticmethod
    def is_integer_solution(x: np.ndarray) -> Tuple[bool, int]:
        # pdb.set_trace()
        if len(x) <= 0:
            return False
        for i in np.arange(len(x)):
            if int(x[i]) != x[i]:
                return False, i
        return True, -1

    def test_branch(self, branch: Branch) -> bool:
        self.root.print_tree()
        print(branch)
        # pdb.set_trace()
        is_int, idx = Ramificacion.is_integer_solution(branch.x)
        if branch.valid:
            if not is_int:
                if not self.is_better_solution(branch):
                    return
                lower_bounds = copy(branch.bounds)
                upper_bounds = copy(branch.bounds)

                lower_bounds[idx] = [lower_bounds[idx][0], int(branch.x[idx])]
                upper_bounds[idx] = [
                    int(branch.x[idx]) + 1, upper_bounds[idx][1]]

                branch.right = copy(self.solve_simplex(upper_bounds))
                branch.right.bounds = upper_bounds
                self.test_branch(branch.right)

                branch.left = self.solve_simplex(lower_bounds)
                branch.left.bounds = lower_bounds
                self.test_branch(branch.left)
            else:
                if self.is_better_solution(branch):
                    self.x = branch.x

    def solve(self):
        extra_bounds = [[None, None]]*self.num_vars
        self.root = self.solve_simplex(extra_bounds)
        valid, _ = Ramificacion.is_integer_solution(self.root.x)
        if valid:
            print(self.root)
            self.x = self.root.x
            return self.x, self.z()
        self.x = [0*self.num_vars]
        branch = self.root
        self.test_branch(branch)
        z = self.z() if self.obj == Objetivo.MINIMIZAR else -self.z()
        print("Los valores para x son {}".format(self.x))
        print("Z={}".format(self.z()))
        return self.x, self.z()

def simplex_redes():
    num_nodos=int(input("Dame la candidad de nodos de tu red: "))
    
    #Ascii de 65(A) a 90(Z) chr(65)=A


    red=np.ones((num_nodos,num_nodos))#Se crea una matriz de adyacencia de nxn con costos c_ij
    
    red_minima=np.ones((num_nodos,num_nodos)) 
    red_iteracion_x=np.ones((num_nodos,num_nodos))#costos calculados x_ij
    red_iteracion_c=np.ones((num_nodos,num_nodos))#costos c_ij de iteracion que se ocupan esa iteracion
    red_iteracion_z=np.ones((num_nodos,num_nodos))
    indices_ecuaciones=np.ones((num_nodos-1,3))

    aristas=np.ones(((num_nodos)**2,3))
    aristas_c=np.ones(((num_nodos)**2,3))

    w_i=np.ones((num_nodos,1))
    indices_ecuaciones=np.empty((num_nodos-1,3))
    
    nodo_ofe_dem=[]   #demandas y productos de nodos (b_i)
    print(f"Nombremos a tus nodos desde A hasta {chr(64+num_nodos)};\n"
        f"A sera tu nodo de salida y {chr(64+num_nodos)} sera tu nodo destino\n")

    print("Procederemos a llenar tus aristas, AB quiere decir que pregunto por el \n"
        "precio de ir de A a B. Es importante notar que AB no es lo mismo que BA en un grafo dirigido\n\n"
        "0 representa que no tiene costo mientras que None representa que no hay camino de A a B\n"
        "Si precionas enter sin dejar un valor se pondra None automaticamente y se entendera que no hay camino")
    n=0
    for i in range(num_nodos):
        for j in range(num_nodos):
            try:
                red[i,j]=input((f"Valor de {chr(65+i)} a {chr(65+j)}: "))
                aristas[n,0]=65+i
                aristas[n,1]=red[i,j]
                aristas[n,2]=65+j

            except:
                red[i,j]= 10**8
                aristas[n,0]=65+i
                aristas[n,1]=10**8
                aristas[n,2]=65+j
            n=n+1
            print("\n")
            
    #red[num_nodos,num_nodos]=10**8
    #lista_nodo_artificial=np.full((num_nodos+1,3), 10**8)

    print("ahora dame la demanda o la oferta de cada nodo\n")
    for i in range(num_nodos):
        nodo_ofe_dem.append(input((f"valor del nodo {chr(65+i)}: \n")))
        #if(int(nodo_ofe_dem[i])==0):
         #   lista_nodo_artificial[i,0]=65+i
          #  lista_nodo_artificial[i,1]=10**8
           # lista_nodo_artificial[i,2]=64
       # if(int(nodo_ofe_dem[i])>0):
        #    lista_nodo_artificial[i,0]=65+i
         #   lista_nodo_artificial[i,1]=int(nodo_ofe_dem[i])
          #  lista_nodo_artificial[i,2]=64
        #elif (int(nodo_ofe_dem[i])<0):
         #   lista_nodo_artificial[i,2]=65+i
          #  lista_nodo_artificial[i,1]=int(nodo_ofe_dem[i])*(-1)
           # lista_nodo_artificial[i,0]=64
    #lista_nodo_artificial[num_nodos,0]=64
    #lista_nodo_artificial[num_nodos,1]=0
    #lista_nodo_artificial[num_nodos,2]=63

    b_n=0
    for i in range(len(nodo_ofe_dem)):
        b_n=b_n+int(nodo_ofe_dem[i])
    if (b_n != 0):
        print("El grafo no esta balanceado")
    print("Funcion objetivo: \n")
    funcion=[]
    for i in range(num_nodos**2):
        if (aristas[i,1] !=10**8):
            if (lista_vaciaM(funcion)==True):
                funcion.append(f"({(aristas[i,1])*(-1)}X_{chr(int(aristas[i,0]))}{chr(int(aristas[i,2]))})")
            else:
                funcion.append(f"+({(aristas[i,1])*(-1)}X_{chr(int(aristas[i,0]))}{chr(int(aristas[i,2]))})")
     

    lista_nodos = np.array(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
                    'S','T','U','V','W','X','Y','Z'])
    print("Tu matriz de adyasencia es: ")
    print(f"  {lista_nodos[0:num_nodos]}")
    for i in range(num_nodos):
        print(f"{chr(65+i)} {red[i,0:]}") 

    for i in range(n):
        print(chr(int(aristas[i,0])),aristas[i,1], chr(int(aristas[i,2])))
    
    print(f"Minizar z={funcion}")
    

    aristas_c=aristas.copy()
    red_iteracion_c=red.copy()
    
    con=0
    for i in range(num_nodos):
        for j in range(num_nodos):
            if (red_iteracion_c[i,j] != 10**8):
                if(int(nodo_ofe_dem[i]) <0 ):
                    if(int(nodo_ofe_dem[j])>0):#eliminamos la linea
                        
                        red_iteracion_c[i,j]=10**8
                        aristas_c[con,0]=65+i
                        aristas_c[con,1]=10**8
                        aristas_c[con,2]=65+j
            con=con+1
    







        



                    
    
    red_minima=metodo3(red_iteracion_c, aristas_c)
    
    
    for i in range(num_nodos):
        for j in range(num_nodos):
            red_iteracion_x[i,j]=10**8

    
    red_iteracion_c=red_minima.copy()
    

    nodos_hojas_raices=np.ones((num_nodos,2))# (num nodos que manda, num nodos que recibe)
    manda=0
    recibe=0
    cos_red_pos=0
    #n_h=0
    
    print(red_minima)
    print("Definimos que nodos son hojas y que nodos son de transicion")
    for i in range(num_nodos):
        manda=0
        recibe=0
        for j in range(num_nodos):
            
            
            if(red_iteracion_c[i,j] != 10**8):
                manda=manda+1
            nodos_hojas_raices[i,0]=manda
            
        for k in range(num_nodos):
            if (red_iteracion_c[k,i] != 10**8):
                recibe=recibe+1 
            nodos_hojas_raices[i,1]=recibe    
                                        
        
    
    print("Llenamos la matriz de x_ij con los costos de demanda y oferta")
    print("nodos hojas")
    print(nodos_hojas_raices)
    #pdb.set_trace()
    for i in range(num_nodos):
        if((nodos_hojas_raices[i,0]+nodos_hojas_raices[i,1]) == 1):
            if (int(nodo_ofe_dem[i])<0):
                for s in range(num_nodos):
                    if (red_iteracion_c[s,i]!=10**8):
                        red_iteracion_x[s,i]=int(nodo_ofe_dem[i])*(-1)
            elif(int(nodo_ofe_dem[i])>0 and nodos_hojas_raices[i,0]==1):
                for s in range(num_nodos):
                    if (red_iteracion_c[i,s] != 10**8):
                        red_iteracion_x[i,s]=int(nodo_ofe_dem[i])
        else:
            flujo=0
            aristas_temporales=[]
            for s in range(num_nodos):
                if (red_iteracion_x[s,i]!=10**8):
                    flujo = flujo + red_iteracion_x[s,i]
            flujo=flujo + int(nodo_ofe_dem[i])
            if (flujo>=0):

                if(nodos_hojas_raices[i,0]!=0):
                    for j in range(int(nodos_hojas_raices[i,0])-1):
                        aristas_temporales.append(int(flujo/nodos_hojas_raices[i,0]))
                    aristas_temporales.append(int(flujo/nodos_hojas_raices[i,0])+flujo%nodos_hojas_raices[i,0])
                    ar=0
                for k in range(num_nodos):
                    if(red_iteracion_c[i,k] != 10**8):
                        
                        red_iteracion_x[i,k]=aristas_temporales[ar]
                        ar=ar+1
    it=0
    
    while(cos_red_pos==0):
        it=it+1
        z_i=0
        funcion_i=[]
        for i in range(num_nodos):
            for j in range(num_nodos):
                if (red_iteracion_c[i,j] != 10**8):
                    z_i=z_i+(red_iteracion_c[i,j]*red_iteracion_x[i,j])
                    if (lista_vaciaM(funcion_i)==True):
                        funcion_i.append(f"({red_iteracion_c[i,j]})*({red_iteracion_x[i,j]})")
                    else:
                        funcion_i.append(f"+({red_iteracion_c[i,j]})*({red_iteracion_x[i,j]})")
                    

                    

                    


        print(f"z={funcion_i}\n Z={z_i}")

        print("Calculamos las variables W_i")
        
         #se llena segun las aristas que participen en el arbol
        for i in range(num_nodos-1):
            indices_ecuaciones[i,0]=10**8
            indices_ecuaciones[i,1]=10**8
            indices_ecuaciones[i,2]=10**8

        counter = 0
        for i in range(num_nodos):
            for j in range(num_nodos):
                
                if (red_iteracion_c[i,j] != 10**8):
                    print(f"w_{i}-w_{j}={red_iteracion_c[i,j]}")
                    indices_ecuaciones[counter,0]=i           #0-1=2 subindices para resolver el sistema
                    indices_ecuaciones[counter,1]=j
                    indices_ecuaciones[counter,2]=red_iteracion_c[i,j] #guardamos una referencia de que 
                    print(indices_ecuaciones[i,0:])  
                    print(f"w_{i}-w_{j}={red_iteracion_c[i,j]}")  
                    counter += 1
                
                                  
        print("indices ecuaciones\n ") 
        print(indices_ecuaciones)                                      #w_i - w_j=c_ij    #lo que nos deja guardar las ecuaciones
        for i in range(num_nodos):#llenamos de M los valores de w_i
            w_i[i,0]=10**8
                                                            
        w_i[num_nodos-1,0]=0 #hacemos que el nodo w_k = 0 para poder resolver el sistema de ecuaciones
        w_lleno=0
        while(w_lleno!=1):#hasta que en w_1 ya no queden M por resolver no deja de resolver las ecuaciones
            for i in range(num_nodos):
                if (w_i[i,0] != 10**8):
                    for j in range(num_nodos-1):
                       
                        if (indices_ecuaciones[j,0] == i):
                            if (w_i[int(indices_ecuaciones[j,1]),0] == 10**8):
                                w_i[int(indices_ecuaciones[j,1]),0] =w_i[i,0]-indices_ecuaciones[j,2]

                        if (indices_ecuaciones[j,1]==i):
                            if (w_i[int(indices_ecuaciones[j,0]),0] == 10**8):
                                w_i[int(indices_ecuaciones[j,0]),0]=indices_ecuaciones[j,2]+w_i[i,0]
                                
                           
                            
            w_lleno=1
            for i in range(num_nodos):
                if(w_i[i,0]==10**8):
                    w_lleno=0
            #Procederemos a calcular la matriz  Z_ij (costos reducidos)
            #  para saber si se necesita otra iteracion
        
        cos_red_pos=1
        z_maxima=[]
        maximo_z=0
        nodo_productor=10**8
        nodo_destino=10**8
        for i in range(num_nodos): #vaciamos la matriz por iteraciones anteriores
            for j in range(num_nodos):
                red_iteracion_z[i,j]=10**8
        for i in range(num_nodos): #llenamos la matriz con los arcos que no pertenecen a la matriz C_ij
            for j in range(num_nodos):
                if (red[i,j]==red_iteracion_c[i,j]):
                    red_iteracion_z[i,j]=0
                else:
                    red_iteracion_z[i,j]= w_i[i,0]-w_i[j,0]-red[i,j]
                    z_maxima.append(red_iteracion_z[i,j])
                    if (red_iteracion_z[i,j]>0):
                        cos_red_pos=0
        #pdb.set_trace()
        

                    #asignamos los costos reducidos y verificamos si existen costos reducidos positivos
        if (cos_red_pos==0):#ya que aun no se llega a la z minima procedemos a calcular 
                               #la solucion inicial de la nueva iteracion
            maximo_z=max(z_maxima)
            for i in range(num_nodos):
                for j in range(num_nodos):
                    if (red_iteracion_z[i,j]==maximo_z):#coordenadas de la nueva arista basica
                        nodo_productor=i
                        nodo_destino=j # son importantes para balancear el problema
            delta=10**7 #inicializo a delta en M pero una M diferente
            #agrego el arco a la base
            #determino que arco abandona la base
            
            #hay que buscar que aristas y nodos forman el bucle al agregar el nuevo nodo a la base
            nodos_bucle=[]
            nodos_bucle.append(nodo_destino)
            
            nodo_temporal=nodo_destino
            exceso=0
            while(nodo_temporal != nodo_productor):
                for i in range(num_nodos):
                    
                    if(red_iteracion_c[i, nodo_temporal] != 10**8):
                        nodos_bucle.append(i)
                        nodo_temporal=i

                exceso=exceso+1
                if (exceso==num_nodos**2):
                    nodos_bucle.append(nodo_productor)
                    nodo_temporal=nodo_productor
                    

                
            
            
           
            nodos_bucle=nodos_bucle[::-1]
            x_minima=[]
            minimo_x=0
            for i in range(len(nodos_bucle)-1):
                x_minima.append(red_iteracion_x[i,(i+1)])
            minimo_x=min(x_minima)
            arista_en_bucle=0
            arista_i_sale=10**8
            arista_j_sale=10**8
            #buscamos la arista minima que saldra de la base
            for i in range(num_nodos):
                for j in range(num_nodos):
                    for k in range(len(nodos_bucle)):
                        if (i==nodos_bucle[k] and j==nodos_bucle[k]):
                            arista_en_bucle=1
                    if(minimo_x==red_iteracion_x[i,j] and arista_en_bucle==1 ):
                        delta=red_iteracion_x[i,j]
                        arista_i_sale=i
                        arista_j_sale=j
            nodo_temporal=nodo_destino
            exceso=0
            ultimo_nodo=np.ones((1,2))
            while(nodo_temporal != nodo_productor):
                for i in range(num_nodos):
                    if(red_iteracion_c[i, nodo_temporal] != 10**8):
                        red_iteracion_x[i,nodo_temporal]=red_iteracion_x[i,nodo_temporal]-delta
                        ultimo_nodo[0,0]=i
                        ultimo_nodo[0,1]=nodo_temporal
                exceso=exceso+1
                if (exceso==num_nodos**2):
                    red_iteracion_x[int(ultimo_nodo[0,0]),nodo_productor]=red_iteracion_x[int(ultimo_nodo[0,0]),nodo_productor]+delta
                    nodo_temporal=nodo_productor

            #ya solo falta sacar la arista de la base y meter la nueva a la base
            red_iteracion_x[arista_i_sale,arista_j_sale]=10**8
            red_iteracion_c[arista_i_sale,arista_j_sale]=10**8
            red_iteracion_x[nodo_productor,nodo_destino]=delta
            red_iteracion_c[nodo_productor,nodo_destino]=red[nodo_productor,nodo_destino]


    red_iteracion_x_impresion=np.full((num_nodos,num_nodos),"___________")
    red_iteracion_c_impresion=np.full((num_nodos,num_nodos),"___________")
    red_iteracion_z_impresion=np.full((num_nodos,num_nodos),"___________")
    red_impresion=np.full((num_nodos,num_nodos),"___________")

    for i in range(num_nodos):
        for j in range(num_nodos):
            if (red_iteracion_x[i,j] != 10**8):
                red_iteracion_x_impresion[i,j]=red_iteracion_x[i,j]
            else:
                red_iteracion_x_impresion[i,j]="X"

            if (red_iteracion_c[i,j] != 10**8):
                red_iteracion_c_impresion[i,j]=red_iteracion_c[i,j]
            else:
                red_iteracion_c_impresion[i,j]="X"

            if (red_iteracion_z[i,j] != 10**8):
                red_iteracion_z_impresion[i,j]=red_iteracion_z[i,j]
            else:
                red_iteracion_z_impresion[i,j]="X"
            
            if (red[i,j] != 10**8):
                red_impresion[i,j]=red[i,j]
            else:
                red_impresion[i,j]="X"
    z_i=0
    funcion_i=[]
    for i in range(num_nodos):
        for j in range(num_nodos):
            if (red_iteracion_c[i,j] != 10**8):
                z_i=z_i+(red_iteracion_c[i,j]*red_iteracion_x[i,j])
            if (lista_vaciaM(funcion_i)==True):
                funcion_i.append(f"({red_iteracion_c[i,j]})*({red_iteracion_x[i,j]})")
            else:
                funcion_i.append(f"+({red_iteracion_c[i,j]})*({red_iteracion_x[i,j]})")
                



    print(red)
    print("\nTu matriz de adyasencia era: ")
    print(f"  {lista_nodos[0:num_nodos]}")
    for i in range(num_nodos):
        print(f"{chr(65+i)} {red_impresion[i,0:]}")
    print("Tu matriz de costos (C_ij) es: ")
    print(f"  {lista_nodos[0:num_nodos]}")
    for i in range(num_nodos):
        print(f"{chr(65+i)} {red_iteracion_c_impresion[i,0:]}")
    print("Tu matriz de flijo (X_ij) es: ")
    print(f"  {lista_nodos[0:num_nodos]}")
    for i in range(num_nodos):
        print(f"{chr(65+i)} {red_iteracion_x_impresion[i,0:]}")
    print("Tu matriz de precios sombra es: ")
    print(f"  {lista_nodos[0:num_nodos]}")
    for i in range(num_nodos):
        print(f"{chr(65+i)} {red_iteracion_z_impresion[i,0:]}")
    

    print(f"z={funcion_i}\n Z={z_i}")
    print(f"Acabo en la iteracion{it}")

def metodo3(matriz, lista_modificaciones):
    print("Metodo del arbol de expansion minima")
    #print(matriz)
    
    print(lista_modificaciones)
    
    #lista de nodos que no pertene aun al grafo final
    n= int(math.sqrt(matriz.size)) 
    arbol_minimo=np.ones((n,n))
    for i in range(n):
        for j in range(n):
            arbol_minimo[i,j]=10**8
    no_final=np.ones((1, n ))
    menor=[]
    minimo=10**8
    for i in range(n):
        no_final[0,i]=65+i
    #lista de nodos que ya pertenecen al grafo final
    si_final=[]
    index=10**8
    nodo_valido=0

    
    while (int(no_final.sum()) != n):#mientras existan nodos sueltos (o sea no se encuentren en el grafo final)
                                #el programa seguira buscando la siguiente mejor arista que complete el arbol
        for i in range(matriz.size):#valida si los nodos que una la arista ya estan contemplados en el arbol final
            for j in range(len(si_final)):
                if (lista_modificaciones[i,0] == si_final[j]):
                    nodo_valido=nodo_valido+1
                if (lista_modificaciones[i,2] == si_final[j]):
                    nodo_valido=nodo_valido+1
            print(f"nodo valido vale {nodo_valido}")
            if(nodo_valido==2):
                lista_modificaciones[i,1]=10**8 #si ambos nodos ya estan en el arbol entonces la arista ya no es relevante
            nodo_valido=0                           #y podemos igualarla a M (10**8) 
        minimo=10**8
        menor=[]
        index=10**8
        for i in range(matriz.size):
            if (lista_vaciaM(si_final)==True):
                menor.append(lista_modificaciones[i,1])
            else:
                for j in range(len(si_final)):
                    if (lista_modificaciones[i,0]==si_final[j] or lista_modificaciones[i,2]== si_final[j]):
                        menor.append(lista_modificaciones[i,1])

        minimo=min(menor)
        print(minimo)
        
        for i in range(matriz.size):
            print(f"minimo= {minimo}")
            print(f"tiene que ser igual a {lista_modificaciones[i,1]}")
            if (minimo==lista_modificaciones[i,1]):
                if (lista_vaciaM(si_final)==True):
                    index=i
                else:
                    for j in range(len(si_final)):
                        if (lista_modificaciones[i,0]==si_final[j] or lista_modificaciones[i,2]== si_final[j]):
                            index=i


        if (index==10**8):
            print("Algo salio muy mal  CORREEEEE")#significaria que aun no se conecta todo el arbol pero ya no hay aristas factibles
        arbol_minimo[(int(lista_modificaciones[index,0])-65), (int(lista_modificaciones[index,2])-65)]=float(lista_modificaciones[index,1])
        si_final.append(lista_modificaciones[index,0])
        si_final.append(lista_modificaciones[index,2])
        lista_modificaciones[index,1]=10**8
        for k in range(n):
            if (int(no_final[0,k])==int(lista_modificaciones[index,0])):
                no_final[0,k]=1
            if (int(no_final[0,k])==int(lista_modificaciones[index,2])):
                no_final[0,k]=1


        si_final=list(set(si_final))
        print("Iniciamos el rellenado de la matriz\n\n\n\n")
        print("matriz")
        print(arbol_minimo)
        print("nodos finales")
        for i in range(len(si_final)):
            print(chr(int(si_final[i])))
        print("nodos no finales")
        print(no_final)
    
        print(f"la condicion se rompe cuando {int(no_final.sum())} ={n}")

    print("Matriz final\n\n\n\n")
    print(arbol_minimo)
    for i in range(len(si_final)):
        print(chr(int(si_final[i])))
    print(no_final)
    print(f"lista modificaciones\n {lista_modificaciones}")
    lista_nodos = np.array(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R',
                    'S','T','U','V','W','X','Y','Z'])
    z=0
    contador=0
    for i in range(n):
        for j in range(n):
            if (arbol_minimo[i,j] == 10**8):
                contador=contador+1

    matriz_imp=np.full((n,n),"espero_funcione_lo_que_voy_a_intentar")
    for i in range(n):
        for j in range(n):
            if (matriz[i,j] ==10**8):
                matriz_imp[i,j]="X"
            else:
                matriz_imp[i,j]=str(matriz[i,j])

    print("Tu matriz de adyacencia inicial es:\n")
    print(f"  {lista_nodos[0:n]}")
    for i in range(n):
        print(f"{chr(65+i)} {matriz_imp[i,0:]}")

    z=arbol_minimo.sum()-(contador*(10**8))
    arbol_minimo_imp=np.full((n,n),"espero_funcione_lo_que_voy_a_intentar")
    for i in range(n):
        for j in range(n):
            if (arbol_minimo[i,j] == 10**8):
                arbol_minimo_imp[i,j]="X"
            else:
                arbol_minimo_imp[i,j]=str(arbol_minimo[i,j])

    print("Resultado final, arbol de expansion minida del grafo:\n")
    print(f"  {lista_nodos[0:n]}")
    for i in range(n):
        print(f"{chr(65+i)} {arbol_minimo_imp[i,0:]}")

    print(f"Z={z}")
    
    return arbol_minimo

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



@unique
class Artificial(Enum):
    ORIGENES = 1
    DESTINOS = 2

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

    # Variables calculadas
    mat_dec = []
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

            # print(self.oferta_origenes, self.demanda_destinos)

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

            campos_disponibles = [x[0] and x[1] for x in it.product(
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

            campos_disponibles = [x[0] and x[1] for x in it.product(
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

            campos_disponibles = [x[0] and x[1] for x in it.product(
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



def main():
    print(
        """
      ___        _   _           _               _             ____  
     / _ \ _ __ | |_(_)_ __ ___ (_)______ _  ___(_) ___  _ __ |___ \ 
    | | | | '_ \| __| | '_ ` _ \| |_  / _` |/ __| |/ _ \| '_ \  __) |
    | |_| | |_) | |_| | | | | | | |/ / (_| | (__| | (_) | | | |/ __/ 
     \___/| .__/ \__|_|_| |_| |_|_/___\__,_|\___|_|\___/|_| |_|_____|
          |_|                                                        
    """)
    print("Por:")
    print("Valdez Osorio Jorge Aurelio")
    print("Hernandez Martinez Abraham")
    print("Ramiréz Calnacasco Ulises")

    print()

    print("Hola usuario.")
    print("¿Que metodo quieres resolver hoy?")
    print("1. Transporte - Transbordo")
    print("2. Ramificacion")
    print("3. Enumeracion")
    print("4. Dijkstra")
    print("5. Floyd")
    print("6. Arbol de expansion minima")
    print("7. Simplex para redes")
    metodo = input_int("")

    if metodo == 1:
        transporte = Transporte()
    elif metodo == 2:
        ram = Ramificacion()
        ram.solicitar_datos()
        ram.solve()
    elif metodo == 3:
        enumeracion()
    elif metodo == 4:
        ruta = RutaCorta()
        ruta.solicitar_datos()
        # ruta.test_data(1)
        ruta.solve()
    elif metodo == 5:
        floyd = Floyd()
        floyd.solicitar_datos()
        # floyd.test_data(1)
        floyd.solve()
    elif metodo == 6:
        arbol_exp_minima()
    elif metodo == 7:
        simplex_redes()

if __name__ == "__main__":
    main()
