# Uso de la API de Alpha Vintage para consultar el precio de criptomonedas con Python3.
Nos registramos en https://www.alphavantage.co/support/#api-key para obtener nuestra APIkey.
Creamos un archivo .py en nuestra ide favorita.
Siguiendo el ejemplo propuesto por la documentacion de la API podemos obtener la cotizacion del BTC en USD.
```
import requests

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=**************'
r = requests.get(url)
data = r.json()

print(data)
```
Donde se reemplazan los asteriscos por la APIkey obtenida.
Se corre desde la terminal usando python3
`python3 *.py`
La salida del programa seria la siguiente.
```
{
    "Realtime Currency Exchange Rate": {
        "1. From_Currency Code": "BTC",
        "2. From_Currency Name": "Bitcoin",
        "3. To_Currency Code": "USD",
        "4. To_Currency Name": "United States Dollar",
        "5. Exchange Rate": "41509.96000000",
        "6. Last Refreshed": "2022-03-18 17:53:03",
        "7. Time Zone": "UTC",
        "8. Bid Price": "41509.95000000",
        "9. Ask Price": "41509.96000000"
    }
}
```
