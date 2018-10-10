# 6.4 메서드 오버라이드

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")


give_me_a_car = Car()
give_me_a_yugo = Yugo()


give_me_a_car.exclaim()
# I'm a Car!
give_me_a_yugo.exclaim()
# I'm a Yugo! Much like a Car, but more Yugo-ish.


class Person():
    def __init__(self, name):
        self.name = name

class MDPerson(Person):
    def __init__(self, name):
        self.name = "Doctor " + name

class JDPerson(Person):
    def __init__(self, name):
        self.name = name + ", Esquire"


person = Person('Fudd')
doctor = MDPerson('Fudd')
lawyer = JDPerson('Fudd')
print(person.name)
# Fudd
print(doctor.name)
# Doctor Fudd
print(lawyer.name)
# Fudd, Esquire
