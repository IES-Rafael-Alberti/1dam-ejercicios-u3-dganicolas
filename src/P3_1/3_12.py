#Escribir un programa que almacene las matrices A=(123456) y B=(−100111) en una lista y muestre por pantalla su producto. Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.

#preguntar diego si esta bien

def multiplicar(lista,lista2):
    return tuple(lista[i]+lista2[i] for i in range(len(lista)))

def main():
    lista= [1,2,3,4,5,6]
    lista2= [-1,0,0,1,1,1]
    print(multiplicar(lista, lista2))
if __name__=="__main__":
    main()