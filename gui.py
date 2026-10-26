import tkinter as tk
from tkinter import messagebox

from logic import Calculator, LogManager


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Сумма цифр после запятой")
        self.geometry("450x300")

        self.calculator = Calculator()
        self.log_manager = LogManager()

        self.create_widgets()

    def create_widgets(self):
        title_label = tk.Label(
            self, text="Введите вещественное число", font=("Arial", 12)
        )
        title_label.pack(pady=10)

        self.number_entry = tk.Entry(self, width=30)
        self.number_entry.pack(pady=5)

        calc_button = tk.Button(self, text="Вычислить", command=self.calculate)
        calc_button.pack(pady=5)

        backup_button = tk.Button(
            self, text="Создать резервную копию", command=self.make_backup
        )
        backup_button.pack(pady=5)

        restore_button = tk.Button(
            self, text="Восстановить лог", command=self.restore_backup
        )
        restore_button.pack(pady=5)

        self.result_label = tk.Label(self, text="Результат:", font=("Arial", 12))
        self.result_label.pack(pady=15)

    def calculate(self):
        try:
            number_text = self.number_entry.get()

            float(number_text.replace(",", "."))

            result = self.calculator.calculate_sum(number_text)

            self.result_label.config(text=f"Результат: {result}")

            self.log_manager.write_log(number_text, result)

        except ValueError:
            messagebox.showerror("Ошибка", "Введите корректное число!")

    def make_backup(self):
        if self.log_manager.backup_log():
            messagebox.showinfo("Успех", "Резервная копия создана.")
        else:
            messagebox.showwarning("Ошибка", "Лог-файл не найден.")

    def restore_backup(self):
        if self.log_manager.restore_log():
            messagebox.showinfo("Успех", "Лог восстановлен.")
        else:
            messagebox.showwarning("Ошибка", "Резервная копия не найдена.")
