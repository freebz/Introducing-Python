# 6.1 객체란 무엇인가?

# 6.2 클래스 선언하기: class

class Person():
    pass


someone = Person()


class Person():
    def __init__(self):
        pass


class Person():
    def __init__(self, name):
        self.name = name


hunter = Person('Elmer Fudd')


print('The mighty hunter: ', hunter.name)
# The mighty hunter:  Elmer Fudd
