import pytest

from aiogram import types
from bot.controller.start_controller import StartController


USER = {
    "id": 12345678,
    "is_bot": False,
    "first_name": "FirstName",
    "last_name": "LastName",
    "username": "username",
    "language_code": "ru"
}

CHAT = {
    "id": 12345678,
    "first_name": "FirstName",
    "last_name": "LastName",
    "username": "username",
    "type": "private"
}

MESSAGE = {
    "message_id": 11223,
    "from": USER,
    "chat": CHAT,
    "date": 1508709711,
    "text": "Hi, world!"
}


class TestHandler:

    @pytest.mark.asyncio
    async def test_start(self):
        message = types.Message(**MESSAGE)
        answer_message = await StartController(message).start()
        assert answer_message == "Hello, Bot!", (
            "Ошибка при обработке команды"
        )
