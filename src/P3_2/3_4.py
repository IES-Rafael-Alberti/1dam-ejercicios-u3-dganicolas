#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.

def convertir_fecha(fecha):
    meses = {1:'enero', 2:'febrero', 3:'marzo', 4:'abril', 5:'mayo', 6:'junio', 7:'julio', 8:'agosto', 9:'septiembre', 10:'octubre', 11:'noviembre', 12:'diciembre'}
    dia, mes, año = fecha.split('/')
    mes = meses[int(mes)]
    return f'{dia} de {mes} de {año}'

def main():
    fecha = input('Introduce una fecha en formato dd/mm/aaaa: ')
    print(convertir_fecha(fecha))

if __name__=="__main__":
    main()