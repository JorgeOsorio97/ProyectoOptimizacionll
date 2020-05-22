from typing import Dict, Tuple
from enum import Enum, unique
from copy import copy
import pdb

import numpy as np
from scipy.optimize import linprog
from binarytree import Node


# UTILIDADES

# Funciones utilitarias

def input_int(message=""):
    return int(input(message))


def try_again():
    input_int("")

# ENUMS


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


if __name__ == "__main__":
    ram = Ramificacion()
    # ram.solicitar_datos()
    ram.test_data(1)
    x, z = ram.solve()
    print("Los valores para x son {}".format(x))
    print("Z={}".format(z))
