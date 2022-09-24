#                               ДЗ
# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".

# my_string = 'Всем неабв мир абвгде !'.split()
# print(' '.join([word for word in my_string if 'абв' not in word]))

# 2. Создайте программу для игры с конфетами человек против человека.
    
#     Условие задачи: На столе лежит 2021 конфета. 
#     Играют два игрока делая ход друг после друга. 
#     Первый ход определяется жеребьёвкой. 
#     За один ход можно забрать не более чем 28 конфет. 
#     Все конфеты оппонента достаются сделавшему последний ход.
# 
# Вариант с багами: 
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

# Вариант рабочий, усовершенствованный
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

#     a) Добавьте игру против бота
 
#     b) Подумайте как наделить бота "интеллектом"
#     (Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?)
    
# 3. Создайте программу для игры в "Крестики-нолики".

# from tkinter import*
# import tkinter

# window = Tk() #Создаю окно
# window.title("Добро пожаловать в игру крестики-нолики") #Название окна
# window.geometry('400x250') #Размер окна 

# user = '0'
# def clik(index): #фу-ция нажатия на кнопку
#     global user #передаем глобальную переменную = 0 в функцию
#     if user == 'x': # если пользователь нажал х, то след ход будет 0 и наоборот
#         user = '0'
#     else:
#         user = 'x'
#     but_list[index].configure(text = user)
#     but_list[index]['state'] = tkinter.DISABLED 
#     but_list[index]['relief'] = tkinter.SUNKEN #tk.SUNKEN: Создается эффект углубления элемента;

# # def start_new_game():
#     # btk_1.destroy закомментированы
#     # btk_2.destroy закомментированы
# but_list = [0 for x in range(9)]
# index = 0
# for i in range(3): #используем двойной цикл, чтобы задать кнопки: 3 на 3 
#     window.columnconfigure(i, weight=1, minsize=75) # строки и столбы сетки будут реагировать на изменение размера окна с помощью метода .columnconfigure() и .rowconfigure()
#     window.rowconfigure(i, weight=1, minsize=50)
#     for j in range(3):
#         frame = Frame(   #Создаем фрейм, чтобы установить расстояние между кнопками
#             master=(window),
#             relief=RAISED, # RAISED создает рамке границу в виде эффекта выпуклости;
#             borderwidth=2 #эффект рамки
#             )
#         frame.grid(row=i, column=j, padx=5, pady=5, sticky="nsew") #Менеджер .grid() работает путем разделения окна или рамки на строки и столбцы (на сетку). row и column (строки и столбца), padx, y добавляет отступ в горизонтальном и вертик. направлении;
#         but_list[index] = Button(master=frame, text='', height = 4, width = 12, command= lambda index = index:clik(index))
#         but_list[index].pack(padx=5, pady=5) #5 пикселей дополнительного отступа вокруг каждого ярлыка с текстом в направлениях x и y:
#         index += 1


# # btk_1 = Button(master=window, text ='Игра с другом', height = 5, width=10, command=start_game) закомментированы
# # btk_2 = Button(master=window, text ='Игра с читером ', height = 5, width=10, command=start_game) закомментированы

# window.mainloop() #указывает Python, что нужно запустить цикл событий Tkinter. Данный метод требуется для событий вроде нажатий на клавиши или кнопки

# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaffffcc
# a3f4c2
