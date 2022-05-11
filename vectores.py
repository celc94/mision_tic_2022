#Vectores
def suma_arreglo(A):
  s = 0
  for x in A:
    s = s + x
  return s
print(suma_arreglo([1,-3,4,11,6]))

#Posición del véctor máximo
def pos_maximo(A):
  m =0
  for i in range(1, len(A)):
    if A[i] > A[m]:
      m = i
  return m
print(pos_maximo([1,-3,4,11,6]))

#Promedio de un vector
def prom(A):
  s =0
  for x in A:
    s = s + x
    p = s / len(A)
  return p
print(prom([10,10,10]))

#Promedio de un vector utilizando numpy
import numpy as np

a = np.array([5,5,5])
p = np.mean(a)
print(p)

#Producto escalar utilizando la librería de Numpy
import numpy as np

a = np.array([2,1])
b = np.array([3,4])
np.dot(a,b) # np.dot = Función para calcular el producto escalar