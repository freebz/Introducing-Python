# 4.7 함수

def do_nothing():
    pass


do_nothing()


def make_a_sound():
    print('quack')

make_a_sound()
# quack


def agree():
    return True


if agree():
    print('Splendid!')
else:
    print('That was unexpected.')

# Splendid!


def echo(anything):
    return anything + ' ' + anything


echo('Rumplestiltskin')
# 'Rumplestiltskin Rumplestiltskin'


def commentary(color):
    if color == 'red':
        return "It's a tomato."
    elif color == "green":
        return "It's a green pepper."
    elif color == 'bee purple':
        return "I don't know what it is, but only bees can see it."
    else:
        return "I've never heard of the color " + color + "."


comment = commentary('blue')


print(comment)
# I've never heard of the color blue.


print(do_nothing())
# None


# 유용한 None

thing = None
if thing:
    print("It's some thing")
else:
    print("It's no thing")

# It's no thing


if thing is None:
    print("It's nothing")
else:
    print("It's something")

# It's nothing


def is_none(thing):
    if thing is None:
        print("It's None")
    elif thing:
        print("It's True")
    else:
        print("It's False")


is_none(None)
# It's None
is_none(True)
# It's True
is_none(False)
# It's False
is_none(0)
# It's False
is_none(0.0)
# It's False
is_none(())
# It's False
is_none([])
# It's False
is_none({})
# It's False
is_none(set())
# It's False


# 4.7.1 위치 인자

def menu(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

menu('chardonnay', 'chicken', 'cake')
# {'wine': 'chardonnay', 'entree': 'chicken', 'dessert': 'cake'}


menu('beef', 'bagel', 'bordeaus')
# {'wine': 'beef', 'entree': 'bagel', 'dessert': 'bordeaus'}


# 4.7.2 키워드 인자

menu(entree='beef', dessert='bagel', wine='bordeaux')
# {'wine': 'bordeaux', 'entree': 'beef', 'dessert': 'bagel'}


menu('frontenac', dessert='flan', entree='fish')
# {'wine': 'frontenac', 'entree': 'fish', 'dessert': 'flan'}


# 4.7.3 기본 매개변수값 지정하기

def menu(wine, entree, dessert='pudding'):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}


menu('charonnay', 'chicken')
# {'wine': 'charonnay', 'entree': 'chicken', 'dessert': 'pudding'}


def buggy(arg, result=[]):
    result.append(arg)
    print(result)

buggy('a')
# ['a']
buggy('b') # expect['b']
# ['a', 'b']


def works(arg):
    result = []
    result.append(arg)
    return result

works('a')
# ['a']
works('b')
# ['b']


def nonbuggy(arg, result=None):
    if result is None:
        result = []
    result.append(arg)
    print(result)

nonbuggy('a')
# ['a']
nonbuggy('b')
# ['b']


# 4.7.4 위치 인자 모으기: *

def print_args(*args):
    print('Positional argument tuple:', args)


print_args()
# Positional argument tuple: ()


print_args(3, 2, 1, 'wait!', 'uh...')
# Positional argument tuple: (3, 2, 1, 'wait!', 'uh...')


def print_more(required1, required2, *args):
    print('Need this one:', required1)
    print('Need this one too:', required2)
    print('All the rest:', args)

print_more('cap', 'gloves', 'scarf', 'monocle', 'mustache wax')
# Need this one: cap
# Need this one too: gloves
# All the rest: ('scarf', 'monocle', 'mustache wax')


# 4.7.5 키워드 인자 모으기: **

def print_kwargs(**kwargs):
    print('Keyword arguments:', kwargs)


print_kwargs(wine='merlog', netree='mutton', dessert='macaroon')
# Keyword arguments: {'wine': 'merlog', 'netree': 'mutton', 'dessert': 'macaroon'}


# 4.7.6 docstring

def echo(anything):
    'echo returns its input argument'
    return anything


def print_if_true(thing, check):
    '''
    Prints the first argument if a second argument is true.
    The operations is:
        1. Check whether the *second* argument is true.
        2. If it is, print the *first* argument.
    '''
    if check:
        print(thing)


help(echo)
# Help on function echo in module __main__:
#     echo(anything)
#     echo returns its input argument


print(echo.__doc__)
# echo returns its input argument


# 4.7.7 일등 시민: 함수

def answer():
    print(42)


answer()
# 42


def run_something(func):
    func()


run_something(answer)
# 42


type(run_something)
# <class 'function'>


def add_args(arg1, arg2):
    print(arg1 + arg2)


type(add_args)
# <class 'function'>


def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)


run_something_with_args(add_args, 5, 9)
# 14


def sum_args(*args):
    return sum(args)


def run_with_positional_args(func, *args):
    return func(*args)


run_with_positional_args(sum_args, 1, 2, 3, 4)
# 10


# 4.7.8 내부 함수

def outer(a, b):
    def inner(c, d):
        return c + d
    return inner(a, b)

outer(4, 7)
# 11


def knights(saying):
    def inner(quote):
        return "We are the knights who say: '%s'" % quote
    return inner(saying)

knights('Ni!')
# "We are the knights who say: 'Ni!'"


# 4.7.9 클로저

def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" %saying
    return inner2


a = knights2('Duck')
b = knights2('Hasenpfeffer')


type(a)
# <class 'function'>
type(b)
# <class 'function'>


a
# <function knights2.<locals>.inner2 at 0x7f84eee5e400>
b
# <function knights2.<locals>.inner2 at 0x7f84eee5e488>


a()
# "We are the knights who say: 'Duck'"
b()
# "We are the knights who say: 'Hasenpfeffer'"


# 4.7.10 익명 함수: lambda()

def edit_story(words, func):
    for word in words:
        print(func(word))


stairs = ['thud', 'meow', 'thud', 'hiss']


def enliven(word): # 첫 글자를 대문자로 만들고 느낌표 붙이기
    return word.capitalize() + '!'



edit_story(stairs, enliven)
# Thud!
# Meow!
# Thud!
# Hiss!


edit_story(stairs, lambda word: word.capitalize() + '!')
# Thud!
# Meow!
# Thud!
# Hiss!
