import datetime
import os

opcion = '3'
while opcion != '4':
    # Obtener la fecha y hora actuales
    fecha_hora_actual = datetime.datetime.now()

    # Limpiar la pantalla
    os.system('cls')

    print('Sistema para el control de un motor de corriente directa')
    print('Desarrollado por Fontes')
    print(fecha_hora_actual)

    print('Menu')
    print('1. Girar en sentido horario')
    print('2. Girar en sentido antihorario')
    print('3. Detener el motor')
    print('4. Salir')
    if(opcion == '1'):
        print('Estado del motor: Girando en sentido horario')
    elif(opcion == '2'):
        print('Estado del motor: Girando en sentido antihorario')
    elif(opcion == '3'):
        print('Estado del motor: Detenido')

    opcion = input('Seleccione una opcion: ')

print('Saliendo del sistema...')