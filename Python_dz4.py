# Вычислить число c заданной точностью d 
# Пример: при d = 0.001, π = 3.141.d=0.001,π=3.141.﻿﻿

# d = 100.25632545
# to = (input("Введите точность числа -> ")).split('.')
# x = int(len(to[1]))
# y = 10**x
# result = int(d * y) / y
# print(result)

# Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

# n = int(input("Введите N -> "))
# def poisk(n):
#     for num in range(1,n):
#             count = 0
#             delit = 2
#             while delit<num:
#                 if num%delit == 0:
#                     count += 1
#                 delit += 1
#             if count == 0:
#                 print (f'{num}', end =' ')
# poisk(n)

# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
# [1, 2, 4, 5, 5, 6, 6, 6] -> [1, 2, 4, 5,6]

# 1 вариант
# from random import random

# numbers = [1, 2, 4, 5, 5, 6, 6, 6]
# result = []
# for i in range(0, len(numbers)):
#     count = 0
#     for j in range(0, len(numbers)):
#         if numbers[i] == numbers[j]:
#             count += 1
#     if count == 1:
#         result.append(numbers[i])
# print(result)

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

# 2 вариант (с помощью множества)
# numbers = {"1", "5", "7", "8", "9", "23", "65"}
# print(numbers)

# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k. 
# Пример: k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 35.

# from random import randint


# def new_list(kk, list_my_my):
#     while kk != 0:
#         list_my_my.append(randint(0, 100))
#         kk -= 1


# k = int(input("Введите k -> "))
# list_my = []
# k += 1
# new_list(k, list_my)
# result = ''

# for i in range(len(list_my)-1):
#     k -= 1
#     if list_my[i] != 0:
#         result += f'{list_my[i]} '
#         if k == 0:
#             result += '= 0'
#         elif k == 1:
#             result += f'* x  '
#         else:
#             result += f'* x ^ {k}  '
#     if list_my[0] == 0:
#         continue
#     if list_my[i+1] != 0:
#         result += '+ '

# if list_my[-1] == 0:
#     result += '= 0'
# else:
#     result += f'{list_my[-1]} = 0'

# with open('Text.txt', 'w') as fail:
#     fail.write(result)

# print(result)
# print(list_my)

# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

