import random # se importa la libreria de python random

#Se define una lista
sujetos = ['Bebé', 'Princess', 'Mami']
intenciones = ['yo quiero', 'yo puedo', 'yo vengo a', 'voy a']
verbos = ['encendelte', 'amalte', 'ligal', 'jugal']
advs = ['suave', 'lento', 'lápido', 'fuelte']
complementosUno = ['hasta que salga el sol', 'toda la noche', 'hasta el amanecer', 'todo el día']
complementosDos = ['sin anestecia', 'sin compromiso', 'feis to feis', 'sin miedo']

#Se utiliza la libreria choice para seleccionar un elemento al azar
sujetoSeleccionado = random.choice(sujetos)
intencionSeleccionada = random.choice(intenciones)
verboSeleccionado = random.choice(verbos)
advsSeleccionado = random.choice(advs)
comp1 = random.choice(complementosUno)
comp2 = random.choice(complementosDos)
print(f'Letra generada: {sujetoSeleccionado} {intencionSeleccionada} {verboSeleccionado} {advsSeleccionado} {comp1} {comp2}.')