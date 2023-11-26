def pedir_palabra()->tuple:
    palabra = tuple(input("dame una palabra: "))
    return palabra

def contar_vocales(palabra:tuple)->tuple:
    vocales = (["a",0],["e",0],["i",0],["o",0],["u",0],)
    for vocal in vocales:
        vocal[1] =palabra.count(vocal[0])
    return vocales

def mostrarVocales():
    print()

def main():
    palabra=pedir_palabra()
    vocales = contar_vocales(palabra)
    print(*vocales)

if __name__=="__main__":
    main()