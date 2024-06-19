import sys
import logging
import asyncio

from aiogram import Bot, Dispatcher

from handlers.user import bot_callback, bot_messages, user_commands
from bot.misc import TOKEN


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        bot_callback.router,
        user_commands.router,
        bot_messages.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("[-] BOT HAS BEEN DISABLE")
