# 4.6 컴프리헨션

# 4.6.1 리스트 컴프리헨션

number_list = []
number_list.append(1)
number_list.append(2)
number_list.append(3)
number_list.append(4)
number_list.append(5)
number_list
# [1, 2, 3, 4, 5]


number_list = []
for number in range(1, 6):
    number_list.append(number)

number_list
# [1, 2, 3, 4, 5]


number_list = list(range(1, 6))
number_list
# [1, 2, 3, 4, 5]


number_list = [number for number in range(1,6)]
number_list
# [1, 2, 3, 4, 5]


number_list = [number-1 for number in range(1,6)]
number_list
# [0, 1, 2, 3, 4]


a_list = [number for number in range(1,6) if number % 2 == 1]
a_list
# [1, 3, 5]


a_list = []
for number in range(1,6):
    if number % 2 == 1:
        a_list.append(number)

a_list
# [1, 3, 5]


rows = range(1,4)
cols = range(1,3)
for row in rows:
    for col in cols:
        print(row, col)

# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2


rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
for cell in cells:
    print(cell)

# (1, 1)
# (1, 2)
# (2, 1)
# (2, 2)
# (3, 1)
# (3, 2)


for row, col in cells:
    print(row, col)

# 1 1
# 1 2
# 2 1
# 2 2
# 3 1
# 3 2


# 4.6.2 딕셔너리 컴프리헨션

word = 'letters'
letter_counts = {letter: word.count(letter) for letter in word}
letter_counts
# {'l': 1, 'e': 2, 't': 2, 'r': 1, 's': 1}


word = 'letters'
letter_counts = {letter: word.count(letter) for letter in set(word)}
letter_counts
# {'e': 2, 't': 2, 's': 1, 'r': 1, 'l': 1}


# 4.6.3 셋 컴프리헨션

a_set = {number for number in range(1,6) if number % 3 == 1}
a_set
# {1, 4}


# 4.6.4 제너레이터 컴프리헨션

number_thing = (number for number in range(1, 6))


type(number_thing)
# <class 'generator'>


for number in number_thing:
    print(number)

# 1
# 2
# 3
# 4
# 5


number_thing = (number for number in range(1, 6))
number_list = list(number_thing)
number_list
# [1, 2, 3, 4, 5]


try_again = list(number_thing)
try_again
# []
