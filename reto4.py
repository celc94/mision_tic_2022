import json

laminas = json.loads(input()) 
mis_laminas = str(input())

precio_total = 0
laminas_disponibles = []
for i in mis_laminas.split(" "):
    precio_lamina = laminas.get(i)
    if precio_lamina:
        precio_total += precio_lamina
        laminas_disponibles.append(i)

print(precio_total)
print(' '.join(str(l) for l in laminas_disponibles))