# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

# 1 вариант решения
# import time

# def my_random(minn, maxx):
#     time.sleep(0.3)
#     return int((time.time() % 1  * (maxx - minn)) + minn)
# #                     0.9                  7           1

# for i in range(10):
#     print(my_random(1, 9))

# 2 вариант решения
# def random(a,b):
#     the_set = set()
#     list = []
#     for i in range(a,b):
#         the_set.add(str(i))

#     for e in the_set:
#         list.append(e)
#     print(list)

# random(5, 10)

#3 вариант решения
# import time

# def random():
#     interval = int(input('Введите желаемый интервал рандома: '))
#     ms = time.time()*1000.0
#     b = int(ms)
#     d = ms - b
#     answer = d * interval
#     print(int(round(answer, 0)))
#     return answer

# random()


# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['efg23', '79234gefg', 'sdgs', 'g53']
# '2'
# ['efg23', '79234gefg']

# list1 = ['efg23', '79234gefg', 'sdgs', 'g53']

# def func(list, x):  
#     count = 0
#     for i in range(0,len(list)):
#         if x in list[i]:
#             count += 1
#     print(count)

# x = input("vvedite  ")
# func(list1, x)

# 3. Напишите программу, которая определит позицию второго вхождения 
# строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# list = ["qwe", "asd", "qwe", "zxc", "qwe", "ertqwe"]
# x = 'qwe'

# def Entry(list, x):
#     count = 0
#     for i in range(0, len(list)):
#         if x in list[i]:
#             count += 1
#             if count == 2:
#                 print(i)
#             else: print('no 2 vxo')
   
# Entry(list, x)

# 2 решение
# def findstr(my_list: list, find_string: str) -> int:
#     count = 0
#     for i in range(len(my_list)):
#         if find_string == my_list[i]:
#             count += 1
#             if count == 2:
#                 return i
#     return -1

# list_find = ["йцу", "фыв","йцу", "ячс", "цук", "йцукен"]
# find_string = "йцу"

# print(findstr(list_find, find_string))

# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. 
# В качестве символа-разделителя используйте пробел.

# user_string = input("Введите строку из чисел с разделителем в виде пробела: ").split(" ")
# numbers = list(map(int, user_string))
# print(max(numbers), min(numbers))

# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами: 
# 1) с помощью математических формул нахождения корней квадратного уравнения 
# 2) с помощью дополнительных библиотек Python

# from math import sqrt

# def disk(a: int = 0, b: int = 0,c: int = 0) -> float:
#     d=b**2-(4*a*c)
#     print(f"Ваш дескриминант равен {d}")
#     if d < 0:
#         return []
#     elif d == 0:
#         x = (-1*b)/(2*a)
#         return [x]

#     x1 = (-b+sqrt(d))/(2*a)  
#     x2 = (-b-sqrt(d))/(2*a)
#     return [x1,x2]

# print('Ax2 + Bx + C = 0')
# a = int(input('Введите A: '))
# b = int(input('Введите B: '))
# c = int(input('Введите C: '))
# print(disk(a,b,c))

# from math import *

# def square_root(a: int = 0, b: int = 0, c: int = 0) -> list:
#     discriminant = (b ** 2) - (4 * a * c)
#     if discriminant < 0:
#         return []
#     elif discriminant == 0:
#         x = - (b / (2 * a))
#         return [x]

#     x1 = (-b + sqrt(discriminant)) / (2 * a)
#     x2 = (-b - sqrt(discriminant)) / (2 * a)
#     return [x1, x2]
    
# print('Ax² + Bx + C = 0')
# a = int(input('A= '))
# b = int(input('B= '))
# c = int(input('C= '))
# print(square_root(a, b, c))

# Задайте два числа.
# Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

def nok(number_1, number_2):
    count  = 0
    reserv = number_1 * number_2
    while ((reserv - count) % number_1 != 0) and ((reserv - count) % number_2 != 0):
        count += 1
    print(f'NOK: {reserv}')

number_1 = int(input('x1= '))
number_2 = int(input('x2= '))

print(nok(number_1, number_2))



