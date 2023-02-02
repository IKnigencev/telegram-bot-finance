from aiogram import types

from settings.locales.ru import (
    MENU_TEXT,
    HOW_ADD_DELETE,
    ANALYTICS_TEXT,
    ABOUT_TEXT,
    INFO_TEXT
)
from controller.base_conroller import BaseController


class InfoController(BaseController):
    """Обработка команд связанных со статической информацией"""

    async def menu(self) -> types.Message:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [
            "Баланс",
            "Все об аналитике",
            "Как добавлять расходы/доходы",
            "Информация",
            "Об авторе"
        ]
        keyboard.add(*buttons)
        await self.input_message.answer(MENU_TEXT, reply_markup=keyboard)

    async def about(self) -> types.Message:
        await self.input_message.answer(ABOUT_TEXT)

    async def info(self) -> types.Message:
        await self.input_message.answer(INFO_TEXT)

    async def how_add_delete(self) -> types.Message:
        await self.input_message.answer(HOW_ADD_DELETE)

    async def how_about_analystics(self) -> types.Message:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [
            "Расходы месяц",
            "Доходы месяц",
            "Средняя трата в день",
            "Средняя трата в месяц"
        ]
        keyboard.add(*buttons)
        await self.input_message.answer(ANALYTICS_TEXT, reply_markup=keyboard)
