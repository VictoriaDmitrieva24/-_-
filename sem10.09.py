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

# def nok(number_1, number_2):
#     count  = 0
#     reserv = number_1 * number_2
#     while ((reserv - count) % number_1 != 0) and ((reserv - count) % number_2 != 0):
#         count += 1
#     print(f'NOK: {reserv}')

# number_1 = int(input('x1= '))
# number_2 = int(input('x2= '))

# print(nok(number_1, number_2))


#                         СЕМИНАР 5
# 1. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# 1 2 3 5

# наше решение не работает:
# numbers = '1'
# list_1 = []

# with open('fail.txt', 'w') as data:
#     data.write(numbers)

# with open('fail.txt', 'r') as data:
#     for i in data:
#         list_1.append(i)
#         list_1.append(' ')
# print(list_1)

# for i in range(len(numbers)):
#     if numbers[i]-1 != numbers[i-1]:
#         print(numbers[i]+1)



# path_1 = 'task1.txt'

# def read_file(path):
#     out_string = ''
#     res_txt = open(path, 'r')
#     out_string = res_txt.read()
#     res_txt.close()
#     out_list = out_string.split()

#     for i in range(0, len(out_list)):
#         out_list[i] = int(out_list[i])

#     return out_list

# def find_number(input_list: list):
    
#     for i in range(1, len(input_list)):
#         if input_list[i] - 1 != input_list[i - 1]:
#             number = input_list[i - 1] + 1
#             break
#     return number


# print(f'Не хватает числа {find_number(read_file(path_1))}')

# Решение 3:
# my_list = [1, 2, 4, 5, 6, 8, 9, 11]

# res = [(my_list[i] - 1) for i in range(1, len(my_list)) if (my_list[i] - 1) != my_list[i - 1]]
# print(res)

# 2. Дан список чисел. Создайте список, в который попадают числа, 
# описываемые возрастающую последовательность. Порядок элементов менять нельзя.
    
#     *Пример:* 
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 5, 6, 7] и т.д.

# 1 вариант:    
# list = [1, 5, 2, 3, 4, 6, 1, 7]
# new_list = [list[0]]
# max = list[0]
# for i in list:
#     if i > max:
#         new_list.append(i)
#         max = i
# print(new_list)

# 2 вариант:
# my_list = [1, 5, 2, 3, 4, 6, 1, 7]

# res = [my_list[0]]
# [res.append(item) for item in my_list if item > res[-1]]
# print(res)


# 3. Напишите программу, удаляющую из текста все слова, содержащие "абв".
# 'Мы неабв очень любим Питон иабв Джавуабв!'
# 'Мы очень любим Питон!'

# 1 вариант:
# print (' '.join(filter(lambda x: not 'абв' in x,'Мы неабв очень любим Питон иабв Джавуабв!'.split())))

# 2 вариант:
# my_str = 'Мы неабв очень любим Питон иабв Джавуабв!'.split()
# print(' '.join([word for word in my_str if 'абв' not in word]))


#                                      СЕМИНАР 5
# 1. Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный. 
    
#     *Пример:* 
    
#     2+2 => 4; 
    
#     1+2*3 => 7; 
    
#     1-2*3 => -5;

# import re

# a = input()
# result = 0
# for i in range(len(a)):
#     if a[i] == '*':
#         result = int(a[i-1]) * int(a[i+1])
#         print(result)
#     if a[i] == '/':
#         result = int(a[i-1]) / int(a[i+1])
#         print(result)
#     if a[i] == '+':
#         result = int(a[i-1]) + int(a[i+1])
#         print(result)
#     if a[i] == '-':
#         result = int(a[i-1]) - int(a[i+1])
#         print(result)

# print(result)


#  Вариант:
# expression = input('Что вычислить?')
# print(eval(expression))




#     - Добавьте возможность использования скобок, меняющих приоритет операций.
        
#         *Пример:* 
        
#         1+2*3 => 7; 
        
#         (1+2)*3 => 9;
        

# 2. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

# *Пример:* 
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]

# 1 вариант
# from random import random

# numbers = [1, 2, 4, 5, 5, 6, 6, 6]
# result = []
# for i in range(0, len(numbers)):
#     count = 0
#     for j in range(0, len(numbers)):
#         if numbers[i] == numbe  rs[j]:
#             count += 1
#     if count == 1:
#         result.append(numbers[i])
# print(result)

# 2 вариант
# numbers = [1, 5, 7, 8, 9, 23, 65]
# print(numbers)
# num_copy = []
# for i in range(0, len(numbers)):
#     num_copy.append(int(numbers[i]))
# print(num_copy)
# print(type(num_copy))
# reserv = []
# for j in range(0, max(num_copy)+1):
#     reserv.append(j)
# print(reserv)
# result = []
# for i in range(0,len(reserv)):
#     for j in range(0,len(num_copy)):
#         if reserv[i] == num_copy[j]:
#             result.insert(random.randint(0,len(num_copy)), (reserv[i]))
# print(result)

# 3 вариант через фильтр:
# my_list = [1, 1, 2, 3, 4, 4, 5]
# print(tuple(filter(lambda num: my_list.count(num) == 1, my_list))) #превращаем в кортеж(tuple)
