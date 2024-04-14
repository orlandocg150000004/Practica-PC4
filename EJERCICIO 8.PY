import requests
import sqlite3
from datetime import datetime

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  # Levanta una excepción si la solicitud falla
        datos = response.json()
        return datos["bpi"]
    except requests.RequestException as e:
        print("Error al obtener el precio del Bitcoin:", e)
        return None

def obtener_tipo_cambio_pen(fecha):
    try:
        url = "https://api.apis.net.pe/v1/tipo-cambio"
        parametros = {"fecha": fecha, "moneda": "PEN"}
        response = requests.get(url, params=parametros)
        response.raise_for_status()  # Levanta una excepción si la solicitud falla
        datos = response.json()
        return datos["compra"]
    except requests.RequestException as e:
        print("Error al obtener el tipo de cambio del PEN:", e)
        return None

def crear_tabla_bitcoin(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                        fecha TEXT PRIMARY KEY,
                        precio_usd REAL,
                        precio_gbp REAL,
                        precio_eur REAL,
                        precio_pen REAL
                    )''')

def almacenar_datos_en_tabla(cursor, precio_bitcoin, tipo_cambio_pen):
    if precio_bitcoin and tipo_cambio_pen:
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        precio_pen = precio_bitcoin["USD"]["rate_float"] * tipo_cambio_pen
        cursor.execute('''INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen)
                            VALUES (?, ?, ?, ?, ?)''', (fecha, precio_bitcoin["USD"]["rate_float"],
                                                        precio_bitcoin["GBP"]["rate_float"],
                                                        precio_bitcoin["EUR"]["rate_float"],
                                                        precio_pen))
    else:
        print("No se pueden almacenar datos vacíos.")

def calcular_precio_compra_10_bitcoins(cursor):
    cursor.execute("SELECT precio_pen, precio_eur FROM bitcoin ORDER BY fecha DESC LIMIT 1")
    fila = cursor.fetchone()
    if fila:
        precio_pen = fila[0]
        precio_eur = fila[1]
        precio_compra_10_bitcoins_pen = precio_pen * 10
        precio_compra_10_bitcoins_eur = precio_eur * 10
        print(f"Precio de comprar 10 bitcoins en PEN: {precio_compra_10_bitcoins_pen} PEN")
        print(f"Precio de comprar 10 bitcoins en EUR: {precio_compra_10_bitcoins_eur} EUR")
    else:
        print("No se encontraron datos en la tabla bitcoin.")

def main():
    # Crear o conectar a la base de datos
    conexion = sqlite3.connect("base.db")
    cursor = conexion.cursor()

    # Obtener el precio del Bitcoin y el tipo de cambio del PEN
    precio_bitcoin = obtener_precio_bitcoin()
    tipo_cambio_pen = obtener_tipo_cambio_pen(datetime.now().strftime("%Y-%m-%d"))

    # Crear la tabla si no existe
    crear_tabla_bitcoin(cursor)

    # Almacenar los datos en la tabla
    almacenar_datos_en_tabla(cursor, precio_bitcoin, tipo_cambio_pen)

    # Calcular el precio de comprar 10 bitcoins
    calcular_precio_compra_10_bitcoins(cursor)

    # Confirmar los cambios y cerrar la conexión
    conexion.commit()
    conexion.close()

if __name__ == "__main__":
    main()