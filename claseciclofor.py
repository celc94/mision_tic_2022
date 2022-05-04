#Imprimir una lista de 11 índices 
lista1 = ['Colombia', 'Ecuador', 'Guatemala', 'Venezuela', 'Brasil', 'Perú', 'Argentina', 'Uruguay', 'Chile', 'México', 'Estados Unidos'] 
lista2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lista3 =['Loverpool', 'Barcelona', 'United', 'City', 'Everton', 'Leeds', 'Totenham', 'Real Matrid', 'Sevilla', 'Atlético']
lista_concatenada = lista1 + lista2
lista2.append(11) #Agrega un nuevo índice a una lista
lista1.insert(0, 'Canadá') #Agrega un nuevo índice a una lista, indicando la posición
print(lista2)
print(lista1)
print(f'La posición 5 es: {lista1[5]}')
print(f'La posición 10 es: {lista2[10]}')
print(f'La posición 3 es: {lista3[1]}')
print(f'La concatenación de las listas es: {lista_concatenada}')

lista = ['Colombia', 'Ecuador', 'Guatemala', 'Venezuela', 'Brasil', 'Perú', 'Argentina', 'Uruguay', 'Chile', 'México', 'Estados Unidos'] 
print(lista[0:3]) #Imprime el rango de una lista

list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [11,12,13,14,15,16,17,18,19,20]

print("Numero de elementos lista 1:", len (list1)) #len: devuelve un número entero que indica el tamaño de lo que está dentro
print("Numero de elementos lista 1:", len (list2))

#Ciclo For
list1 = ['Colombia', 'Ecuador', 'Guatemala', 'Venezuela']
for a in list1:
  print (a, end=" ")

  #Ciclo For
list1 = [1,2,3,4,5,6,7,8,9,10]
for a in list1:
  print (a, end="")

  for i in [2,4,6]:
  print (i)

  for i in [2,4,6,9]:
  print ("omar")

#Números Pares  
  listaNumeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in listaNumeros:
  if num % 2 == 0:
    print(f'Los números pares son: {num}')
else:
  print('Fin del Ciclo For')

#imprime en el ciclo varias cadenas hasta que termine el ciclo for

for lista in ['calcetin', 'blusa', 'pantalon']:
  print(f'la lavadora se ha comido mi ',lista)
  