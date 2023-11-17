#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.


def crearLista():
    return list(i+1 for i in range(10))

def main():
    numeros = crearLista()
    numeros.reverse()
    numeros =", ".join(map(str,numeros))
    print(numeros)

if __name__=="__main__":
    main()