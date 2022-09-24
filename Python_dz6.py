#                                             Задача 1 :
#     Условие задачи: На столе лежит 2021 конфета. 
#     Играют два игрока делая ход друг после друга. 
#     Первый ход определяется жеребьёвкой. 
#     За один ход можно забрать не более чем 28 конфет. 
#     Все конфеты оппонента достаются сделавшему последний ход.
# 
#                                            Вариант с багами: 

# from random import randint

# name_igrok1 = input('Введите имя игрока №1 ->')
# name_igrok2 = input('Введите имя игрока №2 ->')
# num = randint(1,2)
# flag = 2
# result = 100
# if num == 1:
#     print(f'Первым ходит игрок: {name_igrok1}')
# else:
#     print(f'Первым ходит игрок: {name_igrok2}')

# while result != 1:
#     number_1 = int(input(f'Игрок № 1 введите кол-во конфет, которые хотите забрать со стола ->'))
#     if (number_1 > result) or (number_1 > 28) or (number_1 < 1):
#         number_1 = int(input(f'Ваш ход нарушает правила игры, попробуйте еще раз ->'))
#     result -= number_1
#     flag -= 1  
#     print(f'Остаток конфет равен: {result}')
#     number_2 = int(input(f'Игрок № 2 введите кол-во конфет, которые хотите забрать со стола ->'))
#     if (number_2 > result) or (number_2 > 28) or (number_2 < 1):
#         number_2 = int(input(f'Ваш ход нарушает правила игры, попробуйте еще раз ->'))
#     result -= number_2
#     print(f'Остаток конфет равен: {result}')
#     flag += 1
# if flag == 2:
#     print('Игрок 1 - вы ПОБЕДИЛИ')
# else:
#     print('Игрок 2 - вы ПОБЕДИЛИ')  

#                                       Вариант рабочий, усовершенствованный
# from random import randint


# name_igrok_1 = input('Введите имя игрока №1 ->')
# name_igrok_2 = input('Введите имя игрока №2 ->')
# num = randint(0, 1)
# result = 100

# while result > 0:
#     num = not num
#     maxim = result > 28
#     while True:
#         try:
#             number = int(input(f'Игрок {name_igrok_1 if num else name_igrok_2} введите кол-во конфет, которые хотите забрать со стола ->'))
#             break
#         except Exception as oshibka:
#             print(oshibka)
#     while number > (28 if maxim else result) or (number <= 0):
#         number = int(input(f'Ваш ход нарушает правила игры, попробуйте еще раз ->'))
#     result -= number
#     print(f'Остаток конфет равен: {result}')

# print(f'Игрок {name_igrok_1 if num else name_igrok_2} - вы ПОБЕДИЛИ')

#                                          Задача 2:
#  Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.
# [1, 2, 4, 5, 5, 6, 6, 6] -> [1, 2, 4, 5,6]

# my_list = [1, 2, 4, 5, 5, 6, 6, 6]
# print(tuple(filter(lambda num: my_list.count(num) == 1, my_list))) #превращаем в кортеж(tuple)


#                                           Задача 3:
# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

# Изначальный вариант:
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

from math import ceil

reserv = 0
my_list = [2, 3, 4, 5, 6] 
res = []
res = [res.append(my_list[item] * my_list[len(my_list)-1-item]) for item in range(0, ceil(len(my_list)/2))]
print(res)