import requests

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=ARS&apikey=9N3E66AEYSMKXXHT'
r = requests.get(url)
data = r.json()

print(data)