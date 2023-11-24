# Задание 1
def sort_list(lst):
    if sum(lst) / len(lst) > 0:
        first_two_thirds = sorted(lst[:int(len(lst)*2/3)])
        last_third = lst[int(len(lst)*2/3):][::-1]
        return first_two_thirds + last_third
    else:
        first_third = sorted(lst[:int(len(lst)/3)])
        last_two_thirds = lst[int(len(lst)/3):][::-1]
        return first_third + last_two_thirds


my_list = [4, 2, 7, -1, 0, 5, 3, -3, 9]
sorted_list = sort_list(my_list)
print(sorted_list)


# Задание 2
grades = []

for i in range(10):
    grade = int(input("Введите оценку: "))
    while grade < 1 or grade > 12:
        grade = int(input("Оценка должна быть от 1 до 12. Введите оценку: "))
    grades.append(grade)


def print_grades():
    print("Оценки студента:", grades)


def retake_exam():
    index = int(input("Введите номер оценки, которую нужно изменить: "))
    new_grade = int(input("Введите новую оценку: "))
    while new_grade < 1 or new_grade > 12:
        new_grade = int(input("Оценка должна быть от 1 до 12. Введите новую оценку: "))
    grades[index - 1] = new_grade


def check_scholarship():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 10.7:
        print("Студент имеет право на стипендию")
    else:
        print("Студент не имеет права на стипендию")


def sort_grades():
    option = input("Выберите вариант сортировки (по возрастанию или убыванию): ")
    if option.lower() == "по возрастанию":
        sorted_grades = sorted(grades)
        print("Отсортированные оценки по возрастанию:", sorted_grades)
    elif option.lower() == "по убыванию":
        sorted_grades = sorted(grades, reverse=True)
        print("Отсортированные оценки по убыванию:", sorted_grades)
    else:
        print("Некорректный ввод")


while True:
    print("\nМеню:")
    print("1. Вывод оценок")
    print("2. Пересдача экзамена")
    print("3. Выходит ли стипендия")
    print("4. Вывод отсортированного списка оценок")
    print("5. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        print_grades()
    elif choice == "2":
        retake_exam()
    elif choice == "3":
        check_scholarship()
    elif choice == "4":
        sort_grades()
    elif choice == "5":
        break
    else:
        print("Некорректный ввод")
print()


# Задание 3
def bubble_sort(lst):
    n = len(lst)
    swapped = True

    while swapped:
        swapped = False
        for i in range(1, n):
            if lst[i-1] > lst[i]:
                lst[i-1], lst[i] = lst[i], lst[i-1]
                swapped = True

        n -= 1

    return lst


my_list = [4, 2, 7, -1, 0, 5, 3, -3, 9]
sorted_list = bubble_sort(my_list)
print(sorted_list)

