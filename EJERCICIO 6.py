def count_loc(file_path):
    try:
        with open(file_path, 'r') as file:
            loc_count = 0
            for line in file.readlines():
                # Eliminar espacios en blanco al principio y al final de la línea
                stripped_line = line.strip()
                # Verificar si la línea no está en blanco y no es un comentario
                if stripped_line != '' and not stripped_line.startswith('#'):
                    loc_count += 1
        return loc_count
    except FileNotFoundError:
        print(f"El archivo '{file_path}' no fue encontrado.")
        return None

# Ruta del archivo Python a analizar
file_path = 'tu_archivo.py'

# Contar las líneas de código (LOC)
loc = count_loc(file_path)
if loc is not None:
    print(f"El número de líneas de código (LOC) en el archivo '{file_path}' es: {loc}")
