# 4.8 제너레이터

sum(range(1, 101))
# 5050


def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step


my_range
# <function my_range at 0x7f84eee50e18>


ranger = my_range(1, 5)
ranger
# <generator object my_range at 0x7f445f8fc048>


for x in ranger:
    print(x)

# 1
# 2
# 3
# 4
