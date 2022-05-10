#Condicionales en las listas
text =["cien","años","de","soledad"]
if "años" in text :
  print("Si está en la lista.")
else:
  print("No está en la lista.")

#Escribir un programa que almacene las asignaturas de un curso 
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una 
#lista y la muestre por pantalla.
asignatura = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
print(asignatura)

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
#Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio 
#asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
asignatura = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
for a in asignatura:
  print(f'Yo estudio: {a}')

#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
#en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje 
#En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las 
#correspondientes notas introducidas por el usuario.
subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
scores = []
for subject in subjects:
    score = input("¿Qué nota has sacado en " + subject + "?")
    scores.append(score)
for i in range(len(subjects)):
    print("En " + subjects[i] + " has sacado " + scores[i])

#Escribir un programa que pregunte al usuario los números ganadores 
#de la lotería primitiva, los almacene en una lista y los muestre por 
#pantalla ordenados de menor a mayor.
num= input('Ingrese los números ganadores de la lotería: ')
numeros = list(num)
ordenados = sorted(numeros)
print(ordenados)

#Escribir un programa que almacene en una lista los números del 1 al 10 
#y los muestre por pantalla en orden inverso separados por comas.
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num.reverse()
print(num)

#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
texto = input('Ingrese una palabra o un número: ')
txt = list(texto)
for a in txt:
  texto1 = a
for b in reversed(txt):
  texto2 = b
if texto1 == texto2:
  print('Es un palíndromo.')
else:
  print('No es un palíndromo.')