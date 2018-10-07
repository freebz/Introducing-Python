# 4.9 데커레이터

def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function


def add_ints(a, b):
    return a + b

add_ints(3, 5)
# 8
cooler_add_ints = document_it(add_ints) # 데커레이터를 수동으로 할당
cooler_add_ints(3, 5)
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8
# 8


@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8
# 8


def square_it(func):
    def new_function(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * result
    return new_function


@document_it
@square_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)
# Running function: new_function
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 64
# 64


@square_it
@document_it
def add_ints(a, b):
    return a + b

add_ints(3, 5)
# Running function: add_ints
# Positional arguments: (3, 5)
# Keyword arguments: {}
# Result: 8
# 64
