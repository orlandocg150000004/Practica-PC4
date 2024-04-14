import requests
import sqlite3
from datetime import datetime, timedelta

def obtener_tipo_cambio(fecha):
    url = f"https://api.apis.net.pe/v2/sunat/tipo-cambio?date={fecha}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        tipo_cambio = data['exchange_rate']['purchase']
        return tipo_cambio
    else:
        print(f"Error al obtener el tipo de cambio para la fecha {fecha}")
        return None

def guardar_en_base_de_datos(fecha, tipo_cambio_compra, tipo_cambio_venta):
    try:
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                            fecha TEXT PRIMARY KEY,
                            tipo_cambio_compra REAL,
                            tipo_cambio_venta REAL
                        )''')
        cursor.execute('''INSERT INTO sunat_info (fecha, tipo_cambio_compra, tipo_cambio_venta)
                          VALUES (?, ?, ?)''', (fecha, tipo_cambio_compra, tipo_cambio_venta))
        conn.commit()
        conn.close()
        print(f"Datos para la fecha {fecha} guardados en la tabla 'sunat_info'")
    except sqlite3.Error as e:
        print("Error al guardar datos en la base de datos:", e)

def mostrar_contenido_tabla():
    try:
        conn = sqlite3.connect('base.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM sunat_info''')
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        conn.close()
    except sqlite3.Error as e:
        print("Error al mostrar contenido de la tabla:", e)

def main():
    fecha_inicio = datetime(2023, 1, 1)
    fecha_fin = datetime(2023, 12, 31)
    delta = timedelta(days=1)

    while fecha_inicio <= fecha_fin:
        fecha = fecha_inicio.strftime("%Y-%m-%d")
        tipo_cambio_compra = obtener_tipo_cambio(fecha)
        tipo_cambio_venta = obtener_tipo_cambio(fecha)
        
        if tipo_cambio_compra is not None and tipo_cambio_venta is not None:
            guardar_en_base_de_datos(fecha, tipo_cambio_compra, tipo_cambio_venta)
        
        fecha_inicio += delta

    mostrar_contenido_tabla()

if __name__ == "__main__":
    main()
