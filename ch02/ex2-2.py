# 2.2 숫자

# 2.2.1 정수

5
# 5
0
# 0
05
#   File "<stdin>", line 1
#     05
#      ^
# SyntaxError: invalid token

123
# 123
+123
# 123

-123
# -123

5 + 9
# 14
100 - 7
# 93
4 - 10
# -6

5 + 9 + 3
# 17
4 + 3 - 2 - 1 + 6
# 10

5+9    +            3
# 17

6 * 7
# 42
7 * 6
# 42
6 * 7 * 2 * 3
# 252

9 / 5
# 1.8
9 // 5
# 1
5 / 0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero
7 // 0
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: integer division or modulo by zero

a = 95
a
# 95
a - 3
# 92

a
# 95
a = a - 3
a
# 92

a = 95
temp = a - 3
a = temp

a = a - 3

a = 95
a -= 3
a
# 92

a += 8
a
# 100

a *= 2
a
# 200

a /= 3
a
# 66.66666666666667

a = 13
a //= 4
a
# 3

9 % 5
# 4
divmod(9, 5)
# (1, 4)

9 // 5
# 1
9 % 5
# 4


# 2.2.2 우선순위

2 + 3 * 4
# 14

2 + (3 * 4)
# 14


# 2.2.3 진수

10
# 10

0b10
# 2

0o10
# 8

0x10
# 16


# 2.2.4 형변환

int(True)
# 1
int(False)
# 0

int(98.6)
# 98
int(1.0e4)
# 10000

int('99')
# 99
int('-23')
# -23
int('+12')
# 12

int(12345)
# 12345

int('99 bottles of beer on the wall')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '99 bottles of beer on the wall'
int('')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: ''

int('98.6')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '98.6'
int('1.0e4')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: invalid literal for int() with base 10: '1.0e4'

4 + 7.0
# 11.0

True + 2
# 3
False + 5.0
# 5.0


# 2.2.5 int의 크기

googol = 10 ** 100
googol
# 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
googol * googol
# 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000


# 2.2.6 부동소수점수

float(True)
# 1.0
float(False)
# 0.0

float(98)
# 98.0
float('99')
# 99.0

float('98.6')
# 98.6
float('-1.5')
# -1.5
float('1.0e4')
# 10000.0


# 2.2.7 수학 함수
