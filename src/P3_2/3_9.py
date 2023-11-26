#Escribir un programa que gestione las facturas pendientes de cobro de una empresa. Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
import os
def preguntar_factura():
    clase=input(f"dime el numero de factura: ")
    return clase

def preguntar_cantidad(deuda):
    clase=input(f"dime la cantidad: ")
    deuda+=int(clase)
    return clase,deuda

def parar_usuario():
    numero=int(input('escriba "1" para generar una nueva factura\nescriba "2" para pagar una factura\nescriba "3" para finalizar le programa\n'))
    while numero!=1 and numero!=2 and numero!=3:
        os.system("cls")
        numero=int(input('***ERROR***\nescriba "1" para generar una nueva factura\nescriba "2" para pagar una factura\nescriba"3" para finalizar le programa'))
    return numero

def preguntar_borrado(pagado,deuda,d):
    seguro="S"
    clase=input(f"dime el numero de factura a eliminar: ")
    while seguro=="S":
        if clase in d:
            seguro="N"
        if seguro=="S":
            clase=input(f"***ERROR*** - dime el numero de factura a eliminar: ")
    pagado+=int(d[clase])
    deuda-=int(d[clase])
    del d[clase]
    return pagado,deuda

def main():
    d={}
    lista = 0
    deuda=0
    pagado=0
    while lista!=3:
        os.system("cls")
        print(f"cantidad cobrada {pagado}")
        print(f"cantidad pendiente de cobro {deuda}")
        lista=parar_usuario()
        if lista==1:
            clase = preguntar_factura()
            objeto,deuda=preguntar_cantidad(deuda)
            d[clase]=objeto
        if lista==2:
            pagado,deuda=preguntar_borrado(pagado,deuda,d)
    os.system("cls")
    print("programa finalizado")
    print(f"cantidad cobrada {pagado}")
    print(f"cantidad pendiente de cobro {deuda}")

if __name__=="__main__":
    main()