print('СОРЕВНОВАНИЯ ПО PYTHON')
count = int(input('Введите количество участников: '))
i = count
members = []

while i > 0:
    name = input('Кто занял {} место? '.format(i))
    members.append(name)
    i -= 1

print('В соревновании участвовали: ', sorted(members))

# записали людей с конца?
members.reverse()

result = members[:3]

result = f'Победители {result} поздравляем!'
print(result)

