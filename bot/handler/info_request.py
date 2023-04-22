from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from controller.info_controller import InfoController


async def cmd_info(message: types.Message):
    await InfoController(message).info()


async def cmd_about(message: types.Message):
    await InfoController(message).about()


async def cmd_how_add_delete(message: types.Message):
    await InfoController(message).how_add_delete()


def setup(dp: Dispatcher):
    dp.register_message_handler(
        cmd_how_add_delete, Text(equals="Как добавлять расходы/доходы")
    )
    dp.register_message_handler(
        cmd_info, Text(equals="Информация")
    )
    dp.register_message_handler(
        cmd_about, Text(equals="Об авторе")
    )
