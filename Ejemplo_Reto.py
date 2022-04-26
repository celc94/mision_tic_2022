#RETO SEMANA 1
#Se solicita el peso de Quico
pesoQuico = int(input('Ingrese el peso de Quico en Kilogramos: '))
pesoChavo = int(pesoQuico * 2)
pesoÑoño = pesoQuico + pesoChavo
#Condicional para saber en que etapa está el peso de Ñoño
if (pesoÑoño >= 0 and pesoÑoño <= 20):
    print('Ñoño se encuentra en la Etapa Uno')
elif (pesoÑoño >= 21 and pesoÑoño <= 40):
    print('Ñoño se encuentra en la Etapa dos')
elif (pesoÑoño >= 41 and pesoÑoño <= 80):
    print('Ñoño se encuentra en la Etapa 3')
else:
    print('Ñoño se encuentra en la Etapa 4')

