#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.

import copy


def pedir_palabra():
    palabra=input("dame una palabra: ")
    return palabra

def palindromo(palabra):
    lista_palabra=[]
    for i in range(len(palabra)):
        lista_palabra. append(palabra[i])
    lista_palabra_al_revez = copy.deepcopy(lista_palabra)
    lista_palabra_al_revez.reverse()
    lista1 =", ".join(map(str,lista_palabra))
    lista2 =", ".join(map(str,lista_palabra_al_revez))
    if lista_palabra == lista_palabra_al_revez:
        return f"la palabra es un palindromo // {lista1} / {lista2}"
    else:
        return f"no es un palindromo // {lista1} / {lista2}"

def main():
    palabra = pedir_palabra()
    print(palindromo(palabra))

if __name__=="__main__":
    main()