from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards import rendering_currency

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text="Select the currency to exchange:",
                         reply_markup=await rendering_currency())
