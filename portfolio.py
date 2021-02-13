import json
from requests import Session
from prettytable import PrettyTable

x = PrettyTable()

api_key = '0ed0eb04-94e3-4ce1-aa32-cbac4f8702f1'
global_url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
    'convert': 'USD',
    'symbol': ''
}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': api_key,
}

x.field_names = ["Asset", "Amount", "Value Owned", "Current Price", "1H", "24H", '7D']


def get_coin(coin, amount):
    parameters['symbol'] = coin

    session = Session()
    session.headers.update(headers)

    response = session.get(global_url, params=parameters)
    data = json.loads(response.text)

    coin_price = data['data'][coin]['quote']['USD']['price']
    coin_value = amount * coin_price
    coin_hour_change = round(data['data'][coin]['quote']['USD']['percent_change_1h'], 2)
    coin_day_change = round(data['data'][coin]['quote']['USD']['percent_change_24h'], 2)
    coin_week_change = round(data['data'][coin]['quote']['USD']['percent_change_7d'], 2)
    x.add_rows(
        [
            [coin, amount, '$' + str(coin_value), '$' + str(coin_price), coin_hour_change, coin_day_change,
             str(coin_week_change) + '%'],
        ]
    )


def prompt():
    ans = 'y'
    while ans == 'y':
        print('\nEnter coin symbol')
        sym = input()
        sym = sym.upper()
        print('Enter amount')
        am = input()
        am = float(am)
        get_coin(sym, am)
        print(x)
        print('Add another coin? (y/n)')
        ans = input()


prompt()
