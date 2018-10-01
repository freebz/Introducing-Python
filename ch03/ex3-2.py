# 3.3 튜플

# 3.3.1 튜플 생성하기: ()

empty_tuple = ()
empty_tuple
# ()


one_marx = 'Groucho',
one_marx
# ('Groucho',)



marx_tuple = 'Groucho', 'Chico', 'Harpo'
marx_tuple
# ('Groucho', 'Chico', 'Harpo')


marx_tuple = ('Groucho', 'Chico', 'Harpo')
marx_tuple
# ('Groucho', 'Chico', 'Harpo')


marx_tuple = ('Groucho', 'Chico', 'Harpo')
a, b, c = marx_tuple
a
# 'Groucho'
b
# 'Chico'
c
# 'Harpo'


password = 'swordfish'
icecream = 'tuttifrutti'
password, icecream = icecream, password
password
# 'tuttifrutti'
icecream
# 'swordfish'


marx_list = ['Groucho', 'Chico', 'Harpo']
tuple(marx_list)
# ('Groucho', 'Chico', 'Harpo')


# 3.3.2 튜플과 리스트
