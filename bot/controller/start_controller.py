from string import Template

from aiogram import types
# from aiogram.types import message

from controller.base_conroller import BaseController
from models.models import User
# from settings.settings import logging


class StartController(BaseController):
    STANDART_TEMPLATE = Template(
        "Привет, $name!\n\nЯ здесь,"
        + " чтобы помочь тебе следить за твоими расходами и доходами"
    )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.data_user = {"name": self.input_message["from"]["first_name"]}

    async def start(self) -> types.Message:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Меню", "Информация", "Об авторе"]
        keyboard.add(*buttons)
        text_message = self.STANDART_TEMPLATE.substitute(**self.data_user)
        await self.input_message.answer(text_message, reply_markup=keyboard)
    
    async def help(self) -> types.Message:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Назад", "Об авторе", "Оставить отзыв"]
        keyboard.add(*buttons)
        await self.input_message.answer(
            "Этот бот предназначен для анализа расходов и доходов",
            reply_markup=keyboard
        )
