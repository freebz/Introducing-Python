# 10.1 파일

# 10.1.1 생성하기: open()

fout = open('oops.txt', 'wt')
print('Oops, I created a file.', file=fout)
fout.close()


# 10.1.2 존재여부 확인하기: exists()

import os
os.path.exists('oops.txt')
# True
os.path.exists('./oops.txt')
# True
os.path.exists('waffles')
# False
os.path.exists('.')
# True
os.path.exists('..')
# True


# 10.1.3 타입 확인하기: isfile()

name = 'oops.txt'
os.path.isfile(name)
# True

os.path.isdir(name)
# False

os.path.isdir('.')
# True

os.path.isabs('name')
# False
os.path.isabs('/big/fake/name')
# True
os.path.isabs('big/fake/name/without/a/leading/slash')
# False


# 10.1.4 복사하기: copy()

import shutil
shutil.copy('oops.txt', 'ohno.txt')


# 10.1.5 이름 바꾸기: rename()

import os
os.rename('ohno.txt', 'ohwell.txt')


# 10.1.6 연결하기: link(), symlink()

os.link('oops.txt', 'yikes.txt')
os.path.isfile('yikes.txt')
# True

os.path.islink('yikes.txt')
# False
os.symlink('oops.txt', 'jeepers.txt')
os.path.islink('jeepers.txt')
# True


# 10.1.7 퍼미션 바꾸기: chmod()

os.chmod('oops.txt', 0o400)

import stat
os.chmod('oops.txt', stat.S_IRUSR)


# 10.1.8 오너십 바꾸기: chown()

uid = 5
gid = 22
os.chown('oops.txt', uid, gid)


# 10.1.9 절대 경로 얻기: abspath()

os.path.abspath('oops.txt')
# '/usr/gaberlunzie/oops.txt'


# 10.1.10 심벌릭 링크 경로 얻기: realpath()

os.path.realpath('jeepers.txt')
# '/usr/gaberlunzie/oops.txt'


# 10.1.11 삭제하기: remove()

os.remove('oops.txt')
os.path.exists('oops.txt')
# False
