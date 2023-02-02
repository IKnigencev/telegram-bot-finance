from aiogram import types
from aiogram import Dispatcher
from aiogram.dispatcher.filters import Text


async def cmd_expenses_month(message: types.Message):
    await message.answer(text="Расходы месяц")


async def cmd_income_month(message: types.Message):
    await message.answer(text="Доходы месяц")


async def cmd_average_expenses_day(message: types.Message):
    await message.answer(text="Средняя трата в день")


async def cmd_average_expenses_month(message: types.Message):
    await message.answer(text="Средняя трата в месяц")



def setup(dp: Dispatcher):
    dp.register_message_handler(cmd_expenses_month, Text(equals="Расходы месяц"))
    dp.register_message_handler(cmd_income_month, Text(equals="Доходы месяц"))
    dp.register_message_handler(cmd_average_expenses_day, Text(equals="Средняя трата в день"))
    dp.register_message_handler(cmd_average_expenses_month, Text(equals="Средняя трата в месяц"))

