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

def main():
    # Solicitar al usuario la cantidad de bitcoins que posee
    try:
        cantidad_bitcoins = float(input("Ingrese la cantidad de bitcoins que posee: "))
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")
        return

    # Obtener el precio actual de Bitcoin en USD
    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin is not None:
        # Calcular el costo total en USD de la cantidad de bitcoins
        costo_total_usd = cantidad_bitcoins * precio_bitcoin
        # Mostrar el costo actual de "n" bitcoins en USD con cuatro decimales y separador de miles
        print(f"El costo actual de {cantidad_bitcoins:,.4f} bitcoins es: ${costo_total_usd:,.4f}")

if __name__ == "__main__":
    main()
