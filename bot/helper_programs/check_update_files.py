from os import path
import os
from pathlib import Path
from typing import List, Tuple

# files = Path("/home/ivan/past_dev/Project/Telegram_bot/telegram_finance/bot").glob('*')

res = []
for root, dirs, files in os.walk("/home/ivan/past_dev/Project/Telegram_bot/telegram_finance/bot"):
    for filename in files:
        res.append(os.path.join(root, filename))

    print(dirs)


class CheckUpdateFiles():
    """Проверка на изменения файлов в проекте"""
    def __init__(
            self,
            base_directory: str) -> None:
        self.base_directory = self.__all_files_from_directory(
            base_directory
        )

    def __all_files_from_directory(
            self,
            base_directory: str) -> List[Tuple[str, float]]:
        all_files = list()
        return all_files
