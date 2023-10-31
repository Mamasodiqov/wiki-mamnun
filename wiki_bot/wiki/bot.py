import asyncio
import logging
import sys
from os import getenv
import wikipedia

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

wikipedia.set_lang('uz')
# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6609073912:AAFxPf7I7bCyQzuJvYu6I_gEhfGsMD3qoLQ"

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Assalomu alaykum, {hbold(message.from_user.full_name)} \nwikibot ga xush kelibsiz!")


@dp.message()
async def sendWiki(message: types.Message) -> None:
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Bu mavzuga oid maqola topilmadi!")
    
        

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())