from aiogram import types
from aiogram import Bot

from controller.base_conroller import BaseController
from services.analytics_services import AnalyticsServices
from settings.locales.ru import ANALYTICS_TEXT


class AnalyticsController(BaseController):
    """Обработка команд связанных с аналитикой"""

    async def analytics(self) -> types.Message:
        keyboard = types.InlineKeyboardMarkup()
        buttons = [
            types.InlineKeyboardButton(
                "Расходы месяц",
                callback_data="btn1"
            ),
            types.InlineKeyboardButton(
                "Доходы месяц",
                callback_data="btn2"
            ),
            types.InlineKeyboardButton(
                "Средняя трата в день",
                callback_data="btn3"
            ),
            types.InlineKeyboardButton(
                "Средняя трата в месяц",
                callback_data="btn4"
            )
        ]
        keyboard.add(*buttons)
        await self.input_message.reply(
            ANALYTICS_TEXT,
            reply_markup=keyboard,
            parse_mode="HTML"
        )

    async def response_analytics_buttons(self, bot: Bot) -> types.Message:
        text_analytics = AnalyticsServices(self.input_message).get_analytics()
        await bot.send_message(
            self.input_message.from_user.id,
            text=text_analytics
        )
