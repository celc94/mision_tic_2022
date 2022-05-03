#1.	Haga un programa que calcule el porcentaje de alumnos perdidos y de alumnos que ganaron.
def f(aprobado, reprobado):
  estudiantesAprobados = (aprobado / (aprobado + reprobado))*100
  estudiantesReprobados = (reprobado / (aprobado + reprobado)) * 100
  return print(f' El porcentaje de estudiantes aprobados es: {estudiantesAprobados}%\n El porcentaje de estudiantes reprobados es: {estudiantesReprobados}%')

aprobado = int(input('Ingrese el Total de Estudiantes Aprobados: '))
reprobado = int(input('Ingrese el Total de Estudiantes Reprobados: '))

f(aprobado, reprobado)

#2.	Haga un programa que calcule el valor de un computador si es día de descuento.
def f(valorComputador, diaDescuento):

  valorDescuento = valorComputador - (valorComputador * descuento)

  if diaDescuento == 'si':
        descuento = float(input('Ingrese el valor del descuento: '))
        return print(f'El valor de Computador con descuento es: ${valorDescuento}')  
  elif diaDescuento == 'no':
    return print('No hay día de descuento')
  else:
    return print('Condición no reconocida')

valorComputador = float(input('Ingrese el valor del computador en COP: '))
diaDescuento = (input('Indique si hay día de descuento (si/no): '))



f(valorComputador, diaDescuento)

#3.	Haga un programa que calcule el salario básico para un empleado sabiendo que el empleado
#gana un salario bruto, a ese salario bruto se le descuenta el 10% por la retención en la fuente, 
#1% para Sena, 1% para icbf y 2% por estampilla. Y sobre el valor resultante se le descuenta el 
def calcular(s):
    retefuente = (s*10)/100
    sena = (s*1)/100
    icbf = (s*1)/100
    estampilla = (s*2)/100
    descuentos = s-retefuente-sena-icbf-estampilla

    x4mil = (descuentos*0.04)/100
    total = descuentos-x4mil
    return print(f"\nEl  ́salario básico del empleado es {total} y sus descuentos son:\n\nRetefuente:{retefuente}\nSena:{sena}\nICBF:{icbf}\nEstampilla:{estampilla}\n4x1000:{x4mil}")
#fin función 

s = int(input('Ingrese el salario del empleado: ')) 

#4.	Haga un programa de dados dos numero diga cuál es el mayor
def f(num1, num2):

    if numero1 > numero2:
       return print(f'El número mayor es: {numero1}')
    else: 
       return print(f'El número mayor es: {numero2}')

numero1 = int(input('Ingrese el primer número: '))
numero2 = int(input('Ingrese el segundo número: '))

f(numero1, numero2)

import statistics

def f(nota1, nota2, nota3):
  notas = [nota1, nota2, nota3]
  promedioNotas = sum(notas) / len(notas) #sumatoriadatos / cantidaddedatos

  if promedioNotas < 3:
    return print('El estudiante perdió la asignatura.')
  else:
    return print('El estudiante ganó la asignatura.')

nota1 = float(input('Ingrese la Nota 1. '))
nota2 = float(input('Ingrese la Nota 2. '))
nota3 = float(input('Ingrese la Nota 3. '))

f(nota1, nota2, nota3)

#6.	Haga un programa que calcule el promedio de notas para 3 notas.  
#Si el promedio es menor a tres aparezca un mensaje el estudiante perdió, 
#si el promedio es mayor o igual a tres y menor que cuatro aparezca  un mensaje 
#bien es estudiante gano, si el promedio es mayor o igual a cuatro el mensaje diga 
#excelente promedio superior.
import statistics

def f(nota1, nota2, nota3):
  notas = [nota1, nota2, nota3]
  promedioNotas = sum(notas) / len(notas) #sumatoriadatos / cantidaddedatos

  if promedioNotas < 3:
    return print('El estudiante perdió la asignatura.')
  elif 3 <= promedioNotas < 4:
      return print('El estudiante ganó la asignatura.')
  else:
    return print('Excelente Promedio Superior.')

nota1 = float(input('Ingrese la Nota 1. '))
nota2 = float(input('Ingrese la Nota 2. '))
nota3 = float(input('Ingrese la Nota 3. '))

f(nota1, nota2, nota3)

#7.	Haga un programa que dado un número, si este es mayor que 30 calcule el cubo, en caso contrario calcule el cuadrado.

def f(num):
  cubo = num ** 3
  cuadrado = num ** 2

  if num > 30:
    return print(f'El cubo del número es: {cubo}')
  else:
    return print(f'El cuadrado del número es: {cuadrado}')

num = float(input('Ingrese un número: '))

f(num)

#8.	Haga un programa que calcule el salario neto de un empleado sabiendo que el salario básico 
#de él se calcula de acuerdo a número de horas trabajadas y la hora tiene un valor especifico, 
#además si ese salario es menor que dos salarios mínimos legales vigente (smlv) se le paga un 
#subsidio de transporte equivalente a 55000.  (el smlv=565000).

def f(hora, valorHora):
  valorHoras = hora * valorHora
  smlv = 565000
  transporte = 55000
  salarioHoras = smlv + valorHoras
  
  if salarioHoras < (smlv * 2):
    salarioNeto = salarioHoras + transporte
    return print(f'El salario neto del empleado es {salarioNeto}')
  else:
    return print(f'El salario neto del empleado es: {salarioHoras}')   

hora = float(input('Ingrese la cantidad de horas: '))
valorHora = float(input('Ingrese el valor de la hora: '))    

f(hora, valorHora)