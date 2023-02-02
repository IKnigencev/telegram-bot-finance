from models.models import User


class BaseController:
    """Базовый класс обработки событий"""
    def __init__(self, attr, define_user=None) -> None:
        self.input_message = attr
        if define_user:
            self.user = User.get_or_create(
                id_telegram=attr["from"]["id"],
                name=attr["from"]["first_name"],
                last_name=attr["from"]["last_name"]
            )
