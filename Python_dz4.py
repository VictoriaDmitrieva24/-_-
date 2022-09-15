# Вычислить число c заданной точностью d 
# Пример: при d = 0.001, π = 3.141.d=0.001,π=3.141.﻿﻿

# d = 0.25632545
# to = int(input("Введите точность числа -> "))
# def func(d):
#     x = 0
#     for i in range(0,to):
#         x += 1
#     y = 10**x
#     result = int(d * y) / y
#     print(result)

# func(d)

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

from random import randint


def new_list(kk, list_my_my):
    while kk != 0:
        list_my_my.append(randint(0, 10))
        kk -= 1

k = int(input("Введите k -> ")) + 1
list_my = []
new_list(k, list_my)

for i in list_my:
    k_1 = k - 1
    if i != 0:
        print(str(f'{i}', end=' '))
        if k == 0:
            print(str(' = 0'))
        else:
            print(str(f'* x ^ {k_1} +', end=' '))
    k -= 1

with open('Text.txt', 'w') as fail:

# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.