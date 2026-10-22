import os
import shutil
from datetime import datetime

class Calculator:
    def calculate_sum(self, number_str):

        number_str = number_str.replace(",", ".")

        if "." not in number_str:
            return 0

        decimal_part = number_str.split(".")[1]

        return sum(
            int(digit)
            for digit in decimal_part
            if digit.isdigit()
        )

class LogManager:
    LOG_FILE = "logs/calculations.log"
    BACKUP_FILE = "backup/backup_calculations.log"

    def __init__(self):
        os.makedirs("logs", exist_ok=True)
        os.makedirs("backup", exist_ok=True)

    def write_log(self, number, result):
        with open(self.LOG_FILE, "a", encoding="utf-8") as file:
            file.write(f"Дата: {datetime.now()}\n")
            file.write(f"Число: {number}\n")
            file.write(f"Сумма цифр: {result}\n")
            file.write("-" * 40 + "\n")

    def backup_log(self):
        if os.path.exists(self.LOG_FILE):
            shutil.copy(self.LOG_FILE, self.BACKUP_FILE)
            return True
        return False

    def restore_log(self):
        if os.path.exists(self.BACKUP_FILE):
            shutil.copy(self.BACKUP_FILE, self.LOG_FILE)
            return True
        return False