#Área de un Triángulo
print('Calcular el Área de un Triángulo')
base = int(input('Ingrese el valor de la base: '))
altura = int(input('Ingrese el valor de la altura: '))
area = (base * altura) / 2
print(f'El valor del área del triángulo es: {area}')
#Área de Rectángulo
print('Calcular el Área de un Rectángulo')
base = float(input('Ingrese el valor de la base: '))
altura = float(input('Ingrese el valor de la altura: '))
area = base * altura
print(f'El valor del área del rectángulo es: {area}')
#Cubo, cuadrado, triple, doble
print('Cubo, cuadrado, triple, doble de un número')
numero = float(input('Ingrese un número:' ))
cubo = numero ** 3
cuadrado = numero ** 2
triple = numero * 3
doble = numero * 2
print (f'El cubo del número es: {cubo}')
print (f'El cuadrado del número es: {cuadrado}')
print (f'El triple del número es: {triple}')
print (f'El doble del número es: {doble}')
#Índice de Masa Corporal
print('índice de Masa Corporal')
peso = float(input('Ingrese su peso en Kilogramos: '))
altura = float(input('Ingrese su altura en metros: '))
imc = peso / (altura ** 2)
print(f'Su índice de masa corporal es: {imc} kg/m2')
#Salario Neto 
print('Salario Neto de un empleado')
salarioBasico = int(input('Ingrese el Salario Básico:'))
descuento = 0.2
valorDescuento = salarioBasico * descuento
salarioNeto = salarioBasico - valorDescuento
print(f'El salario Neto es: {salarioNeto}')
#Promedio de Notas
print('Promedio de notas')
nota1 = float(input('Digite la primera nota: '))
nota2 = float(input('Digite la segunda nota: '))
nota3 = float(input('Digite la tercera nota: '))
nota4 = float(input('Digite la cuarta nota: '))
promedio = (nota1 + nota2 + nota3 + nota4) / 4
print(f'El promedio de notas es: {promedio}')
#promedio de notas libreria estadística
import statistics
print('Promedio de notas')
nota1 = float(input('Digite la primera nota: '))
nota2 = float(input('Digite la segunda nota: '))
nota3 = float(input('Digite la tercera nota: '))
nota4 = float(input('Digite la cuarta nota: '))
notas = [nota1, nota2, nota3, nota4]
promedio = sum(notas)/len(notas)
print(f'El promedio de notas es: {promedio}')
#Nota Final
print('Nota Final')
nota1 = float(input('Digite la primera nota: '))
nota2 = float(input('Digite la segunda nota: '))
nota3 = float(input('Digite la tercera nota: '))
notaFinal = (nota1 * 0.3) + (nota2 * 0.3) + (nota3 * 0.4)  
print(f'La nota final es: {notaFinal}')