import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        if response.status_code == 200:
            data = response.json()
            return data['bpi']['USD']['rate_float']
        else:
            print("Error al obtener el precio de Bitcoin")
            return None
    except requests.RequestException as e:
        print("Error de conexión:", e)
        return None

def guardar_datos_en_archivo(precio_bitcoin, cantidad_bitcoins):
    try:
        with open("datos_bitcoin.txt", "w") as file:
            file.write(f"Precio de Bitcoin: ${precio_bitcoin:.4f}\n")
            file.write(f"Cantidad de Bitcoins: {cantidad_bitcoins:.6f}\n")
            file.write(f"Costo total en USD: ${precio_bitcoin * cantidad_bitcoins:.4f}\n")
        print("Datos guardados en 'datos_bitcoin.txt'")
    except IOError:
        print("Error al escribir en el archivo")

def main():
    try:
        cantidad_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")
        return

    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin is not None:
        guardar_datos_en_archivo(precio_bitcoin, cantidad_bitcoins)

if __name__ == "__main__":
    main()

