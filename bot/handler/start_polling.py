import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Text

from settings.settings import TOKEN_BOT, logging

from controller.start_controller import StartController


bot = Bot(token=TOKEN_BOT)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def cmd_start(message: types.Message):
    await StartController(message, define_user=True).start()


@dp.message_handler(Text(equals="Информация"))
async def cmd_info(message: types.Message):
    await StartController(message).info()


@dp.message_handler(Text(equals="Об авторе"))
async def cmd_about(message: types.Message):
    logging.info(message.text)
    await StartController(message).about_author()


async def main():
    await dp.start_polling(bot)


def start_polling():
    asyncio.run(main())


if __name__ == "__main__":
    asyncio.run(main())
