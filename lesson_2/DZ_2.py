# Даны два произвольные списка.
# Удалите из первого списка элементы присутствующие во втором списке.

list_1 = [3, 5, 7, 7, 3, 9, 4, 5]
# list_2 = [3, 6, 1, 2, 8, 4]
#
#
# for i in list_1:
#     if i in list_2:
#         list_1.remove(i)
# print(list_1)


# Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача — вывести дату в текстовом виде, например: второе ноября 2013 года.

months = ['', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября',
          'декабря']

days = ['', 'первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое', 'десятое',
        'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестнадцатое', 'семнадцатое',
        'восемнадцатое', 'девятнадцатое', 'двадцатое', 'двадцать первое', 'двадцать второе', 'двадцать третье',
        'двадцать чертвертое', 'двадцать пятое', 'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое',
        'двадцать девятое', 'тридцатое', 'тридцать первое']

data = '01.08.2001'

# day = days[:: 1]
# month = months[:: 7]

# d, m, y = data.split('.')
# d = int(d)
# m = int(m)
# y = int(y)
# print(d, m, y)
#
# result = f'{days[d]} {months[m]} {y} года'
# print(result)