# 6.6 부모에게 도움 받기: super

class Person():
    def __init__(self, name):
        self.name = name


class EmailPerson(Person):
    def __init__(self, name, email):
        super().__init__(name)
        self.email = email


bob = EmailPerson('Bob Frapples', 'bob@frapples.com')


bob.name
# 'Bob Frapples'
bob.email
# 'bob@frapples.com'
