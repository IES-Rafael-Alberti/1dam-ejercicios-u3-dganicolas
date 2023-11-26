#Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.


def preguntar_usuario():
    lista=input("Dame palabras separadas por comas (hola:hello,adios:bay): ")
    return lista

def tradducion_frase(frase:str,diccionario:dict):
    lista=list(frase.split(" "))
    for i in range (len(lista)):
        if lista[i] in diccionario:
            ingles=diccionario[lista[i]]
            lista.append(ingles)
            lista.remove(lista[i])
        else:
            lista.append(lista[i])
            lista.remove(lista[i])
    return lista

def pregunta_frase():
    lista=input("Dame una frase en español: ")
    return lista

def crear_lista(palabras):
    en_es={}
    pares = palabras.split(',')
    for par in pares:
        clave, valor = par.split(':')
        en_es[clave] = valor
    return en_es

def final(traduccion):
    frase=""
    for i in range(len(traduccion)):
        palabra=traduccion[i]
        frase+=palabra+" "
    print(frase)

def main():
    palabras=preguntar_usuario()
    diccionario=crear_lista(palabras)
    frase=pregunta_frase()
    traduccion=tradducion_frase(frase,diccionario)
    final(traduccion)

if __name__=="__main__":
    main()