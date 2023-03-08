from alfabeto import *
import os
from lenguaje import *


def menuPrincipal():
    aux = int(input("Bienvenido\nEste es un programa que genera lenguajes y alfabetos.\nQue desea ejecutar primero?\n\n"
                    "1.Generador de alfabetos\n2.Generador de lenguajes\n\nSeleccione: "))
    if aux == 1:
        menuAlfabeto()
    else:
        if aux == 2:
            menuLenguaje()


def men():
    print("Bienvenido")

    print("\nEste es un generador de palabras a partir de un alfabeto creado por usted.\n"
          "Cada alfabeto que usted desee crear se guardara en un conjunto representado por un numero.\n"
          "Podra realizar acciones y operaciones como: ingresar alfabetos, operaciones entre 2 alfabetos como: union, intersección, diferencia de alfabetos\ny por ultimo cerradura de estrealla de un alfabeto.\n"
          "\n(Tenga en cuenta que se generara un conjunto vacio representado por el simbolo $)", "\n")

    opcion = int(input("Que deseas realizar?: "
                       "\n1. ingresar alfabetos"
                       "\n2. Union de alfabetos"
                       "\n3. Interseccion de alfabetos"
                       "\n4. Diferencia de alfabetos"
                       "\n5. Cerradura estrella de un alfabeto"
                       "\n6. Menu Principal"
                       "\n7. Salir"
                       "\n Elige opcion de (1-7): "))
    return opcion


def menuAlfabeto():
    while True:
        opcion = men()
        os.system('cls' if os.name == 'nt' else 'clear')

        if opcion == 1:
            n = int(input("\n Ingrese cuantos alfabetos desea crear?: "))
            addAlfabetos(n)
            print("\n")

        if opcion == 2:
            print(f"Union de alfabetos\n")
            print(getAlfabetos())

            i = int(input("\nIngresa primer alfabeto: "))
            j = int(input("\nIngresa segundo alfabeto: "))
            print(
                f"\nUnion de alfabeto {i} y alfabeto {j}: {unionAlfa(i-1, j-1)}\n")

        if opcion == 3:
            print(f"Interseccion de alfabetos\n")
            i = int(input("\nIngresa primer alfabeto: "))
            j = int(input("\nIngresa segundo alfabeto: "))
            print(
                f"\nInterseccion de alfabeto {i} y alfabeto {j}: {interseccionAlfa(i-1, j-1)}\n")

        if opcion == 4:
            print(f"Diferencia de alfabetos\n")
            i = int(input("\nIngresa primer alfabeto: "))
            j = int(input("\nIngresa segundo alfabeto: "))
            print(
                f"\nDiferencia de alfabeto {i} y alfabeto {j}: {diferenciaAlfa(i-1, j-1)}\n")

        if opcion == 5:
            cerraduraEstrella()

        if opcion == 6:
            menuPrincipal()

        if opcion == 7:
            break


def menn():
    print("Bienvenido\n\n")

    print("Este es un generador de lenguaje a partir de un alfabeto creado por usted.\n"
          "Cada lenguaje que usted desee crear se guardara en un conjunto representado por un numero.\n"
          "Podra elegir las operaciones y acciones de los lenguajes a travez del menu.\n\n"
          "(ADVERTENCIA: si NO ha generados palabras las funciones fallaran, si es asi se le recomienda saltar al menu de alfabetos.)\n")
    opcion = int(input("que deseas realizar?:"
                 "\n1. Generar lenguajes"
                       "\n2. Union de lenguajes"
                       "\n3. Interseccion de lenguajes"
                       "\n4. Diferencia de lenguajes"
                       "\n5. Cardinalidad del lenguaje"
                       "\n6. Concatenacion de lenguajes"
                       "\n7. Inversa de un lenguaje"
                       "\n8. Potencia de un lenguaje"
                       "\n9. Menu Principal"
                       "\n10. Salir"
                       "\nElige una opcion de (1-10): "))
    return opcion


def menuLenguaje():
    while True:
        opcion = menn()
        os.system('cls' if os.name == 'nt' else 'clear')

        if opcion == 1:
            lenguaje1 = {'ccd', 'dccc', '$', 'cad', 'ccb'}
            lenguaje2 = {'ee', 'dggf', '$', 'fefg', 'gf'}
            print("Lenguajes generados correctamente\n")

        if opcion == 2:
            print(unionLenguaje(lenguaje1, lenguaje2), "\n\n")
        if opcion == 3:
            print(interseccionLenguaje(lenguaje1, lenguaje2), "\n\n")
        if opcion == 4:
            print(diferenciaLenguaje(lenguaje1, lenguaje2), "\n\n")
        if opcion == 5:
            print(cardinalidadLenguaje(lenguaje1), "\n\n")
        if opcion == 6:
            print(concatenacionLenguajes(lenguaje1, lenguaje2), "\n\n")
        if opcion == 7:
            print(inversaLenguaje(lenguaje1), "\n\n")
        if opcion == 8:
            print(potenciaLenguaje(lenguaje1), "\n\n")
        if opcion == 9:
            menuPrincipal()
        if opcion == 10:
            break


menuPrincipal()
