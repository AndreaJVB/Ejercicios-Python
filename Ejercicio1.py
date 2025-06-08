##Cree un programa que reciba una lista de números y devuelva el número mayor sin usar la función
##max().

numeros = []
try:
    n = int(input("¿Cuantos numeros desea ingresar?: "))

    for i in range(n):
        numero = int(input(f"Ingrese el numero {i + 1}: "))
        numeros.append(numero)
except ValueError:
    print("Por favor, ingrese un número entero válido.")
    numeros.append(0)

mayor = numeros[0]

for n in numeros:
    if n > mayor:
        mayor = n

print("El numero mayor: ", mayor)