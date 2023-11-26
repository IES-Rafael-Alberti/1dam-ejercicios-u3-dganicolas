#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.

def crear_lista():
    return list(chr(i) for i in range(97,123))

def eliminar_letras(abecedario:list):
    n = -26
    for i in range(26):
        if n%3 == 0:
            abecedario.pop(n)
        n+=1
def main():
    abecedario=crear_lista()
    eliminar_letras(abecedario)
    print(abecedario)

if __name__=="__main__":
    main()