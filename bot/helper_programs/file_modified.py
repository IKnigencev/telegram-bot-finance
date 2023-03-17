from os import path
import time
import traceback


class FileModifiled():
    def __init__(self, file_path, callback) -> None:
        self.file_path = file_path
        self.callback = callback
        self.modified = path.getatime(file_path)
