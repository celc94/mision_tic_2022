#Definir una función
def f(x):
  return x * x
  f(4)
print(f(4))

#Área de un círculo = π * radio^2
#Se importa la librería de Matemáticas
import math
# π = math.pi
def f(x):
  return math.pi * x * x
  f(5)
print(f(5))

#Área de un triángulo
def f(b,a):
  return (b * a) / 2
  f(3,1)
print(f(3,1)) 

#Cuadrado-cubo-doble-triple de un número
def f(num):
  cuadrado = num ** 2
  cubo = num ** 3
  doble = num * 2
  triple = num * 3
  return print(f' El cuadrado del número es {cuadrado}\n El cubo del número es {cubo}\n El doble del número es {doble}\n El triple del número es {triple}')
num = float(input('Ingrese el número: '))
f(num)

#Si pido prestados P cantidad de pesos para pagarlos en dos meses, si
#el interés del préstamo es del 3%. Cuanto se debe pagar al final del
#segundo mes si el interés es compuesto mensualmente?.
def f(cantidad_dinero):
  valor_final = cantidad_dinero * ((1 + 0.03) ** 2) 
  return print(f'Al final de los dos meses se debe de pagar: {valor_final}')

cantidad_dinero = float(input('Ingrese el valor del dinero prestado:'))
f(cantidad_dinero)

# El numero de contagiados de Covid-19 en el país de NuncaLandia se
#duplica cada día. Hacer un programa que diga el numero total de
#personas que se han contagiado cuando pasen D días a partir de hoy,
#si el número de contagiados actuales es C.
def f(x,y):
  f=x*(2)**(y)
  return print(f"\n El numero de contagiados el día {y} es {f}")
x=int(input("Ingrese el numero de contagiados en el dia 1: "))
y=int(input("Ingrese el numero de dias transcurridos: "))
f(x,y)

#Ejercicio para calcular el peso de tres personas donde la resta estre Gi - 4 es el peso de Ale y la suma del peso de Gi
# y de Ale es 5 veces el peso de Nico
gi = int(input('Ingrese el peso de Gi en Kilogramos: '))
ale = (gi - 4) / 2
nico = (gi + ale) / 5
print(f'El peso de Gi es: {gi} Kilogramos')
print(f'El peso de Ale es: {ale} Kilogramos')
print(f'El peso de nico es: {nico} Kilogramos')

#Condicional de mayor o menor de edad
edad = int(input('Ingrese su edad en años: '))
if edad >= 18:
  print('La persona es mayor de edad.')
else:
  print('La persona es menor de edad.')

#Ejercicio de Condicional 
dosisAz = int(input('Ingrese la cantidad de dosis a comprar de Astrazenaca: '))
dosisPf = (dosisAz * 2) + 4
dosisJh = (dosisAz + dosisPf) // 5

print(f' La cantidad de dosis a comprar de AZ es {dosisAz}\n La cantidad de dosis a comprar de Pf es {dosisPf}\n La cantidad de dosis a comprar de Jh es {dosisJh}')

if dosisJh >= 0 and dosisJh <= 20:
  print('Fase 1')
elif dosisJh >=21 and dosisJh <= 30:
  print('Fase 2')
elif dosisJh >=31 and dosisJh <= 50:
  print('Fase 3')
else:
  print('Fase 4')  
