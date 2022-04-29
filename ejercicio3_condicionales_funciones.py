#Haga un programa que calcule el valor de un computador sabiendo que tienen un precio de venta
#y se hace un descuento dependiendo de la forma de pago, si es efectivo se le descuenta 30% del
#valor venta, si es con tarjeta crédito se le descuenta 15% del valor venta y si es con tarjeta 
#debito se le descuenta un 25% del valor venta.

def f(valorComputador, formaPago):

  if formaPago == 'ef':
        valorDescuento = valorComputador - (valorComputador * 0.3)
        return print(f'El valor de Computador con descuento es: ${valorDescuento}')  
  elif formaPago == 'tc':
    valorDescuento = valorComputador - (valorComputador * 0.15)
    return print(f'El valor de Computador con descuento es: ${valorDescuento}')
  elif formaPago == 'td':
    valorDescuento = valorComputador - (valorComputador * 0.25)
    return print(f'El valor de Computador con descuento es: ${valorDescuento}')
  else:
    return print('Medio de Pago no Reconocido')

valorComputador = int(input('Ingrese el valor del computador en COP: '))
formaPago = (input('Indique el Medio de Pago, Efectivo (ef), Tarjeta de credito (tc), Tarjeta de debito (td): '))


f(valorComputador, formaPago)

#2.	Haga un programa que dados tres números diga cual es el mayor.

def f(num1, num2, num3):

    if numero1 > numero2 and numero1 > numero3:
       return print(f'El número mayor es: {numero1}')
    elif numero2 > numero1 and numero2 > numero3:
      return print(f'El número mayor es: {numero2}')
    else: 
       return print(f'El número mayor es: {numero3}')

numero1 = int(input('Ingrese el primer número: '))
numero2 = int(input('Ingrese el segundo número: '))
numero3 = int(input('Ingrese el tercer número: '))

f(numero1, numero2, numero3)

#8.	Haga un programa que calcule el salario neto de un empleado sabiendo que el salario básico 
#de él se calcula de acuerdo a número de horas extras trabajadas y la hora tiene un valor especifico + SMLMV, 
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

