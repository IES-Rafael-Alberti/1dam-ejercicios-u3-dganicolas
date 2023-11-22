#Dado el conjunto de letras:

vocales = {'a', 'e', 'i', 'o', 'u'}
#Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.-----------
#Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.--------
#Estos ejercicios te ayudarán a practicar y comprender mejor cómo trabajar con conjuntos en Python. ¡Espero que te sean útiles! Si tienes alguna pregunta o necesitas más ejercicios, no dudes en decírmelo.
def crear_abecedario(vocales):
    abecedario=set()
    for i in range(97,123):
        abecedario.add(chr(i))
    for i in vocales:
        abecedario.discard(i)
    print(abecedario)
    return abecedario

def comunes(vocales,abecedario):
    return vocales&abecedario

def main():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    abecedario=crear_abecedario(vocales)
    conjunto_comunes=comunes(vocales,abecedario)
    print(conjunto_comunes)


if __name__=="__main__":
    main()