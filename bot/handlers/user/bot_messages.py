from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot.misc import exchange, Exchange

router = Router()

@router.message(F.text, Exchange.amount)
async def amount_message(message: Message, state: FSMContext, bot: Bot):
    try:
        amount = float(message.text)
    except Exception as e:
        print(e)
        return
    await state.update_data(amount=amount)

    state_data = await state.get_data()
    first_currency, second_currency = state_data["currency_pair"].split("/")

    exchange_result = exchange(first_currency, second_currency, amount=amount)

    await message.delete()
    await bot.edit_message_text(chat_id=message.chat.id, message_id=state_data["msg_id"],
                                text=f"Currency pair <b>{first_currency}/{second_currency}</b> at the rate: <b>{exchange_result['exchange_rate']}</b>\n\n"
                                f"<b>{first_currency} to {second_currency} (amount {amount}): {exchange_result['converted_amount']}</b>",
                                parse_mode="HTML")
    await state.clear()
