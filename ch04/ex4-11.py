# 4.11 에러 처리하기: try, except

short_list = [1, 2, 3]
position = 5
short_list[position]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IndexError: list index out of range


short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list)-1, ' but got',
          position)

# Need a position between 0 and 2  but got 5


short_list = [1, 2, 3]
while True:
    value = input('Position [q to quit]? ')
    if value == 'q':
        break
    try:
        position = int(value)
        print(short_list[position])
    except IndexError as err:
        print('Bad index:', position)
    except Exception as other:
        print('Something else broke:', other)

# Position [q to quit]? 1
# 2
# Position [q to quit]? 0
# 1
# Position [q to quit]? 2
# 3
# Position [q to quit]? 3
# Bad index: 3
# Position [q to quit]? 2
# 3
# Position [q to quit]? two
# Something else broke: invalid literal for int() with base 10: 'two'
# Position [q to quit]? q
