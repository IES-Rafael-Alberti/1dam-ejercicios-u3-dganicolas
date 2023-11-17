#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
import os
def notas(i,materia):
    notas = int(input(f"dame la nota de {materia[i]}: "))
    while notas <= -1 or notas > 10:
        notas = int(input(f"dame la nota(0-10) de {materia[i]}: "))
    return notas

def crearLista(materia):
    return list(notas(i,materia) for i in range(5))

def eliminar_lista(numero,materia):
    n = -5
    for i in range(5):
        if int(numero[n]) < 5:
            numero.pop(n)
            materia.pop(n)
        n+=1
    return numero,materia


def texto_notas(notas:list,materia:list):
    for i in range(len(notas)):
        print(f"las notas de {materia[i]} es {notas[i]}")
    print(notas)
    print(materia)


def main():
    materia = ["Matemáticas", "Física", "Química", "Historia","Lengua"]
    numero =crearLista(materia)
    numero,materia=eliminar_lista(numero,materia)
    texto_notas(numero,materia)

if __name__=="__main__":
    main()