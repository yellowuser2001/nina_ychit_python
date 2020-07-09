friend_name = 'Ivan'
friends = ['Ivan', 'Oleg', 'Ilya']
roles = ('programmist', 'admin', 'boss')

i = 0

while i < len(friends):
    friend = friends[i]
    print(friend)
    i +=1

for friend in friends:
    print(friend)

for role in roles:
    print(role)

print('end')