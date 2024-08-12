<<<<<<< HEAD
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards import rendering_currency

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text="Select the currency to exchange:",
                         reply_markup=await rendering_currency())
=======
from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from bot.keyboards import rendering_currency

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text="Select the currency to exchange:",
                         reply_markup=await rendering_currency())
>>>>>>> c6436386028f43ce6d1255261173ccc30a7ab61b
