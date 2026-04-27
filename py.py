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
    await message.answer("Я створений на Python з бібліотекою Aiogram учнем 10-А класу")

@dp.message(Command("menu"))
async def show_menu(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Привіт 👋"), KeyboardButton(text="Як справи? 😊")],
            [KeyboardButton(text="Анекдот 🤣")]
        ],
        resize_keyboard=True
    )
    await message.answer("Вибери опцію:", reply_markup=keyboard)

# Обробка натискань
@dp.message(F.text==)
async def handle_message(message: Message):
    text = message.text
    if text == "Привіт 👋":
        await message.answer("Привіт-привіт! 👋")
    elif text == "Як справи? 😊":
        await message.answer("Усе чудово! А в тебе?")
    elif text == "Анекдот 🤣":
        await message.answer("Як називається кіт-програміст? — JavaMeow!")
    else:
        await message.answer("Натисни одну з кнопок 😺")

async def main():
    print("Бот запущений...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
# Налаштування клавіатури
def main_menu():
    builder = ReplyKeyboardBuilder()
    builder.button(text="Як називається кіт-програміст? — JavaMeow!")
    builder.button(text="Як справи? 😊 ")
    builder.button(text="Інтернет – така зараза, гірше сємочок в три раза!😏")
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)