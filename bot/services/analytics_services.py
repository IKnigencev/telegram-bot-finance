import datetime

from settings.settings import logging
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
        logging.info("get_analytics(self)")
        data_from_func = getattr(self, func)()
        return data_from_func

    def _expenses_per_month(self):
        return self.__get_sum_on_month('-')

    def _income_month(self):
        return self.__get_sum_on_month('+')

    def _average_spending_per_day(self):
        return "_average_spending_per_day"

    def _average_spending_per_month(self):
        return "_average_spending_per_month"

    def _unknown_button(self):
        return "_unknown_button"

    def __button_definition(self, text) -> str:
        text = text.replace('btn', '').strip()
        if text == "_expenses_per_month":
            return "_expenses_per_month"
        elif text == "_income_month":
            return "_income_month"
        elif text == "_average_spending_per_day":
            return "_average_spending_per_day"
        elif text == "_average_spending_per_month":
            return "_average_spending_per_month"
        else:
            return "_unknown_button"

    def __get_sum_on_month(self, type_transaction: str):
        balance = self.user.balance.get()
        start_date, end_date = self.__is_transaction_appropriate()
        transactions = balance.transactions.where(
            (TransactionModels.type_transaction == type_transaction)
            & (TransactionModels.created.between(start_date, end_date))
        )
        logging.info([tran for tran in balance.transactions.select().dicts()])
        logging.info(len(transactions))
        result = 0
        for transaction in transactions.select():
            result += transaction.sum_transaction
            logging.info(transaction)
            logging.info(transaction.type_transaction)
        return result

    def __is_transaction_appropriate(self):
        today = datetime.datetime.now()
        diff = today - datetime.timedelta(30)
        end_date = diff
        logging.info()
        return today, end_date
