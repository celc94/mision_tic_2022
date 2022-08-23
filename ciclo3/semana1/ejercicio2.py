print('Suma de productos')
productos = int(input('Ingrese el total de archivos a comprar: '))
suma = 0
for i in range(productos):
    precio_producto = int(input('Ingrese el precio del producto: '))
    suma += precio_producto
print('El total de la suma de producto es: ',suma)