# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 0,56 -> 11

# 1 вариант решения
# x = float(input())
# print(int((x * 10) % 10 + (x * 100) % 10))

# 2 вариант решения
# x = (input("Введите вещественное число "))
# list = x.split('.')
# print(list)
#
# list_1 = []
# for item in list:
#     list_1.append(int(item))
# print(list_1)
#
# summa = 0
# for i in range(len(list_1)):
#    summa += ((int(list_1[i])) % 10 + (int(list_1[i]))// 10)
# print(summa)


# Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
#     *Пример:*
#     - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
# import math
# n = int(input("Введите число: "))
# i = 1
# for i in range(1, n+1):
#    print(math.factorial(i))

# Задайте список из n чисел последовательности (1 + 1\n)^n и выведите на экран их сумму.

# n = int(input("Введите число: "))
# summa = 0
# for i in range(1, n+1):
#     summa += (1+1/i)**i
# print(round((summa),2))

# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных пользователем через пробел позициях.

# n = int(input("Введите число: "))
# list_element = []
# for i in range(-n, n + 1):
#     list_element.append(i)
#     print(i, end=' ')
#
# list_index = []
# for element in input("Введите индексы через пробел: ").split():
#     list_index.append(int(element))
# print(list_index)
#
# summa = 0
# j = 0
# k = 0
# for j in range(len(list_element)):
#     for k in range(len(list_index)):
#         if j == list_index[k]:
#             summa += int(list_element[j])
# print(f'Сумма элементов с индексами {list_index} = {summa}')


# Реализуйте алгоритм перемешивания списка.

# 1 вариант решения
# import random
# elem = [1, 5, 8, 'hi']
# print(f'Первоначальный список: {elem}')
# random.shuffle(elem)
# print(f'Перемешанный список:   {elem}')

# 2 вариант решения (не работает)
# elem = [1, 5, 8, 'hi']
# elem_copy = []
#
# for i in range(len(elem)):
#     elem_copy.append(elem[i])
# print(elem_copy)
#
#
# for j in range(len(elem)):
#     for k in range(len(elem_copy)):
#         elem[j] = elem_copy[len(elem_copy)-1]
#         elem[len(elem)-1] = elem_copy[k]
# print(elem)

