from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from controller.info_controller import InfoController


async def cmd_info(message: types.Message):
    await InfoController(message).info()


async def cmd_about(message: types.Message):
    await InfoController(message).about()


def setup(dp: Dispatcher):
    dp.register_message_handler(cmd_info, Text(equals="Информация"))
    dp.register_message_handler(cmd_about, Text(equals="Об авторе"))
