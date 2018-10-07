# 4.5 순회하기: for

rabbits = ['Flopsy', 'Mopsy', 'Cottontail', 'Peter']
current = 0
while current < len(rabbits):
    print(rabbits[current])
    current += 1

# Flopsy
# Mopsy
# Cottontail
# Petern


for rabbit in rabbits:
    print(rabbit)

# Flopsy
# Mopsy
# Cottontail
# Peter


word = 'cat'
for letter in word:
    print(letter)

# c
# a
# t


accusation = {'room': 'ballroom', 'weapon': 'lead pipe',
              'person': 'Col. Mustard'}
for card in accusation: # 혹은 for card in accusation.keys():
    print(card)

# room
# weapon
# person


for value in accusation.values():
    print(value)

# ballroom
# lead pipe
# Col. Mustard


for item in accusation.items():
    print(item)

# ('room', 'ballroom')
# ('weapon', 'lead pipe')
# ('person', 'Col. Mustard')


for card, contents in accusation.items():
    print('Card', card, 'has the contents', contents)

# Card room has the contents ballroom
# Card weapon has the contents lead pipe
# Card person has the contents Col. Mustard


# 4.5.1 중단하기: break

# 4.5.2 건너뛰기: continue

# 4.5.3 break 확인하기: else

cheeses = []
for cheese in cheeses:
    print('This shop has some lovely', cheese)
    break
else:  # bread 문이 호출되지 않았다면 cheeses가 없는 것이다.
    print('This is not much of a cheese shop, is it?')

# This is not much of a cheese shop, is it?


# 4.5.4 여러 시퀀스 순회하기: zip()

days = ['Monday', 'Tuesday', 'Wednesday']
fruits = ['banana', 'orange', 'peach']
drinks = ['coffee', 'tea', 'beer']
desserts = ['tiramisu', 'ice cream', 'pie', 'pudding']
for day, fruit, drink, dessert in zip(days, fruits, drinks, desserts):
    print(day, ": drink", drink, "- eat", fruit, "- enjoy", dessert)

# Monday : drink coffee - eat banana - enjoy tiramisu
# Tuesday : drink tea - eat orange - enjoy ice cream
# Wednesday : drink beer - eat peach - enjoy pie


english = 'Monday', 'Tuesday', 'Wednesday'
french = 'Lundi', 'Mardi', 'Mercredi'


list( zip(english, french) )
# [('Monday', 'Lundi'), ('Tuesday', 'Mardi'), ('Wednesday', 'Mercredi')]


dict( zip(english, french) )
# {'Monday': 'Lundi', 'Tuesday': 'Mardi', 'Wednesday': 'Mercredi'}


# 4.5.5 숫자 시퀀스 생성하기: range()

for x in range(0,3):
    print(x)

# 0
# 1
# 2
list( range (0, 3) )
# [0, 1, 2]


for x in range(2, -1, -1):
    print(x)

# 2
# 1
# 0
list( range(2, -1, -1) )
# [2, 1, 0]


list( range(0, 11, 2) )
# [0, 2, 4, 6, 8, 10]


# 4.5.6 기타 이터레이터
