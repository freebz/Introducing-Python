# 2.3 문자열

# 2.3.1 인용 부호로 문자열 생성

'Snap'
# 'Snap'
"Crackle"
# 'Crackle'

"'Nay,' said the naysayer."
# "'Nay,' said the naysayer."
'The rare double quote in captivity: ".'
# 'The rare double quote in captivity: ".'
'A "tow by four" is actually 1 1/2" x 3 1/2".'
# 'A "tow by four" is actually 1 1/2" x 3 1/2".'
"'There's the man that shot my paw!' cried the limping hound."
# "'There's the man that shot my paw!' cried the limping hound."


'''Boom!'''
# 'Boom!'
"""Eek!"""
# 'Eek!'


poem = '''There was a Young Lady of Norway,
Who casually sat in a doorway;
When the door squeezed her flat,
She exclaimed, "What of that?"
This courageous Young Lady of Norway.'''


poem2 = '''I do not like thee, Doctor Fell.
    The reason why, I cannot tell.
    But this I know, and know full well:
    I do not like thee, Doctor Fell.
'''

print(poem2)
# I do not like thee, Doctor Fell.
#     The reason why, I cannot tell.
#     But this I know, and know full well:
#     I do not like thee, Doctor Fell.


poem2
# 'I do not like thee, Doctor Fell.\n    The reason why, I cannot tell.\n    But this I know, and know full well:\n    I do not like thee, Doctor Fell.\n'


print(99, 'bottles', 'would be enough.')
# 99 bottles would be enough.


''
# ''
""
# ''
''''''
# ''
""""""
# ''


bottles = 99
base = ''
base += 'current inventory: '
base += str(bottles)
base
# 'current inventory: 99'


# 2.3.2 데이터 타입 변환: str()

str(98.6)
# '98.6'
str(1.0e4)
# '10000.0'
str(True)
# 'True'


# 2.3.3 이스케이프 문자

palindrome = 'A man,\nA plan,\nA canal:\nPanama.'
print(palindrome)
# A man,
# A plan,
# A canal:
# Panama.


print('\tabc')
# 	abc
print('a\tbc')
# a	bc
print('ab\tc')
# ab	c
print('abc\t')
# abc	


testimony = "\"I did nothing!\" he said. \"Not that either! Or the other thing.\""
print(testimony)
# "I did nothing!" he said. "Not that either! Or the other thing."
fact = "The word's largest rubber duck was 54'2\" by 65'7\" by 105'"
print(fact)
# The word's largest rubber duck was 54'2" by 65'7" by 105'


speech = 'Today we honor our friend, the backslash: \\.'
print(speech)
# Today we honor our friend, the backslash: \.


# 2.3.4 결합: +

'Release the kraken! ' + 'At once!'
# 'Release the kraken! At once!'


"My word! " "A gentleman caller!"
# 'My word! A gentleman caller!'


a = 'Duck.'
b = a
c = 'Grey Duck!'
a + b + c
# 'Duck.Duck.Grey Duck!'
print(a, b, c)
# Duck. Duck. Grey Duck!


# 2.3.5 복제하기: *

start = 'Na ' * 4 + '\n'
middle = 'Hey ' * 3 + '\n'
end = 'Goodbye.'
print(start + start + middle + end)
# Na Na Na Na 
# Na Na Na Na 
# Hey Hey Hey 
# Goodbye.


# 2.3.6 문자 추출: []

letters = 'abcdefghijklmnopqrstuvwxyz'
letters[0]
# 'a'
letters[1]
# 'b'
letters[-1]
# 'z'
letters[-2]
# 'y'
letters[25]
# 'z'
letters[5]
# 'f'


letters[100]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: string index out of range


name = 'Henny'
name[0] = 'P'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'str' object does not support item assignment


name = 'Henny'
name.replace('H', 'P')
# 'Penny'
'P' + name[1:]
# 'Penny'


# 2.3.7 슬라이스: [start:end:step]

letters = 'abcdefghijklmnopqrstuvwxyz'

letters[:]
# 'abcdefghijklmnopqrstuvwxyz'

letters[20:]
# 'uvwxyz'

letters[10:]
# 'klmnopqrstuvwxyz'

letters[12:15]
# 'mno'

letters[-3:]
# 'xyz'

letters[18:-3]
# 'stuvw'

letters[-6:-2]
# 'uvwx'

letters[::7]
# 'ahov'

letters[4:20:3]
# 'ehknqt'

letters[19::4]
# 'tx'

letters[:21:5]
# 'afkpu'

letters[::-1]
# 'zyxwvutsrqponmlkjihgfedcba'

letters[-50:]
# 'abcdefghijklmnopqrstuvwxyz'

letters[-51:-50]
# ''

letters[:70]
# 'abcdefghijklmnopqrstuvwxyz'

letters[70:71]
# ''


# 2.3.8 문자열 길이: len()

len(letters)
# 26
empty = ""
len(empty)
# 0


# 2.3.9 문자열 나누기: split()

todos = 'get gloves, get mask,give cat vitamins, call abulance'
todos.split(',')
# ['get gloves', ' get mask', 'give cat vitamins', ' call abulance']

todos.split()
# ['get', 'gloves,', 'get', 'mask,give', 'cat', 'vitamins,', 'call', 'abulance']


# 2.3.10 문자열로 결합하기: join()

crypto_list = ['Yeti', 'Bigfoot', 'Loch Ness Monster']
crypto_string = ', '.join(crypto_list)
print('Found and signing book deals:', crypto_string)
# Found and signing book deals: Yeti, Bigfoot, Loch Ness Monster


# 2.3.11 문자열 다루기

poem = '''All that doth flow we cannot liquid name
Or else would fire and water be the same;
But that is liquid which is moist and wet
Fire that property can never get.
Then 'tis not cold that doth the fire put out
But 'tis the wet that makes it die, no doubt.'''

poem[:13]
# 'All that doth'

len(poem)
# 250

poem.startswith('All')
# True

poem.endswith('That\'s all, folks!')
# False

word = 'the'
poem.find(word)
# 73

poem.rfind(word)
# 214

poem.count(word)
# 3

poem.isalnum()
# False


# 2.3.12 대소문자와 배치

setup = 'a duck goes into a bar...'

setup.strip('.')
# 'a duck goes into a bar'

setup.capitalize()
# 'A duck goes into a bar...'

setup.title()
# 'A Duck Goes Into A Bar...'

setup.upper()
# 'A DUCK GOES INTO A BAR...'

setup.lower()
# 'a duck goes into a bar...'

setup.swapcase()
# 'a DUCK GOES INTO A BAR...'

setup.center(30)
# '  a duck goes into a bar...   '

setup.ljust(30)
# 'a duck goes into a bar...     '

setup.rjust(30)
# '     a duck goes into a bar...'


# 2.3.13 대체하기: replace()

setup.replace('duck', 'marmoset')
# 'a marmoset goes into a bar...'

setup.replace('a ', 'a famous ', 100)
# 'a famous duck goes into a famous bar...'

setup.replace('a', 'a famous', 100)
# 'a famous duck goes into a famous ba famousr...'
