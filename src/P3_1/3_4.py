""""
Ej 3.1.4
Escribir un programa que pregunte al usuario 
los numeros ganadores de la loteria primitiva
y los muestre por pantalla ordenados de menor a mayor
6 numeros de 1 a 49 + reintegro de 0 a 9 
los 6 numeros deben ser unicos
"""
import os
def lista():
    """le introduces los items de la lista y te retorna la lista"""
    lista = []
    numeros=""
    for i in range(0,8):
        numeros = int(input(f"dame el numero {i+1}: "))
        if (numeros is not lista) and numeros>0 and numeros<50:
            while numeros in lista:
                print("error el numero ha sido introducido previamente")
                numeros = int(input(f"dame el numero {i+1}: "))
            lista.append(numeros)
        else:
            print("error el numero no ha sido introducido correctamente")
    return lista

def main():
    listaa=lista()
    listaa.sort
    os.system("cls")
    print(f"tu numero son")
    print(*listaa)
if __name__ =="__main__":
    main()