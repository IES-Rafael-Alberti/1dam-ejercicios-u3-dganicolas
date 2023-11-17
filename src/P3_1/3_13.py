#Escribir un programa que pregunte por una muestra de números, separados por comas, los guarde en una lista y muestre por pantalla su media y desviación típica.

def pedir_numeros():
    numeros = input("Dame una serie numero separados por comas (1,2,3): ")
    numeros = numeros.replace(".",",")
    return numeros

def crear_lista(numeros:str):
    lista = []
    lista_str = []
    lista_str = numeros.split(",")
    for i in range(len(lista_str)):
        convertidor= int(lista_str[i])
        lista.append(convertidor)
    return lista

def calculo_media(lista):
    media=0
    for i in range(len(lista)):
        media+=int(lista[i])
    media = media / int(len(lista))
    return media

def calculo_varianza(lista,media):
    Xi = 0
    Fi = 0
    X = 0
    suma=0
    resultado= 0
    for i in range (len(lista)):
        suma+= int(lista[i])
        Fi+= X**2 * int(lista[i])
        X+=1
    resultado = Fi / suma
    resultado = resultado**0.5
    return resultado

def main():
    numeros = pedir_numeros()
    lista = crear_lista(numeros)
    media = calculo_media(lista)
    varianza = calculo_varianza(lista,media)
    datos= ", ".join(map(str,numeros))
    print(f"los datos son {datos}, la media es {media} y la varianza es {varianza} ")

if __name__=="__main__":
    main()