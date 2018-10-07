# 4.12 예외 만들기

class UppercaseException(Exception):
    pass

words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
    if word in words:
        if word.isupper():
            raise UppercaseException(word)

# Traceback (most recent call last):
#   File "<stdin>", line 3, in <module>
# __main__.UppercaseException: MO


try:
    raise OopsException('panic')
except OopsException as exc:
    print(exc)

# panic
