# 6.14 클래스와 객체, 그리고 모듈은 언제 사용할까?

# 6.14.1 네임드 튜플

from collections import namedtuple

Duck = namedtuple('Duck', 'bill tail')
duck = Duck('wide orange', 'long')
duck
# Duck(bill='wide orange', tail='long')
duck.bill
# 'wide orange'
duck.tail
# 'long'


parts = {'bill': 'wide orange', 'tail': 'long'}
duck2 = Duck(**parts)
duck2
# Duck(bill='wide orange', tail='long')


duck3 = duck2._replace(tail='magnificent', bill='crushing')
duck3
# Duck(bill='crushing', tail='magnificent')


duck_dict = {'bill': 'wide orange', 'tail': 'long'}
duck_dict
# {'bill': 'wide orange', 'tail': 'long'}


duck_dict['color'] = 'green'
duck_dict
# {'bill': 'wide orange', 'tail': 'long', 'color': 'green'}


duck.color = 'green'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'Duck' object has no attribute 'color'
