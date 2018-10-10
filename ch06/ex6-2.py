# 6.3 상속

class Car():
    pass

class Yugo(Car):
    pass


give_me_a_car = Car()
give_me_a_yugo = Yugo()


class Car():
    def exclaim(self):
        print("I'm a Car!")

class Yugo(Car):
    pass


give_me_a_car = Car()
give_me_a_yugo = Yugo()
give_me_a_car.exclaim()
# I'm a Car!
give_me_a_yugo.exclaim()
# I'm a Car!
