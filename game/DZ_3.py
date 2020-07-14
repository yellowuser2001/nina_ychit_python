# В этой игре человек загадывает число, а компьютер пытается его угадать.
# В начале игры человек загадывает число от 1 до 100 в уме или записывает его на листок бумаги.
# Компьютер начинает его отгадывать предлагая игроку варианты чисел.
# Если компьютер угадал число, игрок выбирает “победа”.
# Если компьютер назвал число меньше загаданного, игрок должен выбрать “загаданное число больше”.
# Если компьютер назвал число больше, игрок должен выбрать “загаданное число меньше”.
# Игра продолжается до тех пор пока компьютер не отгадает число.

import random

levels = {1: 10, 2: 5, 3: 3}
count = 0
answer = 14
level = int(input('уровень сложности: '))
max_count = levels[level]

number_1 = 1
number_2 = 50

user_number = None

while True:
    count += 1
    number = random.randint(number_1, number_2)
    print(f'Я угадал число: {number} ?')
    answer = input('> < = Число больше загаданного?: ')
    if answer == "=":
        print(f'Победа! Сразу хотел ввести число {number}')
        break
    print(f'Попытка № {count}')
    if answer == '<':
        number_1 = number + 1
    else:
        number_2 = number - 1
