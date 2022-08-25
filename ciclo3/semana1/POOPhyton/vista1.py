import Persona as pe

nom=input('Digite su nombre: ')
edad=int(input('Digite su edad: '))

resul=pe.Persona(nom,edad)
print(resul.getnombre())
print(resul.getedad())
print(resul.mayordeedad())