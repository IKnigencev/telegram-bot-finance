from aiogram import types

from decimal import InvalidOperation

from settings.settings import logging
from controller.base_conroller import BaseController
from services.balance_services import BalanceServices
from settings.locales.ru import (
    BALANCE_TEXT,
    ADD_TEXT,
    SET_BAlANCE_TEXT,
    DELETE_TEXT,
    REMOVE_ACTION
)


class BalanceController(BaseController):
    """Обработка команд связанных с балансом"""
    async def balance(self) -> types.Message:
        update_balance = BalanceServices(self.user).get_balance()
        await self.input_message.answer(
            BALANCE_TEXT.substitute(**update_balance),
            parse_mode="HTML"
        )

    async def set_balance(self) -> types.Message:
        try:
            update_balance = BalanceServices(self.user).set_balance(
                self.input_message
            )
            await self.input_message.answer(
                SET_BAlANCE_TEXT.substitute(**update_balance)
            )
        except InvalidOperation:
            await self.input_message.answer(
                ("Ошибка в формате ввода,"
                 + "после '==' должно быть число")
            )
        except Exception as e:
            logging.error(e)
            await self.input_message.answer(
                "Неизвестная ошбика"
            )

    async def add_sum(self) -> types.Message:
        try:
            update_balance = BalanceServices(self.user).add_sum(
                self.input_message
            )
            await self.input_message.answer(
                ADD_TEXT.substitute(**update_balance)
            )
        except InvalidOperation:
            await self.input_message.answer(
                ("Ошибка в формате ввода,"
                 + "после '++' должно быть число")
            )

    async def delete_sum(self) -> types.Message:
        try:
            update_balance = BalanceServices(self.user).delete_sum(
                self.input_message
            )
            await self.input_message.answer(
                DELETE_TEXT.substitute(**update_balance)
            )
        except InvalidOperation:
            await self.input_message.answer(
                ("Ошибка в формате ввода,"
                 + "после '--' должно быть число")
            )

    async def remove_action(self) -> types.Message:
        try:
            update_balance = BalanceServices(self.user).remove_action()
            await self.input_message.answer(
                REMOVE_ACTION.substitute(**update_balance)
            )
        except IndexError:
            await self.input_message.answer(
                "Нет последних операций"
            )
