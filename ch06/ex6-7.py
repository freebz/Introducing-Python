# 6.8 get/set 속성값과 프로퍼티

class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    def get_name(self):
        print('inside the getter')
        return self.hidden_name
    def set_name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name
    name = property(get_name, set_name)


fowl = Duck('Howard')
fowl.name
# inside the getter
# 'Howard'


fowl.get_name()
# inside the getter
# 'Howard'


fowl.name = 'Daffy'
# inside the setter
fowl.name
# inside the getter
# 'Daffy'


fowl.set_name('Daffy')
# inside the setter
fowl.name
# inside the getter
# 'Daffy'


class Duck():
    def __init__(self, input_name):
        self.hidden_name = input_name
    @property
    def name(self):
        print('inside the getter')
        return self.hidden_name
    @name.setter
    def name(self, input_name):
        print('inside the setter')
        self.hidden_name = input_name


fowl = Duck('Howard')
fowl.name
# inside the getter
# 'Howard'
fowl.name = 'Donald'
# inside the setter
fowl.name
# inside the getter
# 'Donald'


class Circle():
    def __init__(self, radius):
        self.radius = radius
    @property
    def diameter(self):
        return 2 * self.radius


c = Circle(5)
c.radius
# 5


c.diameter
# 10


c.radius = 7
c.diameter
# 14


c.diameter = 20
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: can't set attribute
