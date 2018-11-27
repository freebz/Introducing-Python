from dump1 import dump

@dump
def double(*args, **kwargs):
    "모든 인자값을 두 배로 반환한다."
    output_list = [ 2 * arg for arg in args ]
    output_dict = { k:2*v for k,v in kwargs.items() }
    return output_list, output_dict

if __name__ == '__main__':
    output =double(3, 5, first=100, next=98.6, last=-40)
