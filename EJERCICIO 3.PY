import requests
import zipfile
import os

def descargar_imagen(url, nombre_archivo):
    response = requests.get(url)
    if response.status_code == 200:
        with open(nombre_archivo, 'wb') as f:
            f.write(response.content)
        print(f"Imagen descargada como '{nombre_archivo}'")
    else:
        print("Error al descargar la imagen")

def comprimir_zip(archivos, nombre_zip):
    with zipfile.ZipFile(nombre_zip, 'w') as zipf:
        for archivo in archivos:
            zipf.write(archivo)
    print(f"Archivos comprimidos en '{nombre_zip}'")

def descomprimir_zip(nombre_zip, directorio_destino):
    with zipfile.ZipFile(nombre_zip, 'r') as zipf:
        zipf.extractall(directorio_destino)
    print(f"Archivo '{nombre_zip}' descomprimido en '{directorio_destino}'")

if __name__ == "__main__":
    # Descargar la imagen desde el URL
    url = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    nombre_imagen = "imagen_descargada.jpg"
    descargar_imagen(url, nombre_imagen)

    # Comprimir la imagen en un archivo ZIP
    archivos_a_comprimir = [nombre_imagen]
    nombre_zip = "archivo_comprimido.zip"
    comprimir_zip(archivos_a_comprimir, nombre_zip)

    # Descomprimir el archivo ZIP
    directorio_destino = "imagen_descomprimida"
    descomprimir_zip(nombre_zip, directorio_destino)
