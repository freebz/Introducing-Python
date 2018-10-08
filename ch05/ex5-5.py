# 5.5 파이썬 표준 라이브러리

# 5.5.1 누락된 키 처리하기: setdefault(), defaultdict()

periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)
# {'Hydrogen': 1, 'Helium': 2}


carbon = periodic_table.setdefault('Carbon', 12)
carbon
# 12
periodic_table
# {'Hydrogen': 1, 'Helium': 2, 'Carbon': 12}
helium = periodic_table.setdefault('Helium', 947)
helium
# 2
periodic_table
# {'Hydrogen': 1, 'Helium': 2, 'Carbon': 12}


from collections import defaultdict
periodic_table = defaultdict(int)


periodic_table['Hydrogen'] = 1
periodic_table['Lead']
# 0
periodic_table
# defaultdict(<class 'int'>, {'Hydrogen': 1, 'Lead': 0})


from collections import defaultdict

def no_idea():
    return 'Huh?'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'
bestiary['A']
# 'Abominable Snowman'
bestiary['B']
# 'Basilisk'
bestiary['C']
# 'Huh?'


bestiary = defaultdict(lambda: 'Huh?')
bestiary['E']
# 'Huh?'


from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)

# spam 3
# eggs 1



dict_counter = {}
for food in ['spam', 'spam', 'eggs', 'spam']:
    if not food in dict_counter:
        dict_counter[food] = 0
    dict_counter[food] += 1

for food, count in dict_counter.items():
    print(food, count)

# spam 3
# eggs 1


# 5.5.2 항목 세기: Counter()

from collections import Counter
breakfast = ['spam', 'spam', 'eggs', 'spam']
breakfast_counter = Counter(breakfast)
breakfast_counter
# Counter({'spam': 3, 'eggs': 1})


breakfast_counter.most_common()
# [('spam', 3), ('eggs', 1)]
breakfast_counter.most_common(1)
# [('spam', 3)]


lunch = ['eggs', 'eggs', 'bacon']
lunch_counter = Counter(lunch)
lunch_counter
# Counter({'eggs': 2, 'bacon': 1})


breakfast_counter + lunch_counter
# Counter({'spam': 3, 'eggs': 3, 'bacon': 1})


breakfast_counter - lunch_counter
# Counter({'spam': 3})


lunch_counter - breakfast_counter
# Counter({'eggs': 1, 'bacon': 1})


breakfast_counter & lunch_counter
# Counter({'eggs': 1})


breakfast_counter | lunch_counter
# Counter({'spam': 3, 'eggs': 2, 'bacon': 1})


# 5.5.3 키 정렬하기: OrderedDict()

quotes = {
    'Moe': 'A wise guy, huh?',
    'Larry': 'Ow!',
    'Curly': 'Nyuk nyuk!',
    }
for stooge in quotes:
    print(stooge)

# Moe
# Larry
# Curly


from collections import OrderedDict
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
    ])

for stooge in quotes:
    print(stooge)

# Moe
# Larry
# Curly


# 5.5.4 스택 + 큐 == 데크

def palindrome(word):
    from collections import deque
    dq = deque(word)
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True

palindrome('a')
# True
palindrome('racecar')
# True
palindrome('')
# True
palindrome('radar')
# True
palindrome('halibut')
# False


def another_palindrome(word):
    return word == word[::-1]

another_palindrome('radar')
# True
another_palindrome('halibut')
# False


# 5.5.5 코드 구조 순회하기: itertools

import itertools
for item in itertools.chain([1, 2], ['a', 'b']):
    print(item)

# 1
# 2
# a
# b


import itertools
for item in itertools.cycle([1, 2]):
    print(item)

# 1
# 2
# 1
# 2
# .
# .
# .
# ... 계속 ...


import itertools
for item in itertools.accumulate([1, 2, 3, 4]):
    print(item)

# 1
# 3
# 6
# 10


import itertools
def multiply(a, b):
    return a * b

for item in itertools.accumulate([1, 2, 3, 4], multiply):
    print(item)

# 1
# 2
# 6
# 24


# 5.5.6 깔끔하게 출력하기: pprint()

from pprint import pprint
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk!'),
    ])


print(quotes)
# OrderedDict([('Moe', 'A wise guy, huh?'), ('Larry', 'Ow!'), ('Curly', 'Nyuk nyuk!')])


pprint(quotes)
# OrderedDict([('Moe', 'A wise guy, huh?'),
#              ('Larry', 'Ow!'),
#              ('Curly', 'Nyuk nyuk!')])
