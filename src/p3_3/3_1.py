#Dadas las siguientes listas:

#frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
#frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
#Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.----------
#Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
#Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.-------------
#Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.

def conjunto_comunes1(set_frutas1,set_frutas2):
    frutas_solo_en_frutas1=set()
    for e in set_frutas1:
        if e in set_frutas2:
            frutas_solo_en_frutas1.add(e)
    return frutas_solo_en_frutas1

def conjunto_comunes2(set_frutas1,set_frutas2):
    frutas_solo_en_frutas2=set()
    for e in set_frutas1:
        if e not in set_frutas2:
            frutas_solo_en_frutas2.add(e)
    return frutas_solo_en_frutas2

def crear_conjunto(frutas1,frutas2):
    set_frutas1=set()
    set_frutas2=set()
    for i in range (len(frutas1)):
        set_frutas1.add(frutas1[i])
    for i in range (len(frutas2)):
        set_frutas2.add(frutas2[i])
    return set_frutas1,set_frutas2

def main():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
    set_frutas1,set_frutas2=crear_conjunto(frutas1,frutas2)
    frutas_solo_en_frutas1=conjunto_comunes1(set_frutas1,set_frutas2)
    frutas_solo_en_frutas2=conjunto_comunes2(set_frutas1,set_frutas2)
    print(set_frutas1)
    print(set_frutas2)
    print(frutas_solo_en_frutas1)
    print(frutas_solo_en_frutas2)

if __name__=="__main__":
    main()