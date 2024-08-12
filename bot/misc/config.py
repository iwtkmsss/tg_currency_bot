from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv('TOKEN')
<<<<<<< HEAD

CURRENCY = {"USD": "$",
=======
ExchangeRate_API_KEY = os.getenv('ExchangeRate_API_KEY') # https://www.exchangerate-api.com/

currency = {"USD": "$",
>>>>>>> c6436386028f43ce6d1255261173ccc30a7ab61b
            "EUR": "€",
            "UAH": "₴",
            "JPY": "¥",
            "GBP": "£",
            "PLN": "zł"}

<<<<<<< HEAD
HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
=======
ExchangeRate_url = "https://v6.exchangerate-api.com/v6/{}/latest/".format(ExchangeRate_API_KEY)
>>>>>>> c6436386028f43ce6d1255261173ccc30a7ab61b
