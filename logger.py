from datetime import datetime as Date
import logging


class Logger:
    def __init__(self, file_path):
        self._logger = logging.getLogger("VishMonitorLogger")
        self._logger.setLevel(logging.INFO)
        
        _console_handler = logging.StreamHandler()
        _console_handler.setLevel(logging.INFO)
        
        _file_handler = logging.FileHandler(file_path)
        _file_handler.setLevel(logging.INFO)
        
        _formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        _file_handler.setFormatter(_formatter)
        
        self._logger.addHandler(_file_handler)
        self._logger.addHandler(_console_handler)
        

    def warn(self, message):
        self._logger.warn(f"{message}")

    def error(self, message):
        self._logger.error(f"{message}")

    def log(self, message):
        self._logger.info(f"{message}")
    
    def to_console(self, message):
        print(message)
