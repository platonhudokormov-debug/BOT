import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart

# Сюди вставляємо свій токен з BotFather
API_TOKEN = "8707422337:AAHPEwq-knwmxI_b3vjBAVbmZh461t1L0q0"

# Створюємо бота і диспетчер
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обробник команди /start
@dp.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привіт! Я твій перший бот!😉 ")

# Головна функція для запуску бота
async def main():
    await dp.start_polling(bot)

# Запускаємо
if __name__ == "__main__":
    asyncio.run(main())




    @dp.message(Command("help"))
    async def help_command(message: Message):
        await message.answer("Ось що я вмію:\n/start - привітання\n/help - довідка\n/about - про мене")


    # Обробник команди /about
    @dp.message(Command("about"))
    async def about_command(message: Message):
        await message.answer("Я створений на Python з бібліотекою Aiogram!")


    # Запуск
    async def main():
        await dp.start_polling(bot)


    if __name__ == "__main__":
        asyncio.run(main())
