from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text

from controller.balance_controller import BalanceController


async def cmd_balance(message: types.Message):
    await BalanceController(message).balance()


async def cmd_add_sum(message: types.Message):
    await BalanceController(message).add_sum()


async def cmd_delete_sum(message: types.Message):
    await BalanceController(message).delete_sum()


async def cmd_remove_action(message: types.Message):
    await BalanceController(message).remove_action()


def setup(dp: Dispatcher):
    dp.register_message_handler(
        cmd_balance, Text(equals="Баланс"))
    dp.register_message_handler(
        cmd_remove_action, Text(equals="Отменить последнее действие"))
    dp.register_message_handler(
        cmd_add_sum, Text(startswith="++"))
    dp.register_message_handler(
        cmd_delete_sum, Text(startswith="--"))
