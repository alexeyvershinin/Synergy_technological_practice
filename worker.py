from datetime import datetime

class WORKER:
    """
        Класс WORKER представляет сотрудника компании.

        Атрибуты:
            __surname (str): Фамилия и инициалы сотрудника.
            __position (str): Название должности.
            __salary (float): Зарплата сотрудника.
            __year_joined (int): Год поступления на работу.

        Методы:
            set_surname(surname): Устанавливает фамилию и инициалы.
            set_position(position): Устанавливает должность.
            set_salary(salary): Устанавливает зарплату (должна быть >= 0).
            set_year_joined(year): Устанавливает год поступления на работу.
            get_surname(): Возвращает фамилию и инициалы.
            get_position(): Возвращает должность.
            get_salary(): Возвращает зарплату.
            get_year_joined(): Возвращает год поступления.
            get_experience(): Вычисляет стаж работы.
            display_info(): Выводит полную информацию о сотруднике.
    """

    def __init__(self, surname='', position='', salary=0, year_joined=0):
        self.__surname = surname
        self.__position = position
        self.__salary = salary
        self.__year_joined = year_joined

    # Методы изменения атрибутов (set)
    def set_surname(self, surname):
        self.__surname = surname

    def set_position(self, position):
        self.__position = position

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Ошибка: зарплата не может быть отрицательной.")

    def set_year_joined(self, year):
        current_year = datetime.now().year
        if 1900 <= year <= current_year:
            self.__year_joined = year
        else:
            print("Ошибка: некорректный год поступления на работу.")

    def get_surname(self):
        return self.__surname

    def get_position(self):
        return self.__position

    def get_salary(self):
        return self.__salary

    def get_year_joined(self):
        return self.__year_joined

    def get_experience(self):
        current_year = datetime.now().year
        return current_year - self.__year_joined

    def display_info(self):
        print(f"{self.__surname}, Должность: {self.__position}, Зарплата: {self.__salary}, Год поступления: {self.__year_joined}, Стаж: {self.get_experience()} лет")
