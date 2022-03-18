import json
import requests

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=9N3E66AEYSMKXXHT'
r = requests.get(url)
data = json.loads(r.text)
BTCtoUSD = data['Realtime Currency Exchange Rate']['5. Exchange Rate']

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=EUR&apikey=9N3E66AEYSMKXXHT'
r = requests.get(url)
data = json.loads(r.text)
BTCtoEUR = data['Realtime Currency Exchange Rate']['5. Exchange Rate']

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=ARS&apikey=9N3E66AEYSMKXXHT'
r = requests.get(url)
data = json.loads(r.text)
USDtoARS = data['Realtime Currency Exchange Rate']['5. Exchange Rate']

url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=ARS&apikey=9N3E66AEYSMKXXHT'
r = requests.get(url)
data = json.loads(r.text)
EURtoARS = data['Realtime Currency Exchange Rate']['5. Exchange Rate']

print("BTC en dolares: " + BTCtoUSD)
print("BTC en euros: " + BTCtoEUR)
print("USD en pesos: " + USDtoARS)
print("EUR en pesos: " + EURtoARS)
