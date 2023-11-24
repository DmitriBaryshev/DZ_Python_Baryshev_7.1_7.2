# Задание 1
ids = [101, 102, 103, 104, 105]
phone_numbers = [5551234, 5555678, 5559876, 5554321, 5558765]


def sort_by_ids():
    sorted_data = sorted(zip(ids, phone_numbers))
    print("Отсортированный список по идентификационным кодам:", sorted_data)


def sort_by_phone_numbers():
    sorted_data = sorted(zip(phone_numbers, ids))
    print("Отсортированный список по номерам телефона:", sorted_data)


def print_users():
    for i in range(len(ids)):
        print("Идентификационный код:", ids[i], "Телефонный номер:", phone_numbers[i])


while True:
    print("\nМеню:")
    print("1. Отсортировать по идентификационным кодам")
    print("2. Отсортировать по номерам телефона")
    print("3. Вывести список пользователей с кодами и телефонами")
    print("4. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        sort_by_ids()
    elif choice == "2":
        sort_by_phone_numbers()
    elif choice == "3":
        print_users()
    elif choice == "4":
        break
    else:
        print("Некорректный ввод")


# Задание 2
books = ["Book1", "Book2", "Book3", "Book4", "Book5"]
years = [2000, 1998, 2010, 2005, 1995]


def sort_by_books():
    sorted_data = sorted(zip(books, years))
    print("Отсортированный список по названиям книг:", sorted_data)


def sort_by_years():
    sorted_data = sorted(zip(years, books))
    print("Отсортированный список по годам выпуска:", sorted_data)


def print_books():
    for i in range(len(books)):
        print("Название книги:", books[i], "Год выпуска:", years[i])


while True:
    print("\nМеню:")
    print("1. Отсортировать по названиям книг")
    print("2. Отсортировать по годам выпуска")
    print("3. Вывести список книг с названиями и годами выпуска")
    print("4. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        sort_by_books()
    elif choice == "2":
        sort_by_years()
    elif choice == "3":
        print_books()
    elif choice == "4":
        break
    else:
        print("Некорректный ввод")
