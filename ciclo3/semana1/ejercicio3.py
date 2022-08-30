#Funciones
def operacionesMatematicas():
    while True:
        print('1. Suma')
        print('2. Resta')
        print('3. Multiplicación')
        print('4. División')
        print('5. Salir') 
        opc = int(input('Elija una opción:'))
        
        if opc == 1:
            num1 = int(input('Digite un número: '))
            num2 = int(input('Digite un número: '))
            suma = num1 + num2
            print(f'El valor de la suma es: {suma}')

        elif opc == 2:
            num1 = int(input('Digite un número: '))
            num2 = int(input('Digite un número: '))
            resta = num1 - num2
            print(f'El valor de la resta es: {resta}')

        elif opc == 3:
            num1 = int(input('Digite un número: '))
            num2 = int(input('Digite un número: '))
            multiplicacion = num1 * num2
            print(f'El valor de la multiplicación es: {multiplicacion}')

        elif opc == 4:
            num1 = int(input('Digite un número: '))
            num2 = int(input('Digite un número: '))
            division = num1 / num2
            print(f'El valor de la división es: {division}')

        else:
            break