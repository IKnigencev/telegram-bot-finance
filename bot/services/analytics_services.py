import datetime
from decimal import Decimal

from settings.settings import logging
from settings.locales.ru import UNKNOWN_BTN
from models.models import TransactionModels


class AnalyticsServices:
    """Сервис обработки запросов на аналитику"""
    MONTH_DAYS = 30

    def __init__(self, attr, user=None) -> None:
        self.input_data = attr
        if user:
            self.user = user

    def get_analytics(self) -> str:
        func = self.__button_definition(self.input_data.data)
        data_from_func = getattr(self, func)()
        return data_from_func

    def _expenses_per_month(self) -> Decimal:
        return self.__get_sum_on_month('-')

    def _income_month(self) -> Decimal:
        return self.__get_sum_on_month('+')

    def _average_spending_per_day_month(self) -> Decimal:
        sum = self.__get_sum_on_month('-')
        return sum / self.MONTH_DAYS

    def _average_income_per_day_month(self) -> Decimal:
        sum = self.__get_sum_on_month('+')
        return sum / self.MONTH_DAYS

    def _unknown_button(self) -> str:
        return UNKNOWN_BTN

    def __button_definition(self, text) -> str:
        text = text.replace('btn', '').strip()
        if text == "_expenses_per_month":
            return "_expenses_per_month"
        elif text == "_income_month":
            return "_income_month"
        elif text == "_average_spending_per_day_month":
            return "_average_spending_per_day_month"
        elif text == "_average_income_per_day_month":
            return "_average_income_per_day_month"
        else:
            return "_unknown_button"

    def __get_sum_on_month(self, type_transaction: str) -> Decimal:
        balance = self.user.balance.get()
        start_date, end_date = self.__is_transaction_appropriate()
        transactions = balance.transactions.where(
            (TransactionModels.type_transaction == type_transaction)
            & (TransactionModels.created.between(start_date, end_date))
        )
        result = 0
        for transaction in transactions.select():
            result += transaction.sum_transaction
        return result

    def __is_transaction_appropriate(self):
        today = datetime.datetime.now()
        diff = today - datetime.timedelta(30)
        end_date = diff
        return today, end_date
