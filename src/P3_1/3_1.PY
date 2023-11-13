#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla.
import os
def lista():
    lista = []
    asignaturas=""
    while asignaturas != "*":
        asignaturas = input('¿que asignaturas cursas?(escribe "*" para imprimir la lista)')
        if asignaturas != "*" and asignaturas != "":
            lista.append(asignaturas)
    return lista

def main():
    listaa=lista()
    os.system("cls")
    print(f"tus asignaturas son:")
    print(*listaa)
if __name__ =="__main__":
    main()
