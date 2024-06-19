from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from bot.keyboards import rendering_currency, rendering_currencies, amount_currency_kb
from bot.misc import exchange, Exchange

router = Router()

@router.callback_query(F.data == "close")
async def close_callback(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.message.delete()
    await state.clear()


@router.callback_query(F.data.startswith('currency_'))
async def currency_callback(callback_query: CallbackQuery, state: FSMContext):
    currency = callback_query.data.split("_")[1]
    await callback_query.message.edit_text(text="Select a currency pair:",
                                           reply_markup=await rendering_currencies(currency))
    await state.update_data(currency=currency)
    await state.update_data(msg_id=callback_query.message.message_id)
    await state.set_state(Exchange.currency_pair)

@router.callback_query(F.data == "back_to_select_currency")
async def back_to_select_currency_callback(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback_query.message.edit_text(text="Select the currency to exchange:",
                         reply_markup=await rendering_currency())


@router.callback_query(F.data == "back_to_select_currency_pair")
async def back_to_select_currency_pair_callback(callback_query: CallbackQuery, state: FSMContext):
    state_data = await state.get_data()
    currency = state_data["currency"]
    await callback_query.message.edit_text(text="Select a currency pair:",
                                           reply_markup=await rendering_currencies(currency))


@router.callback_query(F.data.startswith("c_pair-"), Exchange.currency_pair)
async def c_pair_callback(callback_query: CallbackQuery, state: FSMContext):
    currency_pair = callback_query.data.split("-")[1]

    await state.update_data(currency_pair=currency_pair)

    first_currency, second_currency = currency_pair.split("/")
    data = exchange(first_currency, second_currency)

    await callback_query.message.edit_text(text=f"Exchange rate {currency_pair}: {data['exchange_rate']}",
                                           reply_markup=amount_currency_kb)
    await state.set_state(Exchange.amount)


@router.callback_query(F.data.startswith("amount_"))
async def amount_callback(callback_query: CallbackQuery, state: FSMContext):
    amount = float(callback_query.data.split("_")[1])
    await state.update_data(amount=amount)

    state_data = await state.get_data()
    first_currency, second_currency = state_data["currency_pair"].split("/")

    exchange_result = exchange(first_currency, second_currency, amount=amount)

    await callback_query.message.edit_text(text=f"Currency pair <b>{first_currency}/{second_currency}</b> at the rate: <b>{exchange_result['exchange_rate']}</b>\n\n"
                                                f"<b>{first_currency} to {second_currency} (amount {amount}): {exchange_result['converted_amount']}</b>",
                                           parse_mode="HTML")
    await state.clear()

