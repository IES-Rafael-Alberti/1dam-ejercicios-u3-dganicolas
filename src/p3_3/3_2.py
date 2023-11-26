#Dado el conjunto de números enteros:

#numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#Crea un conjunto pares que contenga los números pares del conjunto numeros.------------
#Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.-----------------
#Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.

def crear_pares(numeros):
    numeros_pares=set()
    for e in numeros:
        par=e%2
        if par==0:
            numeros_pares.add(e)
    return numeros_pares

def crear_3(numeros):
    numeros_3=set()
    for e in numeros:
        par=e%3
        if par==0:
            numeros_3.add(e)
    return numeros_3

def inter(conjuntos_pares:set,conjuntos_3:set):
    pares_y_multiplos_de_tres=conjuntos_pares.intersection(conjuntos_3)#en mi idea esto debe de darme algo
    return pares_y_multiplos_de_tres

def main():
    numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
    conjuntos_pares=crear_pares(numeros)
    conjuntos_3=crear_3(numeros)
    interseccion=inter(conjuntos_pares,conjuntos_3)
    print(interseccion)
    print(conjuntos_3)
    print(conjuntos_pares)


if __name__=="__main__":
    main()