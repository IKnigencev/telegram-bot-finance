from aiogram import types

from settings.locales.ru import (
    HOW_ADD_DELETE,
    ABOUT_TEXT,
    INFO_TEXT
)
from controller.base_conroller import BaseController


class InfoController(BaseController):
    """Обработка команд связанных со статической информацией"""

    async def about(self) -> types.Message:
        await self.input_message.answer(ABOUT_TEXT, parse_mode="HTML")

    async def info(self) -> types.Message:
        await self.input_message.answer(INFO_TEXT, parse_mode="HTML")

    async def how_add_delete(self) -> types.Message:
        await self.input_message.answer(HOW_ADD_DELETE, parse_mode="HTML")
