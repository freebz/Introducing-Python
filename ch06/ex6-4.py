# 6.5 메서드 추가하기

class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    def exclaim(self):
        print("I'm a Yugo! Much like a Car, but more Yugo-ish.")
    def need_a_push(self):
        print("A little help here?")


give_me_a_car = Car()
give_me_a_yugo = Yugo()


give_me_a_yugo.need_a_push()
# A little help here?


give_me_a_car.need_a_push()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Car' object has no attribute 'need_a_push'
