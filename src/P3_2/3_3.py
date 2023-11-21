#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

def preguntar_usuario():
    palabra=input("Dame una fruta: ").capitalize()
    return palabra

def preguntar_kilos():
    palabra=input("Dame el total de los kilosgramos: ")
    return palabra

def comprobar_si_existe(lista,fruta,KGs:int):
    pieza=lista.get(fruta)
    if pieza == None:
        return "***ERROR*** Esa fruta no esta registrada"
    else:
        return f"tu fruta es {fruta} y el peso es {round(float(pieza)* float(KGs),2)}"

def main():
    lista = {'Platano':'1.35', 'Manzana':'0.80', 'Pera':'0.85', 'Naranja':'0.70'}
    fruta=preguntar_usuario()
    KGs=preguntar_kilos()
    print(comprobar_si_existe(lista,fruta,KGs))

if __name__=="__main__":
    main()