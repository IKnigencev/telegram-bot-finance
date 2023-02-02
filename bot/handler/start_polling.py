import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text

from settings.settings import TOKEN_BOT
from controller.start_controller import StartController
from handler import (
    info_request,
    balance_request,
    analystics_request
)


bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await StartController(message, define_user=True).start()


@dp.message_handler(commands=["help"])
async def cmd_help(message: types.Message):
    await StartController(message).help()


@dp.message_handler(Text(equals="Удалить все свои данные"))
async def cmd_delete_user(message: types.Message):
    await StartController(message).help()


async def main():
    info_request.setup(dp)
    balance_request.setup(dp)
    analystics_request.setup(dp)
    await dp.start_polling(bot)


def start_polling():
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())
