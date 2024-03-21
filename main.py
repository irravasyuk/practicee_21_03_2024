# Завдання 1
# До вже реалізованого класу «Людина» додайте статичний метод, який під час виклику повертає кількість
# створених об’єктів класу «Людина».
# class Human:
#     count = 0
#
#     def __init__(self, full_name, date_of_birth, phone_number, city, country, home_address):
#         self.full_name = full_name
#         self.date_of_birth = date_of_birth
#         self.phone_number = phone_number
#         self.city = city
#         self.country = country
#         self.home_address = home_address
#         Human.count += 1
#
#     @staticmethod
#     def count_human():
#         return Human.count
#
#     def input_data(self):
#         self.full_name = input("Введіть піб: ")
#         self.date_of_birth = input("Введіть дату народження: ")
#         self.phone_number = input("Введіть контактний телефон: ")
#         self.city = input("Введіть місто: ")
#         self.country = input("Введіть країну: ")
#         self.home_address = input("Введіть домашню адресу: ")
#
#     def display(self):
#         print("піб:", self.full_name)
#         print("дата народження:", self.date_of_birth)
#         print("контактний телефон:", self.phone_number)
#         print("місто:", self.city)
#         print("країна:", self.country)
#         print("домашня адреса:", self.home_address)
#
#     def update_data(self, attribute):
#         if attribute == "піб":
#             self.full_name = input("Введіть новий піб: ")
#             print("Інформація оновлена.")
#         elif attribute == "дата народження":
#             self.date_of_birth = input("Введіть нову дату народження: ")
#             print("Інформація оновлена.")
#         elif attribute == "контактний телефон":
#             self.phone_number = input("Введіть новий контактний телефон: ")
#             print("Інформація оновлена.")
#         elif attribute == "місто":
#             self.city = input("Введіть нове місто: ")
#             print("Інформація оновлена.")
#         elif attribute == "країна":
#             self.country = input("Введіть нову країну: ")
#             print("Інформація оновлена.")
#         elif attribute == "домащня адреса":
#             self.home_address = input("Введіть нову домашню адресу: ")
#             print("Інформація оновлена.")
#         else:
#             print("Невірний ввід.")
#
# person = Human("", "", "", "", "", "")
# person.input_data()
# print("\nІнформація про людину:")
# person.display()
#
# while True:
#     information_to_change = input("\nВведіть яку інформацію ви хочете змінити (або 0, якщо нічого): ").lower()
#     if information_to_change == "0":
#         print("Програма завершена :(")
#         break
#
#     person.update_data(information_to_change)
#
# print("\nОновлена інформація: ")
# person.display()
#
# print("\nКількість створених об'єктів класу Human: ", Human.count_human())


# Завдання 2
# Створіть клас для підрахунку площі геометричних
# фігур. Клас має надавати функціональність підрахунку
# площі трикутника за різними формулами, площі прямокутника, площі квадрата, площі ромба. Методи класу для
# підрахунку площі реалізуйте за допомогою статичних
# методів. Також клас має розрахувати кількість підрахунків площі та повернути це значення статичним методом.
# class Area:
#     count = 0
#
#     @staticmethod
#     def triangle_area(a, b):
#         Area.count += 1
#         return 0.5 * a * b
#
#     @staticmethod
#     def rectangle_area(width, height):
#         Area.count += 1
#         return width * height
#
#     @staticmethod
#     def square_area(side_length):
#         Area.count += 1
#         return side_length ** 2
#
#     @staticmethod
#     def rhomb_area(diagonal1, diagonal2):
#         Area.count += 1
#         return 0.5 * diagonal1 * diagonal2
#
#     @staticmethod
#     def get_calculation_count():
#         return Area.count
#
# print("Площа трикутника: ", Area.triangle_area(2, 8))
# print("Площа прямокутника: ", Area.rectangle_area(8, 10))
# print("Площа квадрата: ", Area.square_area(8))
# print("Площа ромба: ", Area.rhomb_area(5, 3))
# print("Kількість підрахунків площі: ", Area.get_calculation_count())


# Завдання 3
# Створіть клас для підрахунку максимуму з чотирьох
# аргументів, мінімуму з чотирьох аргументів, середнє
# арифметичне із чотирьох аргументів, факторіалу аргументу. Реалізуйте функціональність у вигляді статичних
# методів.
# class Calculator:
#
#     @staticmethod
#     def maximum(num1, num2, num3, num4):
#         return max(num1, num2, num3, num4)
#
#     @staticmethod
#     def minimum(num1, num2, num3, num4):
#         return min(num1, num2, num3, num4)
#
#     @staticmethod
#     def arifm(num1, num2, num3, num4):
#         return (num1 + num2 + num3 + num4) / 4
#
#     @staticmethod
#     def factorial(num):
#         try:
#             if num < 0:
#                 raise ValueError("Факторіал визначається тільки для додатніх цілих чисел")
#             elif num == 0:
#                 return 1
#             else:
#                 return num * Calculator.factorial(num - 1)
#         except ValueError as e:
#             return str(e)
#
# print("Максимум: ", Calculator.maximum(1, 2, 3, 4))
# print("Мінімум: ", Calculator.minimum(1, 2, 3, 4))
# print("Середнє арифметичне: ", Calculator.arifm(1, 2, 3, 4))
# print("Факторіал 4: ", Calculator.factorial(4))
# print("Факторіал -4: ", Calculator.factorial(-4))
# print("Факторіал 0: ", Calculator.factorial(0))

# Завдання 4
# Створіть клас FileUtils, який має метод класу
# count_lines, який приймає шлях до файлу і повертає
# кількість рядків у файлі.


# Завдання 5
# Створіть клас Character, який має атрибути name, health
# та damage. Реалізуйте метод класу attack, який виводить
# повідомлення про атаку гравця.


# Завдання 6
# Створіть клас Student, який має атрибути name, age,
# grade та courses. Реалізуйте метод класу add_course, який
# додає новий предмет до списку курсів студента

