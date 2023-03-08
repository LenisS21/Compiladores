import random

__vacio = '$'
__Alfabetos = []
__UAlfabetos = ()


def addAlfabetos(n):
    c = 0
    for c in range(c, n):
        __Alfabetos.append(tuple(addAlfa(c)))


def addAlfa(c):

    alfa = set()
    n = int(input("\nCuantos simbolos desea que tenga su alfabeto?: "))
    return generadorAlfa(n, alfa, c)


def generadorAlfa(n, alfa, c):
    if n == 0:
        alfa = __vacio
        return alfa
    else:
        i = 0

        for i in range(i, n):
            aux = input(f"\n Ingrese los simbolos de alfabeto {c+1}: ")
            alfa.add(aux)
    print("Alfabeto creado ;)")
    return alfa


def unionAlfa(i, j):
    if set(__Alfabetos[i]).union(__Alfabetos[j]) != set():
        return set(__Alfabetos[i]).union(__Alfabetos[j])
    else:
        return set().add(__vacio)


def interseccionAlfa(i, j):
    if set(__Alfabetos[i]).intersection(__Alfabetos[j]) != set():
        return set(__Alfabetos[i]).intersection(__Alfabetos[j])
    else:
        return __vacio


def diferenciaAlfa(i, j):
    if set(__Alfabetos[i]).difference(__Alfabetos[j]) != set():
        return set(__Alfabetos[i]).difference(__Alfabetos[j])
    else:
        return __vacio


def cerraduraEstrella():
    indice = int(input("Ingrese el índice del alfabeto: ")) - 1
    n = int(input("Ingrese el número de palabras a generar: "))
    alfa = __Alfabetos[indice]
    cerraduraEstrella = set()
    for i in range(n):
        nueva_palabra = ''.join(random.choices(
            list(alfa), k=random.randint(0, len(alfa))))
        if nueva_palabra == '':
            cerraduraEstrella.add(__vacio)
        else:
            cerraduraEstrella.add(nueva_palabra)
    print(f"Cerradura de estrella de {alfa}: {cerraduraEstrella}")


def getAlfabetos():
    return __Alfabetos


def mostrar():
    for i, alfa in enumerate(__Alfabetos):
        print(f"Alfabeto {i+1}: {alfa}", "\n")
