# 3.5 셋

# 3.5.1 셋 생성하기: set()

empty_set = set()
empty_set
# set()
even_numbers = {0, 2, 4, 6, 8}
even_numbers
# {0, 2, 4, 6, 8}
odd_numbers = {1, 3, 5, 7, 9}
odd_numbers
# {1, 3, 5, 7, 9}


# 3.5.2 데이터 타입 변환하기: set()

set( 'letters' )
# {'t', 'l', 's', 'e', 'r'}


set( ['Dasher', 'Dancer', 'Prancer', 'Mason-Dixon'] )
# {'Dancer', 'Dasher', 'Prancer', 'Mason-Dixon'}


set( ('Ummagumma', 'Echoes', 'Atom Heart Mother') )
# {'Atom Heart Mother', 'Ummagumma', 'Echoes'}


set( {'apple': 'red', 'orange': 'orange', 'cheery': 'red'} )
# {'cheery', 'apple', 'orange'}


# 3.5.3 in으로 값 멤버십 테스트하기

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
    }


for name, contents in drinks.items():
    if 'vodka' in contents:
        print(name)

# martini
# black russian
# white russian
# screwdriver


for name, contents in drinks.items():
    if 'vodka' in contents and not ('vermouth' in contents or
                                    'cream' in contents):
        print(name)

# black russian
# screwdriver


# 3.5.4 콤비네이션과 연산자

for name, contents in drinks.items():
    if contents & {'vermouth', 'orange juice'}:
        print(name)

# martini
# manhattan
# screwdriver


for name, contents in drinks.items():
    if 'vodka' in contents and not contents & {'vermouth', 'cream'}:
        print(name)

# black russian
# screwdriver


bruss = drinks['black russian']
wruss = drinks['white russian']


a = {1, 2}
b = {2, 3}


a & b
# {2}
a.intersection(b)
# {2}


bruss & wruss
# {'kahlua', 'vodka'}


a | b
# {1, 2, 3}
a.union(b)
# {1, 2, 3}


bruss | wruss
# {'vodka', 'cream', 'kahlua'}


a - b
# {1}
a.difference(b)
# {1}
bruss - wruss
# set()
wruss - bruss
# {'cream'}


a ^ b
# {1, 3}
a.symmetric_difference(b)
# {1, 3}


bruss ^ wruss
# {'cream'}


a <= b
# False
a.issubset(b)
# False


bruss <= wruss
# True


a <= a
# True
a.issubset(a)
# True


a < b
# False
a < a
# False
bruss < wruss
# True


a >= b
# False
a.issuperset(b)
# False
wruss >= bruss
# True


a >= a
# True
a.issuperset(a)
# True


a > b
# False
wruss > bruss
# True
