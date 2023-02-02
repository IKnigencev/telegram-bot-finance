from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text


async def cmd_menu(message: types.Message):
    await message.answer(text="Меню")


async def cmd_info(message: types.Message):
    await message.answer(text="Инфа")


async def cmd_about(message: types.Message):
    await message.answer(text="Об авторе")


def setup(dp: Dispatcher):
    dp.register_message_handler(cmd_menu, Text(equals="Меню"))
    dp.register_message_handler(cmd_info, Text(equals="Информация"))
    dp.register_message_handler(cmd_about, Text(equals="Об авторе"))
