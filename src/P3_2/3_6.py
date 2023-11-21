#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.

def preguntar_al_usuario(i):
    clase=input(f"dime tu {i}: ")
    return clase

def main():
    d={}
    lista = ("nombre", "edad", "sexo", "teléfono", "correo electrónico")
    for i in range(1,len(lista)):
        clase = lista[i]
        objeto=preguntar_al_usuario(clase)
        d[clase]=objeto
    print(d)


if __name__=="__main__":
    main()