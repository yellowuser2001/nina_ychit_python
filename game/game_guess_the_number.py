# # Шаг 1 - Загадать случайное число
# import random as rd
#
# number = rd.randint(1, 100)
# # print(number)
#
# while True:
#     # Шаг 2 - Предложить пользователю ввести число
#     user_number = int(input('Введите число: '))
#     # Шаг 3 - сравнение чисел. вывод результата
#     if number == user_number:
#         print('POBEDA!')
#         break
#     elif number < user_number:
#         print('Ваше число больше загаданного')
#     else:
#         print('Ваше число меньше загаданного')

# Вариант 2:

import random

number = random.randint(1, 100)

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}

level = int(input('Выберите уровень сложности: '))
max_count = levels[level]

user_count = int(input('Введите количество пользователей: '))
users = []
for i in range(user_count):
    i += 1
    user_name = input(f'Введите имя пользвателя {i} ')
    users.append(user_name)

print(users)

is_winner = False
winner_name = None

while not is_winner:
    count += 1
    if count > max_count:
        print('Все проиграли')
        break
    print(f'Попытка № {count}')
    for user in users:
        print(f'Ход пользователя {user}')
        user_number = int(input('Введите число: '))
        if user_number == number:
            is_winner = True
            winner_name = user
            break
        elif number < user_number:
            print('Ваше число больше загаданного')
        else:
            print('Ваше число меньше загаданного')
else:
    print(f'ПОБЕДА {winner_name}!!!')

print(number)
