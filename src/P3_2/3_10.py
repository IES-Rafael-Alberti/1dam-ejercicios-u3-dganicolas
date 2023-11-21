#Escribir un programa que permita gestionar la base de datos de clientes de una empresa. Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente), donde preferente tendrá el valor True si se trata de un cliente preferente. El programa debe preguntar al usuario por una opción del siguiente menú: (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes, (5) Listar clientes preferentes, (6) Terminar. En función de la opción elegida el programa tendrá que hacer lo siguiente:

#Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
#Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
#Preguntar por el NIF del cliente y mostrar sus datos.
#Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
#Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
#Terminar el programa.
import os
def preguntar_nif():
    clase=input(f"dime el nif cliente: ")
    return clase

def mostrar_clientes_vip(d):
    print ({cliente: preferente for cliente, preferente in d.items() if preferente['preferente'] ==True})

def mostrar_cliente(d):
    seguro="S"
    clase=input(f"dime el cliente a eliminar: ")
    while seguro=="S":
        if clase in d:
            seguro="N"
        if seguro=="S":
            clase=input(f"***ERROR*** - dime el cliente a eliminar: ")
    print(d[clase])

def preguntar_datos(d:dict,clase):
    datos=("nombre", "dirección", "teléfono", "correo", "preferente")
    for i in range (len(datos)-1): 
        dato=input(f"dime {datos[i]} del cliente: ")
        d[clase][str(datos[i])]=dato
    preferente=input("es el cliente preferente?(si/no)")
    if preferente=="si":
        d[clase][str(datos[4])]=True
    if preferente=="no":
        d[clase][str(datos[4])]=False

def parar_usuario():
    numero=int(input('(1) Añadir cliente\n (2) Eliminar cliente\n (3) Mostrar cliente\n (4) Listar todos los clientes\n (5) Listar clientes preferentes\n (6) Terminar\n'))
    while numero!=1 and numero!=2 and numero!=3 and numero!=4 and numero!=5 and numero!=6:
        os.system("cls")
        numero=int(input('***ERROR***\n(1) Añadir cliente\n (2) Eliminar cliente\n (3) Mostrar cliente\n (4) Listar todos los clientes\n (5) Listar clientes preferentes\n (6) Terminar\n'))
    return numero

def lista_clientes(d):
    for i,j in d.items():
        print(f"{i} {j}")

def preguntar_borrado(pagado,deuda,d):
    seguro="S"
    clase=input(f"dime el cliente a eliminar: ")
    while seguro=="S":
        if clase in d:
            seguro="N"
        if seguro=="S":
            clase=input(f"***ERROR*** - dime el cliente a eliminar: ")
    del d[clase]
    return pagado,deuda

def main():
    d={1: {'nombre': '1', 'dirección': '1', 'teléfono': '11', 'correo': '1', 'preferente': False}, 2: {'nombre': '2', 'dirección': '2', 'teléfono': '2', 'correo': '22', 'preferente': True}}
    lista = 0
    deuda=0
    pagado=0
    while lista!=6:
        os.system("cls")
        lista=parar_usuario()
        if lista==1:
            clase = preguntar_nif()
            d[clase]={}
            preguntar_datos(d,clase)
        if lista==2:
            d=preguntar_borrado(pagado,deuda,d)
        if lista==3:
            mostrar_cliente(d)
        if lista==4:
            lista_clientes(d)
        if lista==5:
            mostrar_clientes_vip(d)

        input("presiona ENTER para continuar")
    os.system("cls")
    print("programa finalizado")

if __name__=="__main__":
    main()