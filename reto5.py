def tipodefigurita(listaLaminas):
    sinRepetir = []
    for lamina in listaLaminas:
        if lamina not in sinRepetir:
            sinRepetir.append(lamina)
    return sinRepetir

def mefaltandeltipodefigurita(laminasQueFaltan, listaDeTiposLamina, tipoLaminas):
    numerofaltante = []
    for lamina in laminasQueFaltan:
        if listaDeTiposLamina[lamina] == tipoLaminas:
            numerofaltante.append(lamina)
    return numerofaltante

def notengo(laminasIntercambio,misRepetidos):
    laminasFaltantes = []
    for lamina in laminasIntercambio:
        if lamina not in misRepetidos:
            laminasFaltantes.append(lamina)
    return laminasFaltantes

def puedocambiar(susRepetidos, misRepetidos):

    interesan = [[],[]]
    for lamina in susRepetidos:
        if lamina not in misRepetidos:
            interesan[0].append(lamina)
    for lamina in misRepetidos:
        if lamina not in susRepetidos:
            interesan[1].append(lamina)
    print(interesan[0], interesan[1])
    if len(interesan[0]) > len(interesan[1]):
        return len(interesan[1])
    else:
        return len(interesan[0])