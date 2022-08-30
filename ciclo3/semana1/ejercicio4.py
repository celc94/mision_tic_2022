#Algoritmo que suma aparte positivos y aparte negativos y si es cero sale de la función

def funcion():
    suma =0
    sumnegativo =0
    num = int(input("digite numero: "))
    while num!=0:
        if num>0:
            suma += num 
            num = int(input("digite numero: "))

        elif num<0:
            sumnegativo+=num
            num = int(input("digite numero: "))
     

    print(f'la suma de numeros positivos es: {suma}\nla suma de numeros negativos es: {sumnegativo}')

    #Otra opción con listas
    def SumaPosAndNeg ():
    
    ListPos = []
    ListNeg = []
    comando = int(input("Ingresar Números Positivos o Negativos --> "))

    while (comando !=0):
        if (comando <0):
            ListNeg.append(comando)
            comando = int(input("Ingresar Números Positivos o Negativos --> "))
        if (comando >0):
            ListPos.append(comando)
            comando = int(input("Ingresar Números Positivos o Negativos --> "))
 
    print("Suma Positivos -->")
    print(sum(ListPos))