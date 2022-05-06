#Imprimir 10 números
from turtle import distance


i = 0
while i <= 10:
  print(i)
  i += 1
else:
  print('Fin del Ciclo While')

  #Imprimir números pares
i = 2
while i <= 20:
  print(i)
  i += 2
else:
  print('Fin del Ciclo While')

  #Imprimir números impares
i = 1
while i <= 20:
  print(i)
  i += 2
else:
  print('Fin del Ciclo While')

  #Sumar los primeros 10 valores
i = 0
suma = 0
while i < 10:
  print(i)
  suma = suma + i
  i += 1
print(suma)

numero = int(input("Escriba un número positivo: "))
while numero < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    numero = int(input("Escriba un número positivo: "))
else:
  print("Gracias por su colaboración")

  #Tabla del 3
i = 0
tabla = 0
while i <= 10:
  tabla = 3 * i
  i += 1
  print(f'3 * {i-1} = {tabla}')

  #Imprimir 5 veces la palabra python
i = 1
while i <= 5:
  print('Python')
  i += 1
else:
  print('Fin de Ciclo While')

  #Múltiplos de 3, entre 3 y 15
i=3
print('Multiplos de 3 comprendidos entre 3 y 15:')
while i <=15:    
    print(f"{i}")
    i=i+3

