from string import Template

from aiogram import types
# from aiogram.types import message

from models.models import User
# from settings.settings import logging


class StartController:
    STANDART_TEMPLATE = Template(
        "Привет, $name!\n\nЯ здесь,"
        + " чтобы помочь тебе следить за твоими расходами и доходами"
    )

    def __init__(self, input_message, define_user=None) -> None:
        self.input_message = input_message
        self.data_user = {"name": input_message["from"]["first_name"]}
        if define_user:
            self.user = User.get_or_create(
                id_telegram=input_message["from"]["id"],
                name=input_message["from"]["first_name"],
                last_name=input_message["from"]["last_name"]
            )

    async def start(self) -> types.Message:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Информация", "Об авторе"]
        keyboard.add(*buttons)
        text_message = self.STANDART_TEMPLATE.substitute(**self.data_user)
        await self.input_message.answer(text_message, reply_markup=keyboard)

    async def info(self) -> types.Message:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Назад", "Об авторе", "Оставить отзыв"]
        keyboard.add(*buttons)
        await self.input_message.answer(
            "Этот бот предназначен для анализа расходов и доходов",
            reply_markup=keyboard
        )

    async def about_author(self) -> types.Message:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Назад", "Об авторе", "Оставить отзыв"]
        keyboard.add(*buttons)
        await self.input_message.answer(
            "Этот бот предназначен для анализа расходов и доходов",
            reply_markup=keyboard
        )
