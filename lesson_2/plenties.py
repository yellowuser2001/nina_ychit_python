cities = ['Las VEgas', 'Oslo', 'Minsk','Oslo']
print(cities)

cities = set(cities)

print(cities)

cities = {'Las VEgas', 'Oslo', 'Minsk'}
print(cities)

cities.remove('Las VEgas')
print(cities)

print('Oslo' in cities)

for city in cities:
    print(city)