# 6.9 private 네임 맹글링

class Duck():
    def __init__(self, input_name):
        self.__name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.__name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.__name = input_name


fowl = Duck('Howard')
fowl.name
# inside the getter
# 'Howard'
fowl.name = 'Donald'
# inside the setter
fowl.name
# inside the getter
# 'Donald'


fowl.__name
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Duck' object has no attribute '__name'


fowl._Duck__name
# 'Donald'
