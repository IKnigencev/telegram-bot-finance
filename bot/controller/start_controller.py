from aiogram import types
# from aiogram.types import message

from settings.locales.ru import START_TEXT, HELP_TEXT
from controller.base_conroller import BaseController
# from settings.settings import logging


class StartController(BaseController):
    """Обработка базовых команд"""

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.data_user = {"name": self.input_message["from"]["first_name"]}

    async def start(self) -> types.Message:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = [
            "Баланс",
            "Аналитика",
            "Как добавлять расходы/доходы",
            "Информация",
            "Об авторе",
            "Отменить"
        ]
        keyboard.add(*buttons)
        text_message = START_TEXT.substitute(**self.data_user)
        await self.input_message.answer(text_message, reply_markup=keyboard)

    async def help(self) -> types.Message:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Назад", "Об авторе", "Оставить отзыв"]
        keyboard.add(*buttons)
        await self.input_message.answer(
            HELP_TEXT,
            reply_markup=keyboard
        )
