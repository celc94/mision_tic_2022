#Leer datos de juego, Strings
#vmp -> Armas clan Vampiric Ghosts
#frn -> Armas clan Frenzy Shooters
#clk -> Reloj de juego
vmp=input()   
frn=input()
clk=input()
# Convierte las cadenas leídas en listas
vmpArm=list(vmp)
frnArm=list(frn)
clkSec=list(clk)
#Inicializa acumuladores de puntaje para cada equipo
frnpnt=0
vmppnt=0
for i in clkSec:
    #Compara el valor de arma indicado por el reloj con las armas del equipo Frenzy
    #Si coincide el arma del reloj con alguna de las elegidas por el equipo acumula puntaje
    for j in frnArm:
        if(i==j):
            frnpnt=frnpnt+1
#Compara el valor de arma indicado por el reloj con las armas del equipo Vampiric
    #Si coincide el arma del reloj con alguna de las elegidas por el equipo acumula puntaje
    for k in vmpArm:
        if(i==k):
            vmppnt=vmppnt+1
#Compara puntajes acumulados y entrega el resultado segun condiciones del reto
    if(frnpnt==vmppnt):
        print("≈",end="")
    if(frnpnt>vmppnt):
            print("F",end="")
    if(vmppnt>frnpnt):
            print("V",end="")