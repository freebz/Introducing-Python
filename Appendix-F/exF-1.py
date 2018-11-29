# F.1 연산자 우선순위

# F.2 문자열 메서드

s = "OH, my paws and whiskers!"
t = "I'm late!"


# F.2.1 대소문자 변경

s.capitalize()
# 'Oh, my paws and whiskers!'
s.lower()
# 'oh, my paws and whiskers!'
s.swapcase()
# 'oh, MY PAWS AND WHISKERS!'
s.title()
# 'Oh, My Paws And Whiskers!'
s.upper()
# 'OH, MY PAWS AND WHISKERS!'


# F.2.2 검색

s.count('w')
# 2
s.find('w')
# 9
s.index('w')
# 9
s.rfind('w')
# 16
s.rindex('w')
# 16
s.startswith('OH')
# True


# F.2.3 수정

''.join(s)
# 'OH, my paws and whiskers!'
' '.join(s)
# 'O H ,   m y   p a w s   a n d   w h i s k e r s !'
' '.join((s, t))
# "OH, my paws and whiskers! I'm late!"
s.lstrip('HO')
# ', my paws and whiskers!'
s.replace('H', 'MG')
# 'OMG, my paws and whiskers!'
s.rsplit()
# ['OH,', 'my', 'paws', 'and', 'whiskers!']
s.rsplit(' ',   1)
# ['OH, my paws and', 'whiskers!']
s.split()
# ['OH,', 'my', 'paws', 'and', 'whiskers!']
s.split(' ')
# ['OH,', 'my', 'paws', 'and', 'whiskers!']
s.splitlines()
# ['OH, my paws and whiskers!']
s.strip()
# 'OH, my paws and whiskers!'
s.strip('s!')
# 'OH, my paws and whisker'


# F.2.4 정렬

s.center(30)
# '  OH, my paws and whiskers!   '
s.expandtabs()
# 'OH, my paws and whiskers!'
s.ljust(30)
# 'OH, my paws and whiskers!     '
s.rjust(30)
# '     OH, my paws and whiskers!'


# F.2.5 문자열 타입

s.isalnum()
# False
s.isalpha()
# False
s.isprintable()
# True
s.istitle()
# False
s.isupper()
# False
s.isdecimal()
# False
s.isnumeric()
# False

# F.3 문자열 모듈 속성
