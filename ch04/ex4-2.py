# 4.2 라인 유지하기: \

alphabet = ''
alphabet += 'abcdefg'
alphabet += 'hijklmnop'
alphabet += 'qrstuv'
alphabet += 'wxyz'


alphabet = 'abcdefg' + \
           'hijklmnop' + \
           'qrstuv' + \
           'wxyz'


1 + 2 +
#   File "<stdin>", line 1
#     1 + 2 +
#           ^
# SyntaxError: invalid syntax
1 + 2 + \
    3
# 6
