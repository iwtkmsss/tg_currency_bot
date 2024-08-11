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
