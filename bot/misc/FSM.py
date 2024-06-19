from aiogram.fsm.state import StatesGroup, State


class Exchange(StatesGroup):
    msg_id = State()

    currency = State()
    currency_pair = State()
    amount = State()
