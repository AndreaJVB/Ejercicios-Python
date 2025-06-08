## Dado el siguiente diccionario:
ventas = {
 'Producto': ['A', 'B', 'A', 'C', 'B', 'A'],
 'Cantidad': [10, 5, 7, 3, 2, 8]
 }

 ## Agrupa las cantidades por producto y muestra la suma total de ventas por cada uno
agrupados = {}

for i in range(len(ventas['Producto'])):
    producto = ventas['Producto'][i]
    cantidad = ventas['Cantidad'][i]
    
    if producto in agrupados:
        agrupados[producto] += cantidad
    else:
        agrupados[producto] = cantidad

print("Ventas totales por producto:")
print(agrupados)