# name = 'Алексей'
#
# letter = name[-3]
# print(letter)

# friends = 'Нина Лёша'
#
# print(friends)
#
# print(len(friends))
#
# print(friends.find('Лёш'))
#
# print(friends.split())
#
# print(friends.upper())
#
# print(friends.lower())
#
# name = 'Aleksandr'
# age = 25
# format_str = 'Hi {} you {} old'.format(name, age)
# print(format_str)

top_5 = ' Поздравляем : 1.иванов 2. петров 3. сидоров 4. архипов 5. данилов'
start = top_5.find('1')
end = top_5.find('4')

top_3 = top_5 [start: end]

result = 'Поздравляем {} с победой!'.format(top_3.upper())

print(result)

