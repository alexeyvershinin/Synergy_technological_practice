Пример использования класса WORKER:

from worker_module import WORKER

# Создание объекта
worker = WORKER("Иванов И.И.", "Инженер", 50000, 2018)

# Изменение данных
worker.set_salary(55000)
worker.set_position("Старший инженер")

# Получение информации
print(worker.get_surname())  # Иванов И.И.
print(worker.get_experience())  # Стаж работы в годах

# Вывод полной информации
worker.display_info()
