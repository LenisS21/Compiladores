from alfabeto import *
palabras = getAlfabetos()
__vacio = '$'


def generarLenguaje1():
    n = int(input("alfabeto para generar palabras: "))
    alfa = palabras
    lenguaje1 = []
    for i in range(n):
        nueva_palabra = ''.join(random.choices(
            list(alfa), k=random.randint(0, len(alfa))))
        if nueva_palabra == '':
            lenguaje1.add(__vacio)
        else:
            lenguaje1.add(nueva_palabra)
    return lenguaje1


def generarLenguaje2():
    n = int(input("alfabeto para generar palabras: "))
    alfa = getAlfabetos[n-1]
    lenguaje2 = []
    for i in range(n):
        nueva_palabra = ''.join(random.choices(
            list(alfa), k=random.randint(0, len(alfa))))
        if nueva_palabra == '':
            lenguaje2.add(__vacio)
        else:
            lenguaje2.add(nueva_palabra)
    return lenguaje2


def unionLenguaje(lenguaje1, lenguaje2):
    if set(lenguaje1).union(set(lenguaje2)) != __vacio:
        return set(lenguaje1).union(lenguaje2)
    else:
        return __vacio


def interseccionLenguaje(lenguaje1, lenguaje2):
    if set(lenguaje1).intersection(set(lenguaje2)) != __vacio:
        return set(lenguaje1).intersection(set(lenguaje2))
    else:
        return __vacio


def diferenciaLenguaje(lenguaje1, lenguaje2):
    if set(lenguaje1).difference(set(lenguaje2)) != __vacio:
        return set(lenguaje1).difference(set(lenguaje2))
    else:
        return __vacio


def cardinalidadLenguaje(lenguaje1):
    return len(lenguaje1)


def concatenacionLenguajes(lenguaje1, lenguaje2):
    concatenacion = set()
    for palabra1 in lenguaje1:
        for palabra2 in lenguaje2:
            concatenacion.add(palabra1 + palabra2)
    return concatenacion


def inversaLenguaje(lenguaje1):
    inversa = set()
    for palabra in lenguaje1:
        inversa.add(palabra[::-1])
    return inversa


def potenciaLenguaje(lenguaje1, potencia):
    if potencia == 0:
        return {""}
    else:
        potencia_anterior = potenciaLenguaje(lenguaje1, potencia - 1)
        potencia_actual = set()
        for palabra in lenguaje1:
            for palabra_anterior in potencia_anterior:
                potencia_actual.add(palabra + palabra_anterior)
        return potencia_actual
