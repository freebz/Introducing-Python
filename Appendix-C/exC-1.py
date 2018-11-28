# C.1 수학 및 통계의 표준 라이브러리

# C.1.1 수학 함수

import math
math.pi
# 3.141592653589793
math.e
# 2.718281828459045


math.fabs(98.6)
# 98.6
math.fabs(-271.1)
# 271.1


math.floor(98.6)
# 98
math.floor(-271.1)
# -272
math.ceil(98.6)
# 99
math.ceil(-271.1)
# -271


math.factorial(0)
# 1
math.factorial(1)
# 1
math.factorial(2)
# 2
math.factorial(3)
# 6
math.factorial(10)
# 3628800


math.log(1.0)
# 0.0
math.log(math.e)
# 1.0


math.log(8, 2)
# 3.0


math.pow(2, 3)
# 8.0


2**3
# 8
2.0**3
# 8.0


math.sqrt(100.0)
# 10.0


math.sqrt(-100.0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ValueError: math domain error


x = 3.0
y = 4.0
math.hypot(x, y)
# 5.0


math.sqrt(x*x + y*y)
# 5.0
math.sqrt(x**2 + y**2)
# 5.0


math.radians(180.0)
# 3.141592653589793
math.degrees(math.pi)
# 180.0


# C.1.2 복소수 계산

# 실수
5
# 허수
8j
# 허수
3 + 2j
# (3+2j)


1j * 1j
# (-1+0j)
(7 + 1j) * 1j
# (-1+7j)


# C.1.3 정확한 부동소수점수 계산하기: decimal

x = 10.0 / 3.0
x
# 3.3333333333333335


from decimal import Decimal
price = Decimal('19.99')
tax = Decimal('0.06')
total = price + (price * tax)
total
# Decimal('21.1894')


penny = Decimal('0.01')
total.quantize(penny)
# Decimal('21.19')


# C.1.4 유리수 계산하기: fractions

from fractions import Fraction
Fraction(1, 3) * Fraction(2, 3)
# Fraction(2, 9)


Fraction(1.0/3.0)
# Fraction(6004799503160661, 18014398509481984)
Fraction(Decimal('1.0')/Decimal('3.0'))
# Fraction(3333333333333333333333333333, 10000000000000000000000000000)


# C.1.5 팩 시퀀스 사용하기: array

# C.1.6 간단한 통계 처리하기: statics

# C.1.7 행렬 곱하기
