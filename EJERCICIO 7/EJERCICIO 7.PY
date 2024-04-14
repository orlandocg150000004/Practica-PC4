import sqlite3
import requests

def obtener_tipo_cambio_2023():
    url = "https://api.apis.net.pe/v1/tipo-cambio/anual/2023"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data['data']
        else:
            print("Error al obtener los datos del API")
            return None
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)
        return None

def crear_tabla():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                        fecha TEXT,
                        precio_compra REAL,
                        precio_venta REAL
                    )''')
    conn.commit()
    conn.close()

def insertar_datos(datos):
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    for registro in datos:
        cursor.execute('''INSERT INTO sunat_info (fecha, precio_compra, precio_venta)
                          VALUES (?, ?, ?)''', (registro['fecha'], registro['compra'], registro['venta']))
    conn.commit()
    conn.close()

def mostrar_contenido_tabla():
    conn = sqlite3.connect('base.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM sunat_info''')
    filas = cursor.fetchall()
    print("Contenido de la tabla sunat_info:")
    for fila in filas:
        print(fila)
    conn.close()

def main():
    datos_tipo_cambio = obtener_tipo_cambio_2023()
    if datos_tipo_cambio:
        crear_tabla()
        insertar_datos(datos_tipo_cambio)
        mostrar_contenido_tabla()

if __name__ == "__main__":
    main()
