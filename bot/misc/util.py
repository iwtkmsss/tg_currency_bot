import requests

from .config import ExchangeRate_url


def exchange(currency, to_currency, amount=None):
    url = ExchangeRate_url + currency
    response = requests.get(url=url)
    data = response.json()

    if response.status_code != 200:
        print("Request error API")
        return None

    exchange_rate = data['conversion_rates'][to_currency]
    converted_amount = (amount * exchange_rate) if amount else 0

    return_data = {
        "converted_amount": round(converted_amount, 2),
        "exchange_rate": exchange_rate
    }

    return return_data
