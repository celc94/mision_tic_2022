#FUNCIONES NATIVAS PARA TRABAJAR FICHEROS O ARCHIVOS

# OPEN= Acceder a los ficheros o archivos;recibe argumentos r,w,a

#Argumento r= se accedera al archivo en modo lectura.

#Argumento w= el archivo se abrirá en modo escritura; se sobre escribe.

#Argumento a= se abrira en modo actualización; similar modo escritura solo que este añade a continuación de lo existente

# Argumento x = crea un archivo para escribir en el. En caso de exitir lo borra

# Argumento b = abre el archivo en modo binario.

# Argumeto t = abre el archivo en modo texto 

# Argumento + = abre el archvo para lectura y escritura.

# Programa para crear un archivo desde python/lo abre/le incluye un texto /lo cierra.
from io import open #Libreria para acceder un archivo
archivo1= open("MiArchivo.txt","w")
texto ="César Eduardo López Cardona\nIngeniero Industrial"
archivo1.write(texto)
archivo1.close()

#Archivo nombre apellido peso estat fna empresa ciudad depa pais

from io import open #Libreria para acceder un archivo
archivo1= open("Archivo.txt","w")
texto ="Nombre: César Eduardo\nApellido: López Cardona\nPeso: 83 Kg\nEstatura: 1,75 mts\nFecha de Nacimiento: 10 de Octubre de 1994\nEmpresa donde Trabaja: Geosafe Consultores - Alcaldía de La Unión Valle \nCiudad: La Unión\nDepartamento: Valle del Cauca\nPaís: Colombia"
archivo1.write(texto)
archivo1.close()

#programa que abre el archivo en modo lectura; lea su contenido y lo ponga en pantalla
from io import open
NombreArchivo ="MiArchivo.txt"
archivo1 =open(NombreArchivo,"r")
texto =archivo1.read()
archivo1.close()
print("ARCHIVO:",NombreArchivo)
print("Contenido:")
print(texto)

from io import open
NombreArchivo ="Archivo.txt"
archivo1 =open(NombreArchivo,"r")
texto =archivo1.read()
archivo1.close()
print("ARCHIVO:",NombreArchivo)
print("Contenido:")
print(texto)

#programa que abre el archivo en modo lectura; lea su contenido y lo ponga en pantalla como una lista
from io import open
NombreArchivo ="MiArchivo.txt"
archivo1 =open(NombreArchivo,"r")
texto =archivo1.readlines() #convierte el texto en lista
archivo1.close()
print("ARCHIVO:",NombreArchivo)
print("Contenido:")
print(texto)

from io import open
NombreArchivo ="Archivo.txt"
archivo1 =open(NombreArchivo,"r")
texto =archivo1.readlines() #convierte el texto en lista
archivo1.close()
print("ARCHIVO:",NombreArchivo)
print("Contenido:")
print(texto)

#programa que abre el archivo en modo lectura; lea su contenido y lo ponga en pantalla desde la posición de una lista
from io import open
NombreArchivo ="MiArchivo.txt"
archivo1 =open(NombreArchivo,"r")
texto =archivo1.readlines()
archivo1.close()
print("ARCHIVO:",NombreArchivo)
print("Contenido:")
print(texto)
print(texto[1])

#programa que abre el archivo en modo lectura; lea su contenido y lo ponga en pantalla desde la posición de una lista
from io import open
NombreArchivo ="Archivo.txt"
archivo1 =open(NombreArchivo,"r")
texto =archivo1.readlines()
archivo1.close()
print("ARCHIVO:",NombreArchivo)
print("Contenido:")
print(texto)
print(texto[4])

import pickle #Archivos Binarios
datos=["César Eduardo","López Cardona","27","1.75"]
archivo =open("Miarchivo.dat","wb") #Write binary - .dat para archivo binario
pickle.dump(datos,archivo) #Funcion dump permite guardar los datos en un archivo binario
archivo.close()

#ARCIVOS BINARIOS//VER EL CONTENIDO
import pickle
archivo2 =open("Miarchivo.dat","rb")
datos = pickle.load (archivo2) #Función Load - permite recuperar información guardada en un archivo binario
archivo2.close()

for c in datos:
  print(c)

#ARCHIVO JSON JSON (JavaScriptObjectNotation)
# Es un estandar utilizado para el intercambio de informacion entre aplicaciones. 
#Un objeto JSON es un diccionario donde la clave una cadena de caracteres delimitado por ""
# el valor puede se un numero, una cadena de caracteres, un elemento null,o una lista de elementos o un Json

import json
{
"Nombre": "Douglas", 
"Apellido": "Crockford",
"pasatiempos": ["trotar","bucear","cantar"],
"edad": 64,
"empleado": false,
"jefe": null,
"hijos": [
    {"Nombre": "Alice","edad":16},
    {"Nombre": "Bob","edad":8}
  ]
}

# DICCIONARIO
{
"Nombre": "Douglas", 
"Apellido": "Crockford",
"pasatiempos": ["trotar","bucear","cantar"],
"edad": 64,
"empleado": False,
"jefe": None,
"hijos": [
    {"Nombre": "Alice","edad":16},
    {"Nombre": "Bob","edad":8}
  ]
}

#Convertir JSON en Python

import json
strjson=input()
s=input()
sl=s.split()
d=json.loads(strjson)
print(d)

