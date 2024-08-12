<<<<<<< HEAD
from aiogram.fsm.state import StatesGroup, State


class Exchange(StatesGroup):
    msg_id = State()

    currency = State()
    currency_pair = State()
    amount = State()
=======
from aiogram.fsm.state import StatesGroup, State


class Exchange(StatesGroup):
    msg_id = State()

    currency = State()
    currency_pair = State()
    amount = State()
>>>>>>> c6436386028f43ce6d1255261173ccc30a7ab61b
