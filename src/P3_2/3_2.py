#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

def preguntar_usuario():
    palabra=input("Dame su nombre: ").capitalize()
    return palabra
def preguntar_edad():
    palabra=input("Dame su edad: ").capitalize()
    return palabra

def preguntar_direccion():
    palabra=input("Dame su direccion: ").capitalize()
    return palabra

def preguntar_telefono():
    palabra=input("Dame su telefono: ").capitalize()
    return palabra


def main():
    nombre=preguntar_usuario()
    edad=preguntar_edad()
    direccion=preguntar_direccion()
    telefono=preguntar_telefono()
    ficha_usuario= {'nombre':nombre,'edad':edad, 'direccion':direccion,'telefono':telefono}
    print(f"{ficha_usuario['nombre']} tiene {ficha_usuario['edad']} años, vive en {ficha_usuario['direccion']} y su número de teléfono es {ficha_usuario['telefono']}")

if __name__=="__main__":
    main()