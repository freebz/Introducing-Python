# 10.2 디렉터리

# 10.2.1 생성하기: mkdir()

os.mkdir('poems')
os.path.exists('poems')
# True


# 10.2.2 삭제하기: rmdir()

os.rmdir('poems')
os.path.exists('poems')
# False


# 10.2.3 콘텐츠 나열하기: listdir()

os.mkdir('poems')

os.listdir('poems')
# []

os.mkdir('poems/mcintyre')
os.listdir('poems')
# ['mcintyre']

fout = open('poems/mcintyre/the_good_man', 'wt')
fout.write('''Cheerful and happy was his mood,
He to the poor was kind and good,
And he oft' times did find them food,
Also supplies of coal and wood,
He never spake a word was rude,
And cheer'd those did o'er sorrows brood,
He passed away not understood,
Because no poet in his lays
Had penned a sonnet in his praise,
'Tis sad, but such is world's ways.
''')
# 344

os.listdir('poems/mcintyre')
# ['the_good_man']


# 10.2.4 현재 디렉터리 바꾸기: chdir()

import os
os.chdir('poems')
os.listdir('.')
# ['mcintyre']


# 10.2.5 일치하는 파일 나열하기: glob()

import glob
glob.glob('m*')
# ['mcintyre']

glob.glob('??')
# []

glob.glob('m??????e')
# ['mcintyre']

glob.glob('[klm]*e')
# ['mcintyre']
