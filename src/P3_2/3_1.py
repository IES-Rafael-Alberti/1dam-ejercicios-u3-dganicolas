#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.



def preguntar_usuario():
    palabra=input("Dame una divisa: ").capitalize()
    return palabra

def comprobar_si_existe(moneda, divisa):
    moneda=moneda.get(divisa)
    if moneda == None:
        return "***ERROR*** Esa divisa no esta registrada"
    else:
        return f"tu simbolo de divisa es {moneda}"

def main():
    moneda = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    divisa=preguntar_usuario()
    print(comprobar_si_existe(moneda,divisa))

if __name__=="__main__":
    main()