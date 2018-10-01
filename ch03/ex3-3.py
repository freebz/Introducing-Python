# 3.4 딕셔너리

# 3.4.1 딕셔너리 생성하기: {}

empty_dict = {}
empty_dict
# {}


bierce = {
    "day": "A period of twenty-four hours, mostly misspent",
    "positive": "Mistaken at the top of one's voice",
    "misfortune": "The kind of fortune that never misses",
    }


bierce
# {'day': 'A period of twenty-four hours, mostly misspent', 'positive': "Mistaken at the top of one's voice", 'misfortune': 'The kind of fortune that never misses'}


# 3.4.2 딕셔너리로 변환하기: dict()

lol = [ ['a', 'b'], ['c', 'd'], ['e', 'f'] ]
dict(lol)
# {'a': 'b', 'c': 'd', 'e': 'f'}


lot = [ ('a', 'b'), ('c', 'd'), ('e', 'f') ]
dict(lot)
# {'a': 'b', 'c': 'd', 'e': 'f'}


tol = ( ['a', 'b'], ['c', 'd'], ['e', 'f'] )
dict(tol)
# {'a': 'b', 'c': 'd', 'e': 'f'}


los = [ 'ab', 'cd', 'ef' ]
dict(los)
# {'a': 'b', 'c': 'd', 'e': 'f'}


tos = ( 'ab', 'cd', 'df' )
dict(tos)
# {'a': 'b', 'c': 'd', 'd': 'f'}


# 3.4.3 항목 추가/변경하기: [key]

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
    }
pythons
# {'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael'}


pythons['Gillian'] = 'Gerry'
pythons
# {'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Gillian': 'Gerry'}


pythons['Gillian'] = 'Terry'
pythons
# {'Chapman': 'Graham', 'Cleese': 'John', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Gillian': 'Terry'}


some_pythons = {
    'Graham': 'Chapman',
    'John': 'Cleese',
    'Eric': 'Idle',
    'Terry': 'Gilliam',
    'Michael': 'Palin',
    'Terry': 'Jones',
    }
some_pythons
# {'Graham': 'Chapman', 'John': 'Cleese', 'Eric': 'Idle', 'Terry': 'Jones', 'Michael': 'Palin'}


# 3.4.4 딕셔너리 결합하기: update()

pythons = {
    'Chapman': 'Graham',
    'Cleese': 'John',
    'Gilliam': 'Terry',
    'Idle': 'Eric',
    'Jones': 'Terry',
    'Palin': 'Michael',
    }
pythons
# {'Chapman': 'Graham', 'Cleese': 'John', 'Gilliam': 'Terry', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael'}


others = { 'Marx': 'Groucho', 'Howard': 'Moe' }


pythons.update(others)
pythons
# {'Chapman': 'Graham', 'Cleese': 'John', 'Gilliam': 'Terry', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Marx': 'Groucho', 'Howard': 'Moe'}


first = {'a': 1, 'b': 2}
second = {'b': 'Platypus'}
first.update(second)
first
# {'a': 1, 'b': 'Platypus'}


# 3.4.5 키와 del로 항목 삭제하기

del pythons['Marx']
pythons
# {'Chapman': 'Graham', 'Cleese': 'John', 'Gilliam': 'Terry', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael', 'Howard': 'Moe'}
del pythons['Howard']
pythons
# {'Chapman': 'Graham', 'Cleese': 'John', 'Gilliam': 'Terry', 'Idle': 'Eric', 'Jones': 'Terry', 'Palin': 'Michael'}


# 3.4.6 모든 항목 삭제하기: clear()

pythons.clear()
pythons
# {}
pythons = {}
pythons
# {}


# 3.4.7 in으로 키 멤버십 테스트하기

pythons = {'Chapman': 'Graham', 'Cleese': 'John',
           'Jones': 'Terry', 'Palin': 'Michael'}


'Chapman' in pythons
# True
'Palin' in pythons
# True


'Gilliam' in pythons
# False


# 3.4.8 항목 얻기: [key]

pythons['Cleese']
# 'John'


pythons['Marx']
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: 'Marx'


pythons.get('Cleese')
# 'John'


pythons.get('Marx', 'Not a Python')
# 'Not a Python'


pythons.get('Marx')
#


# 3.4.9 모든 키 얻기: keys()

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
signals.keys()
# dict_keys(['green', 'yellow', 'red'])


list( signals.keys() )
# ['green', 'yellow', 'red']


# 3.4.10 모든 값 얻기: values()

list(signals.values())
# ['go', 'go faster', 'smile for the camera']


# 3.4.11 모든 쌍의 키-값 얻기: items()

list( signals.items() )
# [('green', 'go'), ('yellow', 'go faster'), ('red', 'smile for the camera')]


# 3.4.12 할당: =, 복사: copy()

signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
save_signals = signals
signals['blue'] = 'confuse everyone'
save_signals
# {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera', 'blue': 'confuse everyone'}


signals = {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
original_signals = signals.copy()
signals['blue'] = 'confuse everyone'
signals
# {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera', 'blue': 'confuse everyone'}
original_signals
# {'green': 'go', 'yellow': 'go faster', 'red': 'smile for the camera'}
