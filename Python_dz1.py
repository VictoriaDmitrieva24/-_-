# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
#  является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input("Введите число: "))
if (a == 6) or (a == 7):
    print("yes")
else: print("no")

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input("Введите X: "))
y = int(input("Введите Y: "))
if (x>0) and (y>0):
    print("Координаты 1 четверти")
elif (x>0) and (y<0):
    print("Координаты 4 четверти")
elif (x<0) and (y>0):
    print("Координаты 2 четверти")
elif (x<0) and (y<0):
    print("Координаты 3 четверти")
