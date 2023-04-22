"""Сервис обработки операций с балансом.

Класс предоставляет реализацию следующего функционала:
- Доходы;
- Расходы;
- Отмена последнего действия;
- Установка баланса;
- Получение баланса;
"""
from typing import Dict, Any
from decimal import Decimal

from models.models import BalanceModels, TransactionModels


class BalanceServices:
    """Сервис работы с балансом пользователя"""

    BALANCE_PREFIX: str = '=='
    ADD_PREFIX: str = '++'
    DELETE_PREFIX_EM_DASH: str = '—'
    DELETE_PREFIX_HYPHEN: str = '--'

    def __init__(self, user) -> None:
        self.user = user

    def add_sum(self, message) -> Dict[str, Decimal]:
        """Добавление введеной пользователем суммы"""

        sum_by_user = Decimal(self.__decimal_from_message(
            message['text'],
            self.ADD_PREFIX
        ))
        balance = self.get_balance()["balance"]
        self.__save_transaction('+', sum_by_user)
        result = balance + sum_by_user
        self.__update_balance(result)
        return self.__result_for_answer_add_delete(sum_by_user, result)

    def delete_sum(self, message) -> Dict[str, Decimal]:
        """Удаление введеной пользователем суммы"""

        sum_by_user = Decimal(self.__sum_of_delete_message(message['text']))
        balance = self.get_balance()["balance"]
        self.__save_transaction('-', sum_by_user)
        result = balance - sum_by_user
        self.__update_balance(result)
        return self.__result_for_answer_add_delete(sum_by_user, result)

    def remove_action(self) -> Dict[str, Any]:
        """Отмена последнего действия"""

        balance = self.user[0].balance.get()
        transactions = [
            transaction for transaction in balance.transactions.select()
        ]
        sum_transaction = transactions[-1].sum_transaction
        type_transaction = transactions[-1].type_transaction
        result = self.__delete_last_action(transactions[-1])
        transactions[-1].delete_instance()
        return self.__result_for_remove(
            type_transaction,
            sum_transaction,
            result
        )

    def set_balance(self, message) -> Dict[str, Decimal]:
        """Установка баланса юзеру"""

        sum_by_user = self.__decimal_from_message(
            message['text'],
            self.BALANCE_PREFIX
        )
        self.__update_balance(sum_by_user)
        return {"balance": sum_by_user}

    def get_balance(self) -> Dict[str, Decimal]:
        """Вывод баланса юзера"""

        balance = BalanceModels.get_or_create(user=self.user[0])
        return {"balance": balance[0].money}

    def __decimal_from_message(self, text, prefix) -> Decimal:
        str_sum = text.replace(prefix, '').strip().replace(',', '.')
        return Decimal(str_sum)

    def __sum_of_delete_message(self, text) -> Decimal:
        if self.DELETE_PREFIX_HYPHEN in text:
            sum_by_user = self.__decimal_from_message(
                text,
                self.DELETE_PREFIX_HYPHEN
            )
        else:
            sum_by_user = self.__decimal_from_message(
                text,
                self.DELETE_PREFIX_EM_DASH
            )
        return sum_by_user

    def __save_transaction(self, type: str, sum: Decimal) -> None:
        TransactionModels.create(
            balance=self.user[0].balance,
            type_transaction=type,
            sum_transaction=sum
        )

    def __delete_last_action(self, transaction) -> Decimal:
        balance = self.get_balance()['balance']
        if transaction.type_transaction == '-':
            last_action = balance + transaction.sum_transaction
        else:
            last_action = balance - transaction.sum_transaction
        self.__update_balance(last_action)
        return last_action

    def __update_balance(self, sum_by_user) -> None:
        BalanceModels.update(
            money=sum_by_user
        ).where(
            BalanceModels.user == self.user[0]
        ).execute()

    def __result_for_answer_add_delete(
            self,
            add: Decimal,
            balance: Decimal) -> Dict[str, Decimal]:
        return {
            "add": add,
            "balance": balance
        }

    def __result_for_remove(
            self,
            type: str,
            last_action: Decimal,
            balance: Decimal) -> Dict[str, Any]:
        type = ("Доходов", "Расходов")[bool(type == "-")]
        return {
            "type": type,
            "last_action": last_action,
            "balance": balance
        }
