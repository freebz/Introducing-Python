# 12.7 코드 디버깅

def func(*args, **kwargs):
    print(vars())

func(1, 2, 3)
# {'kwargs': {}, 'args': (1, 2, 3)}
func(['a', 'b', 'argh'])
# {'kwargs': {}, 'args': (['a', 'b', 'argh'],)}


def dump(func):
    "인자값과 결과값을 출력한다."
    def wrapped(*args, **kwargs):
        print("Function name: %s" % func.__name__)
        print("Input arguments: %s" % ' '.join(map(str, args)))
        print("Input keyword arguments: %s" % kwargs.items())
        output = func(*args, **kwargs)
        print("Output:", output)
        return output
    return wrapped


from dump1 import dump

@dump
def double(*args, **kwargs):
    "모든 인자값을 두 배로 반환한다."
    output_list = [ 2 * arg for arg in args ]
    output_dict = { k:2*v for k,v in kwargs.items() }
    return output_list, output_dict

if __name__ == '__main__':
    output =double(3, 5, first=100, next=98.6, last=-40)
