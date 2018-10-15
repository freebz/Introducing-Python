# 7.2 이진 데이터

# 7.2.1 바이트와 바이트 배열

blist = [1, 2, 3, 255]
the_bytes = bytes(blist)
the_bytes
# b'\x01\x02\x03\xff'
the_byte_array = bytearray(blist)
the_byte_array
# bytearray(b'\x01\x02\x03\xff')


the_bytes[1] = 127
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'bytes' object does not support item assignment


the_byte_array = bytearray(blist)
the_byte_array
# bytearray(b'\x01\x02\x03\xff')
the_byte_array[1] = 127
the_byte_array
# bytearray(b'\x01\x7f\x03\xff')


the_bytes = bytes(range(0, 256))
the_byte_array = bytearray(range(0, 256))


the_bytes
# b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f
# \x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f
# !"#$%&\'()*+,-./
# 0123456789:;<=>?
# @ABCDEFGHIJKLMNO
# PQRSTUVWXYZ[\\]^_
# `abcdefghijklmno
# pqrstuvwxyz{|}~\x7f
# \x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f
# \x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f
# \xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf
# \xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf
# \xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf
# \xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf
# \xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef
# \xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'


# 7.2.2 이진 데이터 변환하기: struct

import struct
valid_png_header = b'\x98PNG\r\n\x1a\n'
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
       b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
if data[:8] == valid_png_header:
    width, height = struct.unpack('>LL', data[16:24])
    print('Valid PNG, width', width, 'height', height)
else:
    print('Not a valid PNG')

# Valid PNG, width 154 height 141


data[16:20]
# b'\x00\x00\x00\x9a'
data[20:24]
# b'\x00\x00\x00\x8d'


0x9a
# 154
0x8d
# 141


import struct
struct.pack('>L', 154)
# b'\x00\x00\x00\x9a'
struct.pack('>L', 141)
# b'\x00\x00\x00\x8d'


struct.unpack('>2L', data[16:24])
# (154, 141)


struct.unpack('>16x2L6x', data)
# (154, 141)


# 7.2.3 기타 이진 데이터 도구

from construct import Struct, Magic, UBInt32, Const, String
# https://github.com/construct에 있는 코드를 적용했음
fmt = Struct('png',
             Magic(b'\x89PNG\r\n\x1a\n'),
             UBInt32('length'),
             Const(String('type', 4), b'IHDR'),
             UBInt32('width'),
             UBInt32('height')
             )
data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR' + \
       b'\x00\x00\x00\x9a\x00\x00\x00\x8d\x08\x02\x00\x00\x00\xc0'
result = fmt.parse(data)
print(result)
# Container:
#     length = 13
#     type = b'IHDR'
#     width = 154
#     height = 141
print(result.width, result.height)
# 154 141


# 7.2.4 바이트/문자열 변환하기: binascii()

import binascii
valid_png_header = b'\x89PNG\r\nx1a\n'
print(binascii.hexlify(valid_png_header))
# b'89504e470d0a7831610a'


print(binascii.unhexlify(b'89504e470d0a7831610a'))
# b'\x89PNG\r\nx1a\n'


# 7.2.5 비트 연산자
