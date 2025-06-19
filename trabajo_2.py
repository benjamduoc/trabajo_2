promedios_estudiantes = {
    "juan": 5.0,
    "maria": 6.0,
    "pedro": 4.5
}

nuevos_estudiantes = []

def mostrar_menu():
    print("--- MENÚ ---")
    print("1. Ver promedio de estudiante")
    print("2. Agregar estudiante y calcular promedio")
    print("3. Mostrar nuevos estudiantes agregados")
    print("4. Salir")

def calcular_promedio(n1, n2, n3):
    promedio = (n1 + n2 + n3) / 3
    return promedio

def pedir_notas():
    try:
        nota1 = float(input("Ingrese la nota 1: "))
        nota2 = float(input("Ingrese la nota 2: "))
        nota3 = float(input("Ingrese la nota 3: "))

        if (nota1 < 1 or nota1 > 7) or (nota2 < 1 or nota2 > 7) or (nota3 < 1 or nota3 > 7):
            print("Las notas deben estar entre 1 y 7.")
            return None, None, None
        return nota1, nota2, nota3

    except ValueError:
        print("Error: debe ingresar un número válido.")
        return None, None, None

def ver_promedio():
    nombre = input("Ingrese el nombre del estudiante: ").lower()
    if nombre in promedios_estudiantes:
        promedio = promedios_estudiantes[nombre]
        print(f"El promedio de {nombre} es: {promedio:.2f}")
    else:
        print("Estudiante no encontrado.")

def agregar_estudiante():
    nombre = input("Ingrese el nombre del nuevo estudiante: ").lower()

    if nombre in promedios_estudiantes:
        print("El estudiante ya existe.")
        return

    nota1, nota2, nota3 = pedir_notas()
    if nota1 is not None:
            promedio = calcular_promedio(nota1, nota2, nota3)
            promedios_estudiantes[nombre] = promedio
            nuevos_estudiantes.append(nombre)
            print(f"Estudiante {nombre} agregado con promedio: {promedio:.1f}")

def mostrar_nuevos_estudiantes():
    if len(nuevos_estudiantes) == 0:
        print("No hay nuevos estudiantes registrados.")
    else:
        print("Nuevos estudiantes registrados:")
        for estudiante in nuevos_estudiantes:
            print(f"- {estudiante}")

opcion = ''
while opcion != '4':
    mostrar_menu()
    opcion = input("Seleccione una opción (1-4): ")

    if opcion == '1':
        ver_promedio()
    elif opcion == '2':
        agregar_estudiante()
    elif opcion == '3':
        mostrar_nuevos_estudiantes()
    elif opcion == '4':
        print("Saliendo del programa. ¡Hasta luego!")
    else:
        print("Opción inválida. Intente nuevamente.")
