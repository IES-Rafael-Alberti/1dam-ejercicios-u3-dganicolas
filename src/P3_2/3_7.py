#Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato
import os

def preguntar_al_usuario(numero):
    if numero %2==0:
        i="precio"
    else:
        i="producto"
    clase=input(f"dime el {i}: ")
    return clase

def parar_usuario():
    return input('escriba "S" para finalizar o pulsa ENTER para un nuevo producto ')

def main():
    d={}
    lista = ""
    productos=1
    while lista!="S":
        os.system("cls")
        print(f"producto {productos}")
        numero=1
        clase = preguntar_al_usuario(numero)
        numero=2
        objeto=preguntar_al_usuario(numero)
        d[clase]=objeto
        productos+=1
        lista=parar_usuario()
    os.system("cls")
    print("lista de la compra")
    suma=0
    for i in d.keys():
        suma+=int(d[i])
        print(f"{i}  {d[i]}")
    print(f"total   {suma}")


if __name__=="__main__":
    main()