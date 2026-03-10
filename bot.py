import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from config import BOT_TOKEN


bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="О боте"), KeyboardButton(text="Помошь")], [KeyboardButton(text="Пока")]
    ],
    resize_keyboard=True
)


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Привет я твой первый бот", reply_markup=main_kb)
    

@dp.message(F.text == "О боте")
async def about(message: Message):
    await message.answer("Я учебный бот")


@dp.message(F.text == "Помошь")
async def help(message: Message):
    await message.answer("Доступные команды: \n/start - начать\n/help - помощь")

    
@dp.message(F.text == "Пока")
async def bay(message: Message):
    await message.answer("До свидания!")

    
@dp.message(F.text)
async def echo(message: Message):
    await message.answer(message.text)









    
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())