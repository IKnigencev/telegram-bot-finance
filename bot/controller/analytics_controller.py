from aiogram import types
from aiogram import Bot

from controller.base_conroller import BaseController
from services.analytics_services import AnalyticsServices
from settings.locales.ru import ANALYTICS_TEXT
from settings.settings import logging


class AnalyticsController(BaseController):
    """Обработка команд связанных с аналитикой"""

    async def analytics(self) -> types.Message:
        keyboard = types.InlineKeyboardMarkup()
        buttons = [
            types.InlineKeyboardButton(
                "Расходы месяц",
                callback_data="btn_expenses_per_month"
            ),
            types.InlineKeyboardButton(
                "Доходы месяц",
                callback_data="btn_income_month"
            ),
            types.InlineKeyboardButton(
                "Средняя трата в день",
                callback_data="btn_average_spending_per_day"
            ),
            types.InlineKeyboardButton(
                "Средняя трата в месяц",
                callback_data="btn_average_spending_per_month"
            )
        ]
        keyboard.add(*buttons)
        await self.input_message.reply(
            ANALYTICS_TEXT,
            reply_markup=keyboard,
            parse_mode="HTML"
        )

    async def response_analytics_buttons(self, bot: Bot) -> types.Message:
        text_analytics = AnalyticsServices(
            self.input_message,
            user=self.user[0]
        ).get_analytics()
        await bot.send_message(
            self.input_message.from_user.id,
            text=text_analytics
        )
