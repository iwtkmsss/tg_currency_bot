from aiogram.utils.keyboard import (InlineKeyboardButton,
                                    InlineKeyboardMarkup,
                                    InlineKeyboardBuilder)

from bot.misc import CURRENCY


async def rendering_currency():
    keyboard = InlineKeyboardBuilder()
    for c in CURRENCY.keys():
        keyboard.row(InlineKeyboardButton(text=c, callback_data=f"currency_{c}"))
    keyboard.row(InlineKeyboardButton(text="Close ❌", callback_data="close"))
    return keyboard.as_markup()


async def rendering_currencies(curr):
    keyboard = InlineKeyboardBuilder()
    for c in CURRENCY.keys():
        if c == curr:
            continue
        keyboard.row(InlineKeyboardButton(text=f"{curr}/{c}", callback_data=f"c_pair-{curr}/{c}"))
    keyboard.row(InlineKeyboardButton(text="Back 🔙", callback_data="back_to_select_currency"))
    return keyboard.as_markup()


amount_currency_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="10", callback_data="amount_10")
        ],
        [
            InlineKeyboardButton(text="50", callback_data="amount_50")
        ],
        [
            InlineKeyboardButton(text="100", callback_data="amount_100")
        ],
        [
            InlineKeyboardButton(text="200", callback_data="amount_200")
        ],
        [
            InlineKeyboardButton(text="500", callback_data="amount_500")
        ],
        [
            InlineKeyboardButton(text="Back 🔙", callback_data="back_to_select_currency_pair")
        ]
    ]
)
