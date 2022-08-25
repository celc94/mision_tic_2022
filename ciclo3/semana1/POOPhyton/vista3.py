import nomina as no

nombre=input('Digite su nombre: ')
horas=int(input('Digite las horas trabajadas: '))

total=no.Nomina(nombre,horas)

print(total.getnombre())
print(total.gethora())
print(total.pagototal())

