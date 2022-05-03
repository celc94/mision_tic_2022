# Ejemplo Robot
x1 = 0
y1 = 0
distancia = 0
print('Describa el Movimiento del Robot.')
while True:
    m = input()
    if not m: #Si no introduce un valor, se cierra del ciclo 
        break
    datos = m.split(' ') #Se separa con espacio en blanco como carácter especial
    print(datos) #Se guarda en una lista
    #Se separan los datos de la lista
    movimiento = datos[0] #Lo que está en la posición 0 de la lista
    cantidadMovimiento = int(datos[1]) #Se convierte a entero
    if movimiento == 'UP' and movimiento =='DOWN':
        print(cantidadMovimiento)


print(distancia)