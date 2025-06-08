#Cree un programa que elimine los elementos repetidos de una
#lista y devuelva una nueva lista con elementos únicos ordenados.
numeros = []
try:
    for i in range(8):
        n = int(input(f"Ingrese el numero {i + 1}: "))
        numeros.append(n)

    print(f"Lista de numeros inresados anteriormente: {numeros}")

    numeros_unicos = []

    for numero in numeros:
        if numero not in numeros_unicos:
            numeros_unicos.append(numero)

    for i in range(len(numeros_unicos)):
        for j in range(i + 1, len(numeros_unicos)):
            if numeros_unicos[i] > numeros_unicos[j]:
                temp = numeros_unicos[i]
                numeros_unicos[i] = numeros_unicos[j]
                numeros_unicos[j] = temp

    print(f"Lista de numeros unicos ordenados: {numeros_unicos}")

except ValueError:
    print("Por favor, ingrese un número entero válido.")
    