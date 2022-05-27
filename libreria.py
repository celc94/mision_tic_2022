# Array de una dimensión
import numpy as np
#a1 = np.array([7, 8, 3])
#print(a1)

# Array de dos dimensiones
a2 = np.array([[1.8, 2.9, 3.6], [4.8, 5.0, 6.3], [8.7, 12.7, 16.6]])
print(a2)

# Numpy = Arreglo de valores del mismo tipo indexadas por enteros no negativos.
# El numero de dimensiones (rank) y La forma de dimension (shape) es una tupla de enteros que da el tamaño.
# Se pueden crear arreglos de numpy desde listas de Python y acceder a los elementos con el operador subscript [].

import numpy as np #  para utilizar la libreria numpy se hace uso de esta sentencia.

a =np.array(list(range(1,5)))# Crea un arreglo lineal
#print(type(a)) #Imprime el tipo del arreglo "<class'numpy.ndarray'>"
print(a)
#print(a.shape) #Imprime"(4,)"es de tamaño 4,de 1 dimensión
#print(a[0], a[1],a[2])
a[0] =98
print(a)

b =np.array([[1,2,3,5,6],[4,5,6,7,8]])# Crea un arreglo bidimensional
print(b.shape)
print(b)
print("---------")
b[0,0] =1590
print(b)
print("---------")
print(b[0,0], b[0,1],b[1,0])

import numpy as np
b =np.ones((2,3))#Crea una matriz de 2x3 de unos(1's)
print(b.shape)
print(b)
#print("---------")

import numpy as np
# Crea un arreglo bidimensionalcon forma(3,4) tres filas cuatro columnas
a =np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a.shape)
print("------------------------")
print(a)
print("------------------------")
b =a[:2,1:3]
# El primer argumento indica las filas y el segundo lascolumnas
print(b)
#print("------------------------")

# Si se modifica algo de b,se cambia algo de a
b[0, 0]=-11 #b[0,0]es el mismo a[0,1]
print(b)
print(a)
#print(a[0,1]) #Imprime"-11"

import numpy as np

#dtype = tipos de datos en arrays , enteros de 64 bits; https://python-para-impacientes.blogspot.com/2019/10/tipos-de-datos-en-arrays-numpy-dtype.html
x =np.array([5,-4])
print(x.dtype)
x =np.array([1.0,2.0])
print(x.dtype)
x =np.array([5,-4],dtype=np.int32)
print(x.dtype)

import numpy as np
x =np.array([[1,2,5],[3,4,6]],dtype=np.float128)
y =np.array([[5,6,-1],[7,8,-6]],dtype=np.float128)
print("Suma:")
print(x + y)
print("-----")
print(np.add(x, y)) # otra forma de hacer la suma
print("raiz cuadrada:")
print(np.sqrt(x))

import numpy as np
#linspace genera un array NumPy formado por n números equiespaciados entre dos dados
#Su sintaxis es: numpy.linspace(valor-inicial, valor-final, número de valores)

np.linspace(2, 3,num=10,endpoint=True,retstep=False)

# LIBRERIA MATPLOTLIB
# Matplotlib es una libreria para la generación de gráficos a partir de datos contenidos en listas 
# o arrays en el lenguaje de programación Python y su extensión matemática NumPy

# Pasos para crear graficos
# https://aprendeconalf.es/docencia/python/manual/matplotlib/

import matplotlib.pyplot as plt    # Importar el módulo pyplot con el alias plt
# Matplotlibplot.
plt.plot([1, 2,3,4],[1,4,2,3]) #.plot Dibuja un polígono con los vértices dados 
#por las coordenadas de la lista x en el eje X y las coordenadas de la lista y en el eje Y

#Enlaces
#https://programmerclick.com/article/1420578004/
#https://python-para-impacientes.blogspot.com/2019/10/tipos-de-datos-en-arrays-numpy-dtype.html
#https://interactivechaos.com/es/manual/tutorial-de-numpy/las-funciones-linspace-y-logspace
#https://numpy.org/doc/stable/reference/generated/numpy.linspace.html

# Importar el módulo pyplot con el alias plt
import matplotlib.pyplot as plt
# Crear la figura y los ejes
fig, ax = plt.subplots()
# Dibujar puntos
ax.scatter(x = [1, 2, 3], y = [3, 2, 1]) #.scatter es un diagrama de dispersión 
# Guardar el gráfico en formato png
plt.savefig('diagrama-dispersion.png')
# Mostrar el gráfico
plt.show()

#  .scatter: Dibuja un diagrama de puntos con las coordenadas de la lista x 
#en el eje X y las coordenadas de la lista y en el eje Y.

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter([1, 2, 3, 4], [1, 2, 0, 0.5])
plt.show()

#Diagrama de areas
# fill_between(x, y): Dibuja el area bajo el polígono con los vértices dados 
#por las coordenadas de la lista x en el eje X y las coordenadas de la lista y en el eje Y

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.fill_between([1, 2, 3, 4], [1, 2, 0, 0.5])
plt.show()

# Diagrama de barras verticales
#bar(x, y): Dibuja un diagrama de barras verticales donde x es una lista
# con la posición de las barras en el eje X, e y es una lista con la altura de las barras en el eje Y.

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.bar([1, 2, 3], [3, 2, 1])
plt.show()

# Diagrama de barras horizontales
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.barh([1, 2, 3], [3, 2, 1])
plt.show()

#COMBINAR LIBRERIA

import numpy as np
import matplotlib.pyplot as plt
x =np.linspace(0,2,50)
#print(x)
# Aun con el OO-style,usamos".pyplot.figure"para crear la figura.
fig, ax=plt.subplots()#Crea la figura y los ejes.
ax.plot(x, x,label="linear")#Dibuja algunos datos en los ejes.
ax.plot(x, x**2,label="quadratic")#Dibuja mas datos en los ejes.
ax.plot(x, x**3,label="cubic")#...y algunos mas.
ax.set_xlabel("x label")#Agrega un x-label a los ejes.
ax.set_ylabel("y label")#Agrega un y-label a los ejes.
ax.set_title("Simple Plot")#Agrega tItulo a los ejes.
ax.legend() #Agrega una leyenda.

#Git HUB
#https://jdvelasq.github.io/courses/notebooks/python_for_data_analysis_examples/1-01_operaciones_basicas_sobre_datos.html

names =["group_a","group_b","group_c"]
values =[3.4,50.3,23]
plt.figure(figsize=(9, 3))
plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle("Categorical Plotting")
plt.show()

# LIBRERIA PANDAS
dictc ={"country":["Brazil","Russia","India","China", "SouthAfrica","Colombia"],"capital": ["Brasilia","Moscow","NewDehli", "Beijing", "Pretoria","Bogota"],
"area": [8.516,17.10,3.286,9.597,1.221,1.142], "population": [200.4,143.5,1252,1357,52.98,49.65]}

import pandas as pd
brics =pd.DataFrame(dictc)
print(brics)

from google.colab import files
uploaded =files.upload()#Uploadfiles/SalesJan2009.csv

# Importpandasaspd
import pandas as pd
from collections import Counter
ventasdf =pd.read_csv("SalesJan2009.csv")
ventasdf.head(3)

import pandas as pd
from collections import Counter
ventasdf =pd.read_csv("SalesJan2009.csv")
#print(ventas)
cp =Counter(ventasdf["Country"])
print(cp.most_common(3))
cv =Counter(ventasdf["Payment_Type"])
print(cv.most_common(3))

import pandas as pd
import datetime
import matplotlib.pyplot as plt
#Reporte porfecha
ventasdf["Transaction_date"]=pd.to_datetime(ventasdf["Transaction_date"])
A = (ventasdf["Transaction_date"]
.dt.floor("d")
.value_counts()
.rename_axis("date")
.reset_index(name="num ventas"))
G=A.plot(x="date",y="num ventas",color="green",title="Ventasporfecha")
plt.show()

import numpy as np
x = np.linspace(0, 10, 100)

fig = plt.figure()
plt.plot(x, np.sin(x), '-')
plt.plot(x, np.cos(x), '--');

