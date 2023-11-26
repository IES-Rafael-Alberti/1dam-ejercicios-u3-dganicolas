#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de créditos del curso.

def texto_final(d:dict):
    suma=0
    for i in d.keys():
        asig=i
        creditos= d[i]
        suma+=int(creditos)
        print(f"tu asignatura es {asig} y la nota es {creditos}")
    print(f"la suma total de notas es: {suma}")

def lista_creditos(creditos:dict)-> list:
    lista = []
    for k in creditos.values():
        lista.append(k)
        return lista

def main():
    asignaturas= {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    texto_final(asignaturas)

if __name__=="__main__":
    main()