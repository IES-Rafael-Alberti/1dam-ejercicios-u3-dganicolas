#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por pantalla su producto escalar.

def multiplicar(lista,lista2):
    return tuple(lista[i]*lista2[i] for i in range(len(lista)))

def main():
    lista= (1,2,3)
    lista2= (-1,0,2)
    print(multiplicar(lista, lista2))
if __name__=="__main__":
    main()