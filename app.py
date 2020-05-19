from enumeracion import enumeracion
from transporte import Transporte
from ramificacion import Ramificacion


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
    metodo = input_int("")

    if metodo == 1:
        transporte = Transporte()
    elif metodo == 2:
        ram = Ramificacion()
        ram.solve()
    elif metodo == 3:
        enumeracion()


if __name__ == "__main__":
    main()
