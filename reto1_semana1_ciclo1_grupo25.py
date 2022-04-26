#La Familia Pesos Pesados
pesoPadre = int(input('Ingrese el peso del padre en Kg: '))
pesoMadre = int((2 * pesoPadre) + 4)
pesoHijo = (pesoMadre + pesoPadre) // 5
print(pesoPadre, pesoMadre, pesoHijo)
if pesoHijo > 0 and pesoHijo <= 20:
    print('uno')
elif pesoHijo >= 21 and pesoHijo <= 40:
    print('dos')
elif pesoHijo >= 41 and pesoHijo <=80:
    print('tres')
else: print('cuatro')