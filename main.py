from worker import WORKER

def main():
    workers = []

    n = int(input("Введите количество работников для добавления: "))
    for i in range(n):
        print(f"\nВведите данные работника {i+1}:")
        surname = input("Фамилия и инициалы: ")
        position = input("Должность: ")
        salary = float(input("Зарплата: "))
        year_joined = int(input("Год поступления на работу: "))
        worker = WORKER(surname, position, salary, year_joined)
        workers.append(worker)

    min_experience = int(input("\nВведите минимальный стаж работы для фильтрации: "))
    filtered_workers = [w for w in workers if w.get_experience() > min_experience]

    print("\nРаботники со стажем больше указанного:")
    if filtered_workers:
        for w in filtered_workers:
            print(f"- {w.get_surname()} (Стаж: {w.get_experience()} лет)")
    else:
        print("Работники не найдены.")

if __name__ == "__main__":
    main()