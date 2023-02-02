from aiogram import types

from controller.base_conroller import BaseController


class InfoController(BaseController):
    async def menu(self) -> types.Message:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Баланс", "Все об аналитике", "Как добавлять расходы/доходы", "Информация", "Об авторе"]
        keyboard.add(*buttons)
        await self.input_message.answer('Меню:', reply_markup=keyboard)

    async def how_add_delete(self) -> types.Message:
        await self.input_message.answer('Ваше сообщение должно начинаться с "++" или "--"')

    async def how_about_analystics(self) -> types.Message:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        buttons = ["Расходы месяц", "Доходы месяц", "Средняя трата в день", "Средняя трата в месяц"]
        keyboard.add(*buttons)
        await self.input_message.answer('Какая аналитика доступна:', reply_markup=keyboard)
