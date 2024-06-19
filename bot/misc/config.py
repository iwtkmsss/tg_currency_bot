from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
ExchangeRate_API_KEY = os.getenv('ExchangeRate_API_KEY') # https://www.exchangerate-api.com/

currency = {"USD": "$",
            "EUR": "€",
            "UAH": "₴",
            "JPY": "¥",
            "GBP": "£",
            "PLN": "zł"}

ExchangeRate_url = "https://v6.exchangerate-api.com/v6/{}/latest/".format(ExchangeRate_API_KEY)
