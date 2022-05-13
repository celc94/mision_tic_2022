#{22:'SSH', 23:'Telnet',80:'HTTP',3306:'MySQL'}

#x ={}

puertos ={22:'SSH',23:'Telnet',80:'HTTP',3306:'MySQL'}
print (puertos)

# Metodo Update
dict_ports1 ={22:"SSH",80:"Http"}
dict_ports2 ={53:"DNS",443:"https"}
dict_ports3 ={25:"JKL",90:"htt"}
print(dict_ports1)
dict_ports1.update(dict_ports2)
print(dict_ports1)
dict_ports1.update(dict_ports3)
print(dict_ports1)

#comparar diccionarios
a ={123:"Rojas",87:"Rosas"}=={87:"Rosas",123:"Rojas"}
print(a)
print({"Rosas":123} !={"rosas":123})


b ={123:"Rosas",87:"rojas"}=={"Rosas":123,87:"rojas"}
print(b)

#acceder al valor de un item con la clave dada // sino existe se genera error
puertos ={22:"SSH",23:"Telnet",80:"HTTP",3306:"MySQL"}
protocolo =puertos[22]
print(protocolo)
#protocolo =puertos[443]
#print(protocolo)

#Agrega si no existe o modifica si existe el valor de un item con la clave dada. 
puertos ={80:"HTTP",23:"SMTP",443:"HTTPS"}
print(puertos)
puertos[23] ="Telnet"
print(puertos)
puertos[110] ="  "
print(puertos)

# eliminando elementos del diccionario con el comando del
puertos ={22:"SSH",23:"Telnet",80:"HTTP",3306:"MySQL"}
print(puertos)
del puertos[23]
print(puertos)

#Es posible determinar si en un diccionario existe un item que tenga asociada una clave
puertos ={80:"HTTP",23:"SMTP",443:"HTTPS"}
if 80 in puertos:
  print("yes")
if 110 not in puertos:
    print("no")
else:
  print("yes")

#Iterando un Diccionario usando ciclo for para obtener las claves
dict_ports ={22:"SSH",23:"telnet",80:"Http"}
for key in dict_ports:
  print(key)

#Iterando un Diccionario usando ciclo for para obtener las claves
dict_ports ={22:"SSH",23:"telnet",80:"Http"}
for key in dict_ports.keys():
  print(key)

dict_ports ={22:"SSH",23:"telnet",80:"Http"}
for valor in dict_ports.values():
  print(valor)

dict_ports ={22:"SSH",23:"telnet",80:"Http"}
for k,l in dict_ports.items():
  print(k,l)

#Metodo Len para un Diccionario
#La función len determina el numero de terminos
# de un diccionario.
puertos ={80:"HTTP",23:"SMTP",443:"HTTPS"}
print(len(puertos))

dict1 ={"a":1,"b":2,"c":3}
print(dict1.get("a"))
print(dict1.get("d", "clave no encontrada."))

puertos ={80:"HTTP",23:"SMTP",443:"HTTPS"}
print(max(puertos))
print(min(puertos))

#Listas de las claves de un diccionario
#Metodo Key : obtiene una lista con todas las claves
#Metodo Values: Obtiene una lista con todos los valores
dict1 ={"a":1,"b":2,"c":3}

#print(list(dict1.keys()))

#print(list(dict1.values()))

# Metodo dict
#Permite convertir listas de listas  y listas de tuplas a diccionarios

puertos =[[80,"http"],[20,"ftp"],[23,"telnet"]]
d_port =dict(puertos)
print(d_port)

puertos =[(20,"ftp"),(80,"http"),(23,"telnet")]
d_port =dict(puertos)
print(d_port)

#Eliminar Entradas
#Metodo Clear elimina todo el item del diccionario

dict_ports ={22:"SSH",23:"telnet",80:"Http"}
print(dict_ports)
dict_ports.clear()
print(dict_ports)

#copiar diccionario
port ={80:"HTTP",23:"SMTP",443:"HTTPS"}
copy_port =port.copy()
false_copy =port
print(port)
print(copy_port)
print(false_copy)

diccionario1 = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
diccionario2 = {
    'IDE': 'Integrated Development Enviroment',
    'OOP': 'Object Oriented Programming',
    'DBMS': 'Database Management System'
}
for key1, valor1 in diccionario1.items():
  True
for key2, valor2 in diccionario2.items():
  True
if key1 == key2 and valor1 == valor2:
    print('Las claves y valores del diccionario 1, se encuentran en el diccionario 2.')
else:
    print('Las claves y valores del diccionario 1, no se encuentran en el diccionario 2.')

#Escribir un programa que pregunte al usuario su nombre, 
#edad, dirección y teléfono y lo guarde en un diccionario. 
#Despúes debe mostrar por pantalla el mensaje <nombre> tiene 
#<edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
name    = input()
age     = input()
address = input()
phone   = input()
dic = {}

dic['name'] = name
dic['age'] = age
dic['address'] = address
dic['phone'] = phone

for key in dic:
    print('My ', key, ': ', dic[key])


#Escribir un programa que guarde en una variable el diccionario 
#{'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa 
#y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.

dicc = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
a = input("digite la divisa: ")
print(dicc.get(a, "Divisa no encontrada."))

cadena = "Hola Mundo" 
print (cadena.upper())

f = "Rapido corren los carros"
f.split(',')

str = "Rapido,corren,los,carros"
str.split(' ')

f = input()
f.replace(","," ")

