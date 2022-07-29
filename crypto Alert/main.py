from webbrowser import get
import requests
import keys
import email
import pandas as pd
from time import sleep

def get_crypto_rates(base_currency='EUR',assets='BTC,ETH,XRP'):
    url='https://api.nomics.com/v1/currencies/ticker'

    payload = {'key':keys.NOMICS_API_KEY, 'convert':base_currency, 'ids':assets, 'interval':'id'}
    response=requests.get(url, params=payload)
    data = response.json()

    crypto_currency, crypto_price, crypto_timestamp = [], [], []

    for asset in data:
        crypto_currency.append(asset['currency'])
        crypto_price.append(asset['price'])
        crypto_timestamp.append(asset['price_timestamp'])
    raw_data = {
        'assets' : crypto_currency,
        'rates' : crypto_price,
        'timestamp' : crypto_timestamp
    }

    df = pd.DataFrame(raw_data)
    return df

    def set_alert(dataframe, asset, alert_high_price):
        crypto_value = float(dataframe[dataframe['assets']== asset]['rates'].item())

        details = f'{asset}: {crypto_value}, Target: {alert_high_price}'

        if crypto_value>= alert_hight_price:
            print(details + '<< TARGET VALUE REACHED !!')
        else:
            print(details)

    loop = 0
    while True:
        printf(f'---------------------({loop})---------------------')

        try:
            df = get_crypto_rates()

            set_alert(df , 'STC', 50300.50)
            set_alert(df, 'ETH', 1000.80)
            set_alert(df, 'XRP', .870)
        except Exception as e:
            print('Could not retrieve the data... Trying again.')

        loop +=1
        sleep(30)
    
    

    

