'''Aplicando la programación orientada a objetos realice el siguiente algoritmo. 
Ingresar el nombre de un empleado, las horas trabajadas, luego Calcular pago bruto 8.000 
pesos por hora trabajada y total a pagar, presentar los resultados del programa Nota: el seguro 
social es de 8.5% del total de lo que recibe si el sueldo es mayor 700.000 sino es el 3.5% del 
sueldo del empleado.'''

class Nomina:

    def __init__(self, nombre, horatrabajada):
        self.__nombre=nombre
        self.__horatrabajada=horatrabajada

    def getnombre(self):
        return self.__nombre
    
    def gethora(self):
        return self.__horatrabajada

    def pagototal(self):
        pagoBruto = 8000*self.__horatrabajada
        print("El pago bruto es:", pagoBruto)
        if pagoBruto > 700000:
            return pagoBruto*(1-0.085)
        else:
            return pagoBruto*(1-0.035)

     