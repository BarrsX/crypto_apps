import json
import requests
from requests import Session
from requests import Session
api_key = 'api_key'
global_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'


def coin_finder():
    print('\nEnter coin symbol')
    coin = input()
    coin = coin.upper()

    parameters = {
        'convert': 'USD',
        'symbol': coin
    }

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key,
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(global_url, params=parameters)
    data = json.loads(response.text)

    name = data['data'][coin]['name']
    coin_price = data['data'][coin]['quote']['USD']['price']
    coin_price = round(coin_price, 4)
    coin_day_change = data['data'][coin]['quote']['USD']['percent_change_24h']
    coin_day_change = str(round(coin_day_change, 2)) + '%'
    volume = data['data'][coin]['quote']['USD']['volume_24h']
    volume = round(volume, 2)

    print(name)
    print('price: ' + '$' + str(coin_price))
    print('change in last day: ' + str(coin_day_change))
    print('volume in last day: ' + str(volume))


while True:
    coin_finder()
    print('Run again? (y/n)')
    leave = input()
    if leave == 'n':
        break
