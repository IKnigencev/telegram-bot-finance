from string import Template


START_TEXT = Template(
    "Привет, $name!\n\nЯ здесь,"
    + " чтобы помочь тебе следить за твоими расходами и доходами"
)

BALANCE_TEXT = Template(
    "<b>Ваш баланс:</b> $balance\n\n"
)

ADD_TEXT = Template(
    "Внесен доход $add\n"
    + "ваш баланс равен: $balance"
)

DELETE_TEXT = Template(
    "Внесен расход $add\n"
    + "ваш баланс равен: $balance"
)

REMOVE_ACTION = Template(
    "Отменено последнее действие $type\n"
    + "на сумму $last_action\n\n"
    + "Ваш баланс: $balance"
)

SET_BAlANCE_TEXT = Template(
    "Установлен баланс $balance"
)

HELP_TEXT = (
    "<b>Этот бот предназначен для анализа расходов и доходов.</b>\n\n"
    + "Чтобы узнать как взаимодействовать с ботом введите"
    + " <code>Информация</code>\n\n"
    + "Доступные команды:\n"
    + "- <code>Информация</code>"
    + "- <code>Информация</code>"
)

INFO_TEXT = (
    "<b>Бот для учета расходов/доходов</b>,"
    + " \nпо умолчанию у вас баланс 0 руб.\n\n"
    + "- Чтобы установить баланс введите <code>== 1000000</code>, "
    + "чтобы установить баланс 5000 руб;\n\n"
    + "- Введите <code>++ 10000</code>, чтобы добавить 1000;\n\n"
    + "- Введите <code>-- 1000</code>, чтобы удалить 1000;"
)

ABOUT_TEXT = (
    "Разработкой и поддержкой этого бота занимается \n"
    + "Иван Книженцев @IKnigencev \n\n"
    + "исходный код расположен здесь: "
    + "<a href='https://github.com/IKnigencev/telegram-bot-finance'>"
    + "GitHub</a>\n\n"
    + "P.S. Можете поставить звездочку"
)

ANALYTICS_TEXT = (
    "<b>Аналитика представлена след. функционалом:</b>\n\n"
)

HOW_ADD_DELETE = "Ваше сообщение должно начинаться с '++' или '--'"
