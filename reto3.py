#Ingresar la combinación del sonido de las cuerdas. 
combinacioncuerdas =  input("Ingrese la combinación de sonido de las cuerdas: ")
cuerdas = combinacioncuerdas.replace(',','')
combinacioncuerdas = cuerdas.upper()

#Lista que almacena las letras y el total de letras
listacuerdas = []    
total_letras = []

#Contador y almacén de letras
contador = 1

#Ciclo For para el input de cuerdas
for c in combinacioncuerdas:
    #Si la lista esta vacia, incluye el primer valor
    if len(listacuerdas) == 0:
      listacuerdas.append(c)
    #Si la lista tiene valores, la revisa al reves para ver si lo incluye o no
    #y asi no incluye valores repetidos
    elif len(listacuerdas) > 0:
        if listacuerdas[-1] != c:
            listacuerdas.append(c)

#Aqui concateno los resultados
resultadocombinacion = ' '.join(listacuerdas)
#Como  los resultados salen juntos, list separa letra a letra
#resultado = list(resultado)
print(resultadocombinacion)

#Este apartado pertenece a la cantidad de letras repetidas
if len(listacuerdas) > 0:
    #Itero en el rango de 1 hasta la longitud
    #asi no se desborda el ciclo
    #Inicio el rango en 1 para lograr comparar el anterior
    for i in range(1, len(combinacioncuerdas)):
        #Si la letra en la posicion 1 es 
        #igual a la letra de la posicion 0
        #se acumula el contador, sino, lo reinicia en 1
        if combinacioncuerdas[i - 1] == combinacioncuerdas[i]:
            contador += 1
        else:
            total_letras += '' + str(contador)
            contador = 1

#Se imprime los resultados del total de letras
total_letras += '' + str(contador)
resultado_letras = ' '.join(total_letras)
print(resultado_letras)