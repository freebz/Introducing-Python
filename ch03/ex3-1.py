# CHAPTER 3 파이 채우기: 리스트, 튜플, 딕셔너리, 셋

# 3.1 리스트와 튜플

# 3.2 리스트

# 3.2.1 리스트 생성하기: [] 또는 list()

empty_list = []
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
big_birds = ['emu', 'ostrich', 'cassowary']
first_names = ['Graham', 'John', 'Terry', 'Terry', 'Michael']


another_empty_list = list()
another_empty_list
# []


# 3.2.2 다른 데이터 타입을 리스트로 변환하기: list()

list('cat')
# ['c', 'a', 't']


a_tuple = ('ready', 'fire', 'aim')
list(a_tuple)
# ['ready', 'fire', 'aim']


birthday = '1/6/1952'
birthday.split('/')
# ['1', '6', '1952']


splitme = 'a/b//c/d///e'
splitme.split('/')
# ['a', 'b', '', 'c', 'd', '', '', 'e']

splitme = 'a/b//c/d///e'
splitme.split('//')
# ['a/b', 'c/d', '/e']


# 3.2.3 [offset]으로 항목 얻기

marxes = ['Groucho', 'Chico', 'Harpo']
marxes[0]
# 'Groucho'
marxes[1]
# 'Chico'
marxes[2]
# 'Harpo'


marxes[-1]
# 'Harpo'
marxes[-2]
# 'Chico'
marxes[-3]
# 'Groucho'


# 3.2.4 리스트의 리스트

small_birds = ['hummingbird', 'finch']
extinct_birds = ['dodo', 'passenger pigeon', 'Norwegian Blue']
carol_birds = [3, 'French hens', 2, 'turtledoves']
all_birds = [small_birds, extinct_birds, 'macaw', carol_birds]


all_birds
# [['hummingbird', 'finch'], ['dodo', 'passenger pigeon', 'Norwegian Blue'], 'macaw', [3, 'French hens', 2, 'turtledoves']]


all_birds[0]
# ['hummingbird', 'finch']


all_birds[1]
# ['dodo', 'passenger pigeon', 'Norwegian Blue']

all_birds[1][0]
# 'dodo'


# 3.2.5 [offset]으로 항목 바꾸기

marxes = ['Groucho', 'Chico', 'Harpo']
marxes[2] = 'Wanda'
marxes
# ['Groucho', 'Chico', 'Wanda']


# 3.2.6 슬라이스로 항목 추출하기

marxes = ['Groucho', 'Chico', 'Harpo']
marxes[0:2]
# ['Groucho', 'Chico']


marxes[::2]
# ['Groucho', 'Harpo']


marxes[::-1]
# ['Harpo', 'Chico', 'Groucho']


# 3.2.7 리스트의 끝에 항목 추가하기: append()

marxes.append('Zeppo')
marxes
# ['Groucho', 'Chico', 'Harpo', 'Zeppo']


# 3.2.8 리스트 병합하기: extend() 또는 +=

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.extend(others)
marxes
# ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']


marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes += others
marxes
# ['Groucho', 'Chico', 'Harpo', 'Zeppo', 'Gummo', 'Karl']


marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
others = ['Gummo', 'Karl']
marxes.append(others)
marxes
# ['Groucho', 'Chico', 'Harpo', 'Zeppo', ['Gummo', 'Karl']]


# 3.2.9 오프셋과 insert()로 항목 추가하기

marxes.insert(3, 'Gummo')
marxes
# ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']

marxes.insert(10, 'Karl')
marxes
# ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo', 'Karl']


# 3.2.10 오프셋으로 항목 삭제하기: del

del marxes[-1]
marxes
# ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']


marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
marxes[2]
# 'Harpo'
del marxes[2]
marxes
# ['Groucho', 'Chico', 'Gummo', 'Zeppo']
marxes[2]
# 'Gummo'


# 3.2.11 값으로 항목 삭제하기: remove()

marxes = ['Groucho', 'Chico', 'Harpo', 'Gummo', 'Zeppo']
marxes.remove('Gummo')
marxes
# ['Groucho', 'Chico', 'Harpo', 'Zeppo']


# 3.2.12 오프셋으로 항목을 얻은 후 삭제하기: pop()

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.pop()
# 'Zeppo'
marxes
# ['Groucho', 'Chico', 'Harpo']
marxes.pop(1)
# 'Chico'
marxes
# ['Groucho', 'Harpo']


# 3.2.13 값으로 항목 오프셋 찾기: index()

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
marxes.index('Chico')
# 1


# 3.2.14 존재여부 확인하기: in

marxes = ['Groucho', 'Chico', 'Harpo', 'Zeppo']
'Groucho' in marxes
# True
'Bob' in marxes
# False


words = ['a', 'deer', 'a', 'female', 'deer']
'deer' in words
# True


# 3.2.15 값 세기: count()

marxes = ['Groucho', 'Chico', 'Harpo']
marxes.count('Harpo')
# 1
marxes.count('Bob')
# 0

snl_skit = ['cheeseburger', 'cheeseburger', 'cheeseburger']
snl_skit.count('cheeseburger')
# 3


# 3.2.16 문자열로 변환하기: join()

marxes = ['Groucho', 'Chico', 'Harpo']
', '.join(marxes)
# 'Groucho, Chico, Harpo'


friends = ['Harry', 'Hermione', 'Ron']
separator = ' * '
joined = separator.join(friends)
joined
# 'Harry * Hermione * Ron'
separated = joined.split(separator)
separated
# ['Harry', 'Hermione', 'Ron']
separated == friends
# True


# 3.2.17 정렬하기: sort()

marxes = ['Groucho', 'Chico', 'Harpo']
sorted_marxes = sorted(marxes)
sorted_marxes
# ['Chico', 'Groucho', 'Harpo']


marxes
# ['Groucho', 'Chico', 'Harpo']


marxes.sort()
marxes
# ['Chico', 'Groucho', 'Harpo']


numbers = [2, 1, 4.0, 3]
numbers.sort()
numbers
# [1, 2, 3, 4.0]


numbers = [2, 1, 4.0, 3]
numbers.sort(reverse=True)
numbers
# [4.0, 3, 2, 1]


# 3.2.18 항목 개수 얻기: len()

marxes = ['Groucho', 'Chico', 'Harpo']
len(marxes)
# 3


# 3.2.19 할당: =, 복사: copy()

a = [1, 2, 3]
a
# [1, 2, 3]
b = a
b
# [1, 2, 3]
a[0] = 'surprise'
a
# ['surprise', 2, 3]


b
# ['surprise', 2, 3]


b
# ['surprise', 2, 3]
b[0] = 'I hate surprises'
b
# ['I hate surprises', 2, 3]
a
# ['I hate surprises', 2, 3]


a = [1, 2, 3]
b = a.copy()
c = list(a)
d = a[:]


a[0] = 'integer lists are boring'
a
# ['integer lists are boring', 2, 3]
b
# [1, 2, 3]
c
# [1, 2, 3]
d
# [1, 2, 3]
