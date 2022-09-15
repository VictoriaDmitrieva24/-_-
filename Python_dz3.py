# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# def poisk(my_numbers):
#     summa = 0
#     for i in range(1,len(my_numbers),2):
#         summa += my_numbers[i]
#     print(f'Сумма элементов списка {my_numbers}, стоящих на нечетной позиции равна: {summa}')

# my_numbers = [2, 3, 5, 9, 3]
# poisk(my_numbers)

# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# from math import ceil

# def result(my_list):

#     list_new = []
#     x = len(my_list)-1
#     for i in range(0, ceil(len(my_list)/2)):
#         reserv = my_list[i] * my_list[x-i]
#         list_new.append(reserv)
#     print(list_new)

# # my_list1 = [2, 3, 4, 5, 6]
# my_list1 = [2, 3, 5, 6]
# result(my_list1)

# Задайте список из вещественных чисел. Напишите программу, которая найдёт
#  разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# my_num = [1.1, 1.2, 3.1, 5.0, 10.01]
# for i in range(0,len(my_num)-1):
#         if (my_num[i]*10) % 10 == 0:
#             del my_num[i]

# def MM(my_num):
#     max_number = 0
#     min_number = 0
#     reserv = []
#     new_num = []
#     for i in range(0,len(my_num)):
#         reserv.append(int(my_num[i]))
#         new_num.append(round(my_num[i]-reserv[i],10))
#     max_number = max(new_num)
#     min_number = min(new_num)
#     print(f'Разница: {max_number - min_number}')

# MM(my_num)

# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# x = int(input('Введите число -> '))
# y = ''
# def kod_2(x,y):
#     while x > 0:
#         y = str(x % 2) + y
#         x = x // 2
#     print(f'В двоичной системе счисления {x} выглядит так ->: {y}')

# kod_2(x,y)

# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# fib1 = fib2 = 1
 
# n = int(input())

# def otriFibbi(fib1,fib2,n):
#     my_list = []
#     my_list.insert(n, fib1)
#     my_list.insert(n-1, fib2)
#     for i in range(2, n):
#         fib1, fib2 = fib2, fib1 + fib2
#         my_list.insert((n-1),fib2)
#     print(my_list.reverse())
    

# def Fibbi(fib1,fib2,n):
#     print(fib1, fib2, end=' ')
#     for i in range(2, n):
#         fib1, fib2 = fib2, fib1 + fib2
#         print(fib2, end=' ')

# otriFibbi(fib1,fib2,n)
# Fibbi(fib1,fib2,n)