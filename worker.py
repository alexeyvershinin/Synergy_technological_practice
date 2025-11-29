from datetime import datetime

class WORKER:
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
