'''Realizar un programa que tenga una clase Persona con las siguientes características. 
La clase tendrá como atributos el nombre y la edad de una persona. Implementar los métodos necesarios 
para inicializar los atributos, mostrar los datos e indicar si la persona es mayor de edad o no.'''


class Persona:
    def __init__(self, nombre, edad):
        self.__nombre=nombre
        self.__edad=edad

    def getnombre(self):
        return self.__nombre
    
    def getedad(self):
        return self.__edad

    def mayordeedad(self):
        if self.__edad >= 18:
            return 'Es mayor de edad.'
        else:
            return 'Es menor de edad.'

