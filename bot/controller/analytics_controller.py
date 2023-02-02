from aiogram import types

from controller.base_conroller import BaseController


class AnalyticsController(BaseController):
    """Обработка команд связанных с аналитикой"""

    async def expenses_month(self) -> types.Message:
        await self.input_message.answer(text="Расходы месяц")

    async def income_month(self) -> types.Message:
        await self.input_message.answer(text="Доходы месяц")

    async def average_expenses_day(self) -> types.Message:
        await self.input_message.answer(text="Средняя трата в день")

    async def average_expenses_month(self) -> types.Message:
        await self.input_message.answer(text="Средняя трата в месяц")
