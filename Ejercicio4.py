## Escriba un programa que solicite ingresar el nombre de varios
##estudiantes y su nota, y lo almacene en un diccionario. Al final, muestra los
##datos almacenados.
try:
    n = int(input("Ingrese la cantidad de estudiantes: "))

    estudiantes = {}

    for i in range(n):
        nombre = input(f"Ingrese el nombre del estudiante {i +1}: ") 
        nota = float(input(f"Ingrese la nota del estudiante {i +1}. {nombre}: "))

        estudiantes[nombre] = nota

    print("\nDatos de los estudiantes:")
    for nombre, nota in estudiantes.items():
        print(f"Nombre: {nombre}, Nota: {nota}")

    print("\nSalida esperada: ")
    print(estudiantes)
except ValueError:
    print("Error en la entrada de datos.")
