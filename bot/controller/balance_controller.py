from aiogram import types

from controller.base_conroller import BaseController
from services.balance_services import BalanceServices


class BalanceController(BaseController):
    """Обработка команд связанных с балансом"""
    async def balance(self) -> types.Message:
        keyboard = types.InlineKeyboardMarkup()
        buttons = [
            types.InlineKeyboardButton(
                "Расходы месяц",
                callback_data="balance1"
            ),
            types.InlineKeyboardButton(
                "Доходы месяц",
                callback_data="balance2"
            ),
            types.InlineKeyboardButton(
                "Средняя трата в день",
                callback_data="balance3"
            ),
            types.InlineKeyboardButton(
                "Средняя трата в месяц",
                callback_data="balance4"
            )
        ]
        keyboard.add(*buttons)
        await self.input_message.reply(
            "TEST",
            reply_markup=keyboard,
            parse_mode="HTML"
        )

    async def add_sum(self) -> types.Message:
        await self.input_message.answer(text="Плюс")

    async def delete_sum(self) -> types.Message:
        await self.input_message.answer(text="Минус")

    async def remove_action(self) -> types.Message:
        await self.input_message.answer(text="Отмена")

    async def balance_buttons(self, bot) -> types.Message:
        text_balance = BalanceServices(self.input_message).get_balance()
        await bot.send_message(
            self.input_message.from_user.id,
            text=text_balance
        )
