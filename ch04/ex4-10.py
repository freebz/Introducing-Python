# 4.10 네임스페이스와 스코프

animal = 'fruitbat'
def print_global():
    print('inside print_global:', animal)

print('at the top level:', animal)
# at the top level: fruitbat
print_global()
# inside print_global: fruitbat


def change_and_print_global():
    print('inside change_and_print_global:', animal)
    animal = 'wombat'
    print('after the change:', animal)

change_and_print_global()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in change_and_print_global
# UnboundLocalError: local variable 'animal' referenced before assignment


def change_local():
    animal = 'wombat'
    print('inside change_local:', animal, id(animal))

change_local()
# inside change_local: wombat 139931630539696
animal
# 'fruitbat'
id(animal)
# 139931576643376


animal = 'fruitbat'
def change_and_print_global():
    global animal
    animal = 'wombat'
    print('inside change_and_print_global:', animal)
    
animal
# 'fruitbat'
change_and_print_global()
# inside change_and_print_global: wombat
animal
# 'wombat'


animal = 'fruitbat'
def change_local():
    animal = 'wombat'  # 지역 변수
    print('locals:', locals())

animal
# 'fruitbat'
change_local()
# locals: {'animal': 'wombat'}
print('globals:', globals())  # 보여주기 위한 작은 출력 포맷
# globals: {'animal': 'fruitbat',
#           '__doc__': None,
#           'change_local': <function change_it at 0x1006c0170>,
#           '__package__': None,
#           '__name__': '__main__',
#           '__loader__': <<class '_frozen_importlib.BuiltinImporter'>,
#           '__builtins__': <module 'builtins'>}
animal
# 'fruitbat'


# 4.10.1 이름에 _와 __사용

def amazing():
    '''This is the amazing function.
    Want to see it again?'''
    print('This function is named:', amazing.__name__)
    print('And its docstring is:', amazing.__doc__)

amazing()
# This function is named: amazing
# And its docstring is: This is the amazing function.
#     Want to see it again?
