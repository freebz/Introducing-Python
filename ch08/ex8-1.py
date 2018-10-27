# 8.1 파일 입출력

# 8.1.1 텍스트 파일 쓰기: write()

poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''
len(poem)
# 150


fout = open('relativity', 'wt')
fout.write(poem)
# 150
fout.close()


fout = open('relativity', 'wt')
print(poem, file=fout)
fout.close()


fout = open('relativity', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()


fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset:offset+chunk])
    offset += chunk

# 100
# 50
fout.close()


fout = open('relativity', 'xt')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# FileExistsError: [Errno 17] File exists: 'relativity'


try:
    fout = open('relativity', 'xt')
    fout.write('stomp stomp stomp')
except FileExistsError:
    print('relativity already exists!. That was a close one.')

# relativity already exists!. That was a close one.


# 8.1.2 텍스트 파일 읽기: read(), readline(), readlines()

fin = open('relativity', 'rt')
poem = fin.read()
fin.close()
len(poem)
# 150


poem = ''
fin = open('relativity', 'rt')
chunk = 100
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment

fin.close()
len(poem)
# 150


poem = ''
fin = open('relativity', 'rt')
while True:
    line = fin.readline()
    if not line:
        break
    poem += line

fin.close()
len(poem)
# 150


poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line

fin.close
len(poem)
# 150


fin = open('relativity', 'rt')
lines = fin.readlines()
fin.close()
print(len(lines), 'lines read')
# 5 lines read
for line in lines:
    print(line, end='')

# There was a young lady named Bright,
# Whose speed was far faster than light;
# She started one day
# In a relative way,
# And returned on the previous night.>>>


# 8.1.3 이진 파일 쓰기: write()

bdata = bytes(range(0, 256))
len(bdata)
# 256


fout = open('bfile', 'wb')
fout.write(bdata)
# 256
fout.close()


fout = open('bfile', 'wb')
size = len(bdata)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(bdata[offset:offset+chunk])
    offset += chunk

# 100
# 100
# 56
fout.close()


# 8.1.4 이진 파일 읽기: read()

fin = open('bfile', 'rb')
bdata = fin.read()
len(bdata)
# 256
fin.close()


# 8.1.5 자동으로 파일 닫기: with

with open('relativity', 'wt') as fout:
    fout.write(poem)


# 8.1.6 파일 위치 찾기: seek()

fin = open('bfile', 'rb')
fin.tell()
# 0


fin.seek(255)
# 255


bdata = fin.read()
len(bdata)
# 1
bdata[0]
# 255


import os
os.SEEK_SET
# 0
os.SEEK_CUR
# 1
os.SEEK_END
# 2


fin = open('bfile', 'rb')


fin.seek(-1, 2)
# 255
fin.tell()
# 255


bdata = fin.read()
len(bdata)
# 1
bdata[0]
# 255


fin = open('bfile', 'rb')


fin.seek(254, 0)
# 254
fin.tell()
# 254


fin.seek(1, 1)
# 255
fin.tell()
# 255


bdata = fin.read()
len(bdata)
# 1
bdata[0]
# 255
