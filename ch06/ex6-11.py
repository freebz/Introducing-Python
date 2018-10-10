# 6.12 특수 메서드

class Word():
    def __init__(self, text):
        self.text = text

    def equals(self, word2):
        return self.text.lower() == word2.text.lower()


first = Word('ha')
second = Word('HA')
third = Word('eh')


first.equals(second)
# True


first.equals(third)
# False


class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()


first = Word('ha')
second = Word('HA')
third = Word('eh')
first == second
# True
first == third
# False


first = Word('ha')
first
# <__main__.Word object at 0x7f569f6ecdd8>
print(first)
# <__main__.Word object at 0x7f569f6ecdd8>


class Word():
    def __init__(self, text):
        self.text = text
    def __eq__(self, word2):
        return self.text.lower() == word2.text.lower()
    def __str__(self):
        return self.text
    def __repr__(self):
        return "Word('" + self.text + "')"

first = Word('ha')
first         # __repr__ 호출
# Word('ha')
print(first)  # __str__ 호출
# ha
