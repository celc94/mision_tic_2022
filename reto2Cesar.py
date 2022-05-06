#Se recibe las armas elegidas por el equipo Vampiric Ghost
av = input('Equipo Vampiric Ghost, ingrese el conjunto de armas elegidas: ')
#Se recibe las armas elegidas por el equipo Frenzy Shooters
af = input('Equipo Frenzy Shooters, ingrese el conjunto de armas elegidas: ')
#Realizar el despliegue de Armas del Reloj
ar = input('Realice el despliegue de armas del reloj: ')

#Para realizar el almacenamiento de la información recibida por el usuario,
#se puede utilizar listas, pero, se utiliza tuplas ya que ocupan menos 
#espacio en memoria, y no pueden ser modificadas.
armasVampiric = tuple(av)
armasFrenzy = tuple(af)
armasReloj = tuple(ar)

#Se utiliza un acumulador, para almacenar los puntajes de cada equipo
puntajeVampiric = 0
puntajeFrenzy = 0

#Se utiliza el primer ciclo for, para recorrer las armas del reloj, que son las
#que se comparan con las armas de los equipos
for aRe in armasReloj:
#Se utiliza un ciclo for dentro del primer ciclo for del reloj, para recorrer las armas del equipo 1
  for aVa in armasVampiric:
#Se utiliza un condicional para comparar las armas, si son iguales cuenta un punto, sino cero puntos
    if aRe == aVa:
      puntajeVampiric += 1
#Se utiliza un ciclo for dentro del primer ciclo for del reloj, para recorrer las armas del equipo 2
  for aFr in armasFrenzy:
    if aRe == aFr:
      puntajeFrenzy += 1

#Se utilizar un condicional para comparar los acumuladores y poder mostrar en pantalla los resultados,
#de cada comparación, se utiliza el end'', ya que se debe de mostrar los resultados de forma horizontal
  if puntajeVampiric > puntajeFrenzy:
    print('V', end='')
  elif puntajeVampiric < puntajeFrenzy:
    print('F', end='')
  else:
    print('≈', end='')