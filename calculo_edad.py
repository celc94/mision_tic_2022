#Calcular la edad a partir de la fecha de nacimiento
#Se importa el módulo datetime para trabajar con fechas
from datetime import datetime

def edad(fecha):
    #Guardamos la fecha actual en una variable, y la llamamos con datetime.now()
    fechaHoy = datetime.now()
    #Se convierte el input en tipo fecha (Año en Mayúscula)
    fechaNacimiento = datetime.strptime (fecha, '%d-%m-%Y')
    #Se restan los años para que no arroje toda la fecha
    edadUsario = fechaHoy.year - fechaNacimiento.year
    #Se utiliza un condicional para saber si estoy en el mismo año pero si es enero y cumplo en febrero, el programa
    #no puede decir que ya cumpli años
    if fechaNacimiento.month <= fechaHoy.month:
        if fechaNacimiento.day <= fechaHoy.day:
            print(f'Tienes {edadUsario} años.')
        else: print(f'Tienes {edadUsario-1} años.')
    else: print(f'Tienes {edadUsario-1} años.')  

edad(input('Introduce tú fecha de nacimiento: '))