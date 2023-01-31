import asyncio
from aiogram import Bot, Dispatcher, types

from settings.settings import TOKEN_BOT


bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):

    await message.answer("Hello!")


async def main():
    await dp.start_polling(bot)


def start_polling():
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())
