from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from controller.balance_controller import BalanceController


async def cmd_balance(message: types.Message):
    await BalanceController(message, define_user=True).balance()


async def cmd_set_balance(message: types.Message):
    await BalanceController(message, define_user=True).set_balance()


async def cmd_add_sum(message: types.Message):
    await BalanceController(message, define_user=True).add_sum()


async def cmd_delete_sum_hypen(message: types.Message):
    await BalanceController(message, define_user=True).delete_sum()


async def cmd_delete_sum_em_dash(message: types.Message):
    await BalanceController(message, define_user=True).delete_sum()


async def cmd_remove_action(message: types.Message):
    await BalanceController(message, define_user=True).remove_action()


def setup(dp: Dispatcher):
    dp.register_message_handler(
        cmd_balance,
        Text(equals="Баланс")
    )
    dp.register_message_handler(
        cmd_remove_action,
        Text(equals="Отменить")
    )
    dp.register_message_handler(
        cmd_add_sum,
        Text(startswith="++")
    )
    dp.register_message_handler(
        cmd_delete_sum_hypen,
        Text(startswith="—")
    )
    dp.register_message_handler(
        cmd_delete_sum_em_dash,
        Text(startswith="--")
    )
    dp.register_message_handler(
        cmd_set_balance,
        Text(startswith="==")
    )
