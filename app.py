from enumeracion import enumeracion
from transporte import Transporte
from ramificacion import Ramificacion
from rutacorta import RutaCorta
from floyd import Floyd
from arb_ex_min import arbol_exp_minima


def input_int(message=""):
    return int(input(message))


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
    print("¿Qué metodo quieres resolver hoy?")
    print("1. Transporte")
    print("2. Ramificacion")
    print("3. Enumeracion")
    print("4. Dijkstra")
    print("5. Floyd")
    print("6. Arbol de expansion minima")
    metodo = input_int("")

    if metodo == 1:
        transporte = Transporte()
    elif metodo == 2:
        ram = Ramificacion()
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
    elif 6:
        arbol_exp_minima()


if __name__ == "__main__":
    main()
