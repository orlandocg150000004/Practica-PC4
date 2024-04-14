def guardar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", 'w') as file:
            for i in range(1, 11):
                file.write(f"{numero} x {i} = {numero*i}\n")
        print(f"Tabla de multiplicar del número {numero} guardada en tabla-{numero}.txt")
    except FileNotFoundError:
        print("Error al guardar la tabla de multiplicar.")

def mostrar_tabla_multiplicar(numero):
    try:
        with open(f"tabla-{numero}.txt", 'r') as file:
            print(f"Tabla de multiplicar del número {numero}:")
            print(file.read())
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def mostrar_linea_tabla_multiplicar(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", 'r') as file:
            lines = file.readlines()
            if len(lines) >= linea:
                print(f"Línea {linea} de la tabla de multiplicar del número {numero}:")
                print(lines[linea - 1].strip())
            else:
                print(f"El archivo tabla-{numero}.txt no tiene {linea} líneas.")
    except FileNotFoundError:
        print(f"El archivo tabla-{numero}.txt no existe.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Guardar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de tabla de multiplicar")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= numero <= 10:
                guardar_tabla_multiplicar(numero)
            else:
                print("El número ingresado no está dentro del rango permitido.")
        elif opcion == '2':
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            if 1 <= numero <= 10:
                mostrar_tabla_multiplicar(numero)
            else:
                print("El número ingresado no está dentro del rango permitido.")
        elif opcion == '3':
            numero = int(input("Ingrese un número entero entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea que desea mostrar: "))
            if 1 <= numero <= 10:
                mostrar_linea_tabla_multiplicar(numero, linea)
            else:
                print("El número ingresado no está dentro del rango permitido.")
        elif opcion == '4':
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    menu()
