<<<<<<< HEAD
import requests
from bs4 import BeautifulSoup

from .config import HEADERS


def exchange(currency, to_currency, amount=None):
    url = f"https://www.google.com/search?q={currency}+to+{to_currency}"

    s = requests.Session()
    response = s.get(url=url, headers=HEADERS)

    if response.status_code != 200:
        print("Request error...")
        return None

    soup = BeautifulSoup(response.text, "lxml")

    exchange_rate = float(soup.find('span', class_="DFlfde SwHCTb").text.replace(",", "."))
    converted_amount = (amount * exchange_rate) if amount else 0

    return_data = {
        "converted_amount": round(converted_amount, 2),
        "exchange_rate": exchange_rate
    }

    return return_data
=======
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
>>>>>>> c6436386028f43ce6d1255261173ccc30a7ab61b
