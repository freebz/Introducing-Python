# 6.10 메서드 타입

class A():
    count = 0
    def __init__(self):
        A.count += 1
    def exclaim(self):
        print("I'm an A!")
    @classmethod
    def kids(cls):
        print("A has", cls.count, "little objects.")

easy_a = A()
breezy_a = A()
wheezy_a = A()
A.kids()
# A has 3 little objects.


class CoyoteWeapon():
    @staticmethod
    def commercial():
        print('This CoyoteWeapon has been brought to you by Acme')

CoyoteWeapon.commercial()
# This CoyoteWeapon has been brought to you by Acme
