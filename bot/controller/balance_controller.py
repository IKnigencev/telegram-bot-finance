from aiogram import types

from controller.base_conroller import BaseController


class BalanceController(BaseController):
    """Обработка команд связанных с балансом"""
    async def balance(self) -> types.Message:
        await self.input_message.answer(text="Баланс")

    async def add_sum(self) -> types.Message:
        await self.input_message.answer(text="Плюс")

    async def delete_sum(self) -> types.Message:
        await self.input_message.answer(text="Минус")

    async def remove_action(self) -> types.Message:
        await self.input_message.answer(text="Отмена")
