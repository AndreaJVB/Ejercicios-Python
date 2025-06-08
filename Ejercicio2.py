# Escriba un programa que solicite un número al usuario y
# muestre la tabla de multiplicar del 1 al 10 de ese número.

try:
    numero = int(input("Inrese un numero para mostrar la tabla de multiplicar: "))

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

except ValueError:
    print("Porfavor ingrese un numero entero valido")