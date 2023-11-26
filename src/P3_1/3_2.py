#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.
import os
def lista():
    """le introduces los items de la lista y te retorna la lista"""
    lista = []
    asignaturas=""
    while asignaturas != "*":
        asignaturas = input("¿que asignaturas cursas?(escribe '*' para imprimir la lista)")
        if asignaturas != "*" and asignaturas != "":
            lista.append(asignaturas)
    return lista

def main():
    lista_str=""
    listaa=lista()
    os.system("cls")
    print(f"Yo estudio")
    print(*listaa)
if __name__ =="__main__":
    main()