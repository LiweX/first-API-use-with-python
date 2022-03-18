import requests

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=9N3E66AEYSMKXXHT'
r = requests.get(url)
data = r.json()
print(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])