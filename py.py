import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

API_TOKEN = "8707422337:AAHPEwq-knwmxI_b3vjBAVbmZh461t1L0q0"

bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привіт! Я твій перший бот!😉")

# /help
@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "Ось що я вмію:\n"
        "/start - привітання\n"
        "/help - довідка\n"
        "/about - про мене"
    )

# /about
@dp.message(Command("about"))
async def about_command(message: Message):
    await message.answer("Я створений на Python з бібліотекою Aiogram!")

# запуск
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())