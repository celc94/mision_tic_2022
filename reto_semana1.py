#RETO SEMANA 1
#Se solicita el peso de Quico
pesoQuico = int(input('Ingrese el peso de Quico en Kilogramos: '))
estaturaQuico = float(input('Ingrese la estatura de Quico en Centímetros: '))
estaturaChavo = float(input('Ingrese la estatura del Chavo en Centímetros: '))
estaturaÑoño = float(input('Ingrese la estatura de Ñoño en Centímetros: '))
pesoChavo = int(pesoQuico * 2)
pesoÑoño = pesoQuico + pesoChavo
#Se calcula la edad a partir del peso con la fórmula de La fórmula de Perrault Dry
# Peso = Altura en cm - 100 + ((edad/10) x 0,9) -> se despeja la edad     
edadQuico = (10 * (pesoQuico - estaturaQuico + 100)) / 0.9
edadChavo = (10 * (pesoChavo - estaturaChavo + 100)) / 0.9
edadÑoño = (10 * (pesoÑoño - estaturaÑoño + 100)) / 0.9
print(f'Las edades del Chavo, Quico y Ñoño son: {edadChavo} {edadQuico} {edadÑoño} respectivamente.')
#Condicional para saber en que etapa está el peso de Ñoño
if (pesoÑoño >= 0 and pesoÑoño <= 20):
    print('Ñoño se encuentra en la Etapa Uno')
elif (pesoÑoño >= 21 and pesoÑoño <= 40):
    print('Ñoño se encuentra en la Etapa dos')
elif (pesoÑoño >= 41 and pesoÑoño <= 80):
    print('Ñoño se encuentra en la Etapa 3')
else:
    print('Ñoño se encuentra en la Etapa 4')

