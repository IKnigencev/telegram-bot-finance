from aiogram import types, Dispatcher, Bot
from aiogram.dispatcher.filters import Text

from controller.analytics_controller import AnalyticsController


async def cmd_analytics(message: types.Message):
    await AnalyticsController(message).analytics()


async def cmd_response_analytics_buttons(callback_query: types.CallbackQuery):
    await AnalyticsController(
        callback_query,
        define_user=True
    ).response_analytics_buttons(BOT)


def setup(dp: Dispatcher, bot: Bot):
    global BOT
    BOT = bot

    dp.register_message_handler(
        cmd_analytics,
        Text(equals="Аналитика")
    )
    dp.register_callback_query_handler(
        cmd_response_analytics_buttons,
        lambda c: c.data and c.data.startswith('btn')
    )
