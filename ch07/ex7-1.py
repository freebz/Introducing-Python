# 7.1 텍스트 문자열

# 7.1.1 유니코드

# 파이썬 3 유니코드 문자열

def unicode_test(value):
    import unicodedata
    name = unicodedata.name(value)
    value2 = unicodedata.lookup(name)
    print('value="%s", name="%s", value2="%s"' % (value, name, value2))


unicode_test('A')
# value="A", name="LATIN CAPITAL LETTER A", value2="A"


unicode_test('$')
# value="$", name="DOLLAR SIGN", value2="$"


unicode_test('\u00a2')
# value="¢", name="CENT SIGN", value2="¢"


unicode_test('\u20ac')
# value="€", name="EURO SIGN", value2="€"


unicode_test('\u2603')
# value="☃", name="SNOWMAN", value2="☃"


place = 'café'
place
# 'café'


unicodedata.name('\u00e9')
# 'LATIN SMALL LETTER E WITH ACUTE'


unicodedata.lookup('E WITH ACUTE, LATIN SMALL LETTER')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# KeyError: "undefined character name 'E WITH ACUTE, LATIN SMALL LETTER'"


place = 'caf\u00e9'
place
# 'café'
place = 'caf\N{LATIN SMALL LETTER E WITH ACUTE}'
place
# 'café'


u_umlaut = '\N{LATIN SMALL LETTER U WITH DIAERESIS}'
u_umlaut
# 'ü'
drink = 'Gew' + u_umlaut + 'rztraminer'
print('Now I can finally have my', drink, 'in a', place)
# Now I can finally have my Gewürztraminer in a café


len('$')
# 1
len('\U0001f47b')
# 1


# UTF-8 인코딩과 디코딩

# 인코딩

snowman = '\u2603'


len(snowman)
# 1


ds = snowman.encode('utf-8')


len(ds)
# 3
ds
# b'\xe2\x98\x83'


ds = snowman.encode('ascii')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# UnicodeEncodeError: 'ascii' codec can't encode character '\u2603' in position 0: ordinal not in range(128)


snowman.encode('ascii', 'ignore')
# b''


snowman.encode('ascii', 'replace')
# b'?'


snowman.encode('ascii', 'backslashreplace')
# b'\\u2603'


snowman.encode('ascii', 'xmlcharrefreplace')
# b'&#9731;'


# 디코딩

place = 'caf\u00e9'
place
# 'café'
type(place)
# <class 'str'>


place_bytes = place.encode('utf-8')
place_bytes
# b'caf\xc3\xa9'
type(place_bytes)
# <class 'bytes'>


place2 = place_bytes.decode('utf-8')
place2
# 'café'


place3 = place_bytes.decode('ascii')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# UnicodeDecodeError: 'ascii' codec can't decode byte 0xc3 in position 3: ordinal not in range(128)


place4 = place_bytes.decode('latin-1')
place4
# 'cafÃ©'
place5 = place_bytes.decode('windows-1252')
place5
# 'cafÃ©'


# 7.1.2 포맷

# 옛 스타일: %

'%s' % 42
# '42'
'%d' % 42
# '42'
'%x' % 42
# '2a'
'%o' % 42
# '52'


'%s' % 7.03
# '7.03'
'%f' % 7.03
# '7.030000'
'%e' % 7.03
# '7.030000e+00'
'%g' % 7.03
# '7.03'


'%d%%' % 100
# '100%'


actor = 'Richard Gere'
cat = 'Chester'
weight = 28
"My wife's favorite actor is %s" % actor
# "My wife's favorite actor is Richard Gere"

"Our cat %s weighs %s pounds" % (cat, weight)
# 'Our cat Chester weighs 28 pounds'


n = 42
f = 7.03
s = 'string cheese'


'%d %f %s' % (n, f, s)
# '42 7.030000 string cheese'


'%10d %10f %10s' % (n, f, s)
# '        42   7.030000 string cheese'


'%-10d %-10f %-10s' % (n, f, s)
# '42         7.030000   string cheese'


'%10.4d %10.4f %10.4s' % (n, f, s)
# '      0042     7.0300       stri'


'%.4d %.4f %.4s' % (n, f, s)
# '0042 7.0300 stri'


'%*.*d %*.*f %*.*s' % (10, 4, n, 10, 4, f, 10, 4, s)
# '      0042     7.0300       stri'


# 새로운 스타일의 포매팅: {}와 format

'{} {} {}'.format(n, f, s)
# '42 7.03 string cheese'


'{2} {0} {1}'.format(f, s, n)
# '42 7.03 string cheese'


'{n} {f} {s}'.format(n=42, f=7.03, s='string cheese')
# '42 7.03 string cheese'


d = {'n': 42, 'f': 7.03, 's': 'string cheese'}


'{0[n]} {0[f]} {0[s]} {1}'.format(d, 'other')
# '42 7.03 string cheese other'


'{0:d} {1:f} {2:s}'.format(n, f, s)
# '42 7.030000 string cheese'


'{n:d} {f:f} {s:s}'.format(n=42, f=7.03, s='string cheese')
# '42 7.030000 string cheese'


'{0:10d} {1:10f} {2:10s}'.format(n, f, s)
# '        42   7.030000 string cheese'


'{0:>10d} {1:>10f} {2:>10s}'.format(n, f, s)
# '        42   7.030000 string cheese'


'{0:<10d} {1:<10f} {2:<10s}'.format(n, f, s)
# '42         7.030000   string cheese'


'{0:^10d} {1:^10f} {2:^10s}'.format(n, f, s)
# '    42      7.030000  string cheese'


'{0:>10.4d} {1:>10.4f} {2:10.4s}'.format(n, f, s)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: Precision not allowed in integer format specifier


'{0:>10d} {1:>10.4f} {2:>10.4s}'.format(n, f, s)
# '        42     7.0300       stri'


'{0:!^20s}'.format('BIG SALE')
# '!!!!!!BIG SALE!!!!!!'


# 7.1.3 정규표현식

result = re.match('You', 'Young Frankenstein')


youpattern = re.compile('You')


result = youpattern.match('Young Frankenstein')


# 시작부터 일치하는 패턴 찾기: match()

import re
source = 'Young Frankenstein'
m = re.match('You', source)  # match는 소스의 시작부터 패턴이 일치하는지 확인한다.
if m:  # match는 객체를 반환한다. 무엇이 일치하는지 보기 위해 다음 작업을 수행한다.
    print(m.group())

# You
m = re.match('^You', source)  # 문자열이 You로 시작하는지 확인한다.
if m:
    print(m.group())

# You


m = re.match('Frank', source)
if m:
    print(m.group())
    
#


m = re.search('Frank', source)
if m:
    print(m.group())

# Frank


m = re.match('.*Frank', source)
if m:  # match는 객체를 반환한다.
    print(m.group())

# Young Frank


# 첫 번째 일치하는 패턴 찾기: search()

m = re.search('Frank', source)
if m:  # search는 객체를 반환한다.
    print(m.group())

# Frank


# 일치하는 모든 패턴 찾기: findall()

m = re.findall('n', source)
m  # findall은 리스트를 반환한다.
# ['n', 'n', 'n', 'n']
print('Found', len(m), 'matches')
# Found 4 matches


m = re.findall('n.', source)
m
# ['ng', 'nk', 'ns']


m = re.findall('n.?', source)
m
# ['ng', 'nk', 'ns', 'n']


# 패턴으로 나누기: split()

m = re.split('n', source)
m  # split은 리스트를 반환한다.
# ['You', 'g Fra', 'ke', 'stei', '']


# 일치하는 패턴 대체하기: sub()

m = re.sub('n', '?', source)
m  # sub는 문자열을 반환한다.
# 'You?g Fra?ke?stei?'


# 패턴: 특수 문자

import string
printable = string.printable
len(printable)
# 100
printable[0:50]
# '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN'
printable[50:]
# 'OPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'


re.findall('\d', printable)
$ ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


re.findall('\w', printable)
# ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '_']


re.findall('\s', printable)
# [' ', '\t', '\n', '\r', '\x0b', '\x0c']


x = 'abc' + '-/*' + '\u00ea' + '\u0115'


re.findall('\w', x)
# ['a', 'b', 'c', 'ê', 'ĕ']


# 패턴: 지정자

source = '''I wish I may, I wish I might
Have a dish of fish tonight.'''

re.findall('wish', source)
# ['wish', 'wish']


re.findall('wish|fish', source)
# ['wish', 'wish', 'fish']


re.findall('^wish', source)
# []


re.findall('^I wish', source)
# ['I wish']


re.findall('fish$', source)
# []


re.findall('fish tonight.$', source)
# ['fish tonight.']


re.findall('fish tonight\.$', source)
# ['fish tonight.']


re.findall('[wf]ish', source)
# ['wish', 'wish', 'fish']


re.findall('[wsh]+', source)
# ['w', 'sh', 'w', 'sh', 'h', 'sh', 'sh', 'h']


re.findall('ght\W', source)
# ['ght\n', 'ght.']


re.findall('I (?=wish)', source)
# ['I ', 'I ']


re.findall('(?<=I) wish', source)
# [' wish', ' wish']


re.findall('\bfish', source)
# []


re.findall(r'\bfish', source)
# ['fish']


# 패턴: 매칭 결과 지정하기

m = re.search(r'(. dish\b).*(\bfish)', source)
m.group()
# 'a dish of fish'
m.groups()
# ('a dish', 'fish')


m = re.search(r'(?P<DISH>. dish\b).*(?P<FISH>\bfish)', source)
m = group()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'group' is not defined
