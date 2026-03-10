import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message
from config import BOT_TOKEN


bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))

async def cmd_start(message: Message):
    await message.answer("Привет я твой первый бот")
    
@dp.message(Command("help"))

async def cmd_help(message: Message):
    await message.answer("Доступные команды: \n/start - начать\n/help - помощь")
    
@dp.message(F.text)

async def echo(message: Message):
    await message.answer(message.text)





    
async def main():
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())