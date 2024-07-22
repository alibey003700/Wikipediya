import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from vikipediya import malumot


TOKEN = "6068900832:AAESMuQLAP5P1KlLAcjcTndF5d2qt4eSa7E"

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    full_name = message.from_user.full_name
    text = f"Salom {full_name}, Wikipediya botga hush kelibsiz"
    await message.answer(text)

@dp.message(F.text)
async def wiki_malumot(message: Message):
    text = message.text
    natija = malumot(text)
    await message.answer(natija)

async def main():
    global bot
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
