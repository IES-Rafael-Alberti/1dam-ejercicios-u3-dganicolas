#Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.

def ordenar_lista(lista):
    return lista.sort()

def main():
    lista=[50, 75, 46, 22, 80, 65, 8]
    ordenar_lista(lista)
    print(", ".join(map(str,lista)))

if __name__=="__main__":
    main()