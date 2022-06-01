#Pandas es una librería de Python especializada en el manejo y análisis de estructuras de datos.

# Caracteristicas

# Define nuevas estructuras de datos basadas en los arrays de la librería NumPy pero con nuevas funcionalidades.
# Permite leer y escribir fácilmente ficheros en formato CSV, Excel y bases de datos SQL.
# Permite acceder a los datos mediante índices o nombres para filas y columnas.
# Ofrece métodos para reordenar, dividir y combinar conjuntos de datos.
# Permite trabajar con series temporales.
# Realiza todas estas operaciones de manera muy eficiente

# TIPOS DE DATOS PANDAS
#  Series: Estructura de una dimensión.
# DataFrame: Estructura de dos dimensiones (tablas).
# Panel: Estructura de tres dimensiones (cubos).

# Estas estructuras se construyen a partir de arrays de la librería NumPy, añadiendo nuevas funcionalidades.


# Creación de una serie a partir de una lista
import pandas as pd
s = pd.Series(['Matemáticas', 'Historia', 'Economía', 'Programación', 'Inglés'], dtype='string')
print(s)

# Creación de una serie a partir de un diccionario
import pandas as pd
s = pd.Series({'Matemáticas': 6.0,  'Economía': 4.5, 'Programación': 8.5})
print(s)


# Atributos de una serie
# s.size : Devuelve el número de elementos de la serie s.
#s.index : Devuelve una lista con los nombres de las filas del DataFrame s.
#s.dtype : Devuelve el tipo de datos de los elementos de la serie s.

#Dataframe
#Dataframe a partir de un diccionario
import pandas as pd
datos = {'nombre':['María', 'Luis', 'Carmen', 'Antonio'],
'edad':[18, 22, 20, 21],
'grado':['Economía', 'Medicina', 'Arquitectura', 'Economía'],
'correo':['maria@gmail.com', 'luis@yahoo.es', 'carmen@gmail.com', 'antonio@gmail.com']
}
df = pd.DataFrame(datos)
print(df)

# creacion de un dataframe a partir de una lista de listas
import pandas as pd
df = pd.DataFrame([['María', 18], ['Luis', 22], ['Carmen', 20]], columns=['Nombre', 'Edad'])
print(df)

# Pandas
dictc ={"country":["Brazil","Russia","India",
"China", "SouthAfrica","Colombia"],
"capital": ["Brasilia","Moscow","NewDehli",
"Beijing", "Pretoria","Bogota"],
"area": [8.516,17.10,3.286,9.597,1.221,1.142],
"population": [200.4,143.5,1252,1357,52.98,49.65]}

import pandas as pd
brics =pd.DataFrame(dictc) # Dataframe, tabla
print(brics)

# cargar archivos
from google.colab import files
uploaded =files.upload()#Uploadfiles/SalesJan2009.csv

# Import pandas as pd

# Es posiblecargarlosdatosyvisualizarcomosevenparapandas.
# El archivo contiene una lista de transacciones realizadas con diferentes
# medios de pago en diferentes paises:


import pandas as pd
from collections import Counter
ventasdf =pd.read_csv("SalesJan2009.csv")
ventasdf.head(3)

# Es posible cargar los datos,listar los 3 paises y las 3 franquicias de tarjetas
# en las que se realizan mas transacciones:

import pandas as pd
from collections import Counter
ventasdf =pd.read_csv("SalesJan2009.csv")
#print(ventas)
cp =Counter(ventasdf["Country"])
print(cp.most_common(3))
cv =Counter(ventasdf["Payment_Type"])
print(cv.most_common(3))

# Pandas y otras librerias
# Adicionalmente esposiblerealizarconsultasyoperacionessobrelos
# *.csv. A continuacion se grafican las ventas porfecha.
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

#https://jdvelasq.github.io/courses/ciencia_de_los_datos/index.html
