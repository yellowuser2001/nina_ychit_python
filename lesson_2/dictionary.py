friend = {'name': 'Max', 'age': 23}
print(friend)

print(friend['age'])

friend['has_car'] = True

print(friend)

friend['has_car'] = False

print(friend)

del friend['age']
print(friend)

if 'name' in friend:
    print('have a name')
# по ключам
for key in friend.keys():
    print(key)
    print(friend[key])

for key in friend:
    print(key)
    print(friend[key])

# по значениям
for val in friend.values():
    print(val)

# пары ключ значение
for item in friend.items():
    print(item)

for key, val in friend.items():
    print(key)
    print(val)


