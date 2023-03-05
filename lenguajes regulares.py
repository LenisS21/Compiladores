
#cosas que falta

#Debe permitir que el usuario ingrese como mínimo dos alfabetos y agregar el simbolo vacio.

A = set()           #Alfabetos
B = set()

n = int(input("cuantos símbolos desea ingresar: "))
i = 0; j = 0

for i in range(i,n):
    simbolo = input("ingrese un símbolo del alfabeto 1: ")
    A.add(simbolo)

for j in range(j,n):
    simbolo = input("ingrese un símbolo del alfabeto 2: ")
    B.add(simbolo)

print(f"este es: {A}, este es {B}")

print(f"\nUnion: {A.union(B) }")                               #Realiza la unión de alfabetos.

def diferencia():
    if A.difference(B):
        print(f"\nDiferencia: {A.difference(B)}")               #Realiza la diferencia entre alfabetos.               
    else:
        print("\nLos conjuntos son iguales")

def interseccion():
    if A.intersection(B):
        print(f"\nInterseccion: {A.intersection(B)}")            #Realiza la intersección entre alfabetos.
    else:
        print("\nno hay elementos iguales")                           

diferencia()

interseccion()

