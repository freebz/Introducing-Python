# 10.3 프로그램과 프로세스

import os
os.getpid()
# 76051
os.getcwd()
# '/Users/williamlubanovic'

os.getuid()
# 501
os.getgid()
# 20


# 10.3.1 프로세스 생성하기(1): subprocess

import subprocess
ret = subprocess.getoutput('date')
ret
# 'Fri Jul  3 07:23:57 KST 2015'


ret = subprocess.getoutput('date -u')
ret
# 'Fri Jul  3 07:56:17 KST 2015'


ret = subprocess.getoutput('date -u | wc')
ret
# '      1       6      29'


ret = subprocess.check_output(['date', '-u'])
ret
# b'Thu Jul  2 23:15:43 UTC 2015\n'


ret = subprocess.getstatusoutput('date')
# (0, 'Fri Jul  3 08:22:36 KST 2015')


ret = subprocess.call('date')
ret
# 0


ret = subprocess.call('date -u', shell=True)
# Thu Jul  2 23:36:03 UTC 2015


ret = subprocess.call(['date', '-u'])
# Mon Jul 13 22:32:21 UTC 2015


# 10.3.2 프로세스 생성하기(2): multiprocessing

import multiprocessing
import os

def do_this(what):
    whoami(what)

def whoami(what):
    print("Process %s says: %s" % (os.getpid(), what))

if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this,
            args=("I'm function %s" % n,))
        p.start()

# Process 10446 says: I'm the main program
# Process 10447 says: I'm function 0
# Process 10448 says: I'm function 1
# Process 10449 says: I'm function 2
# Process 10450 says: I'm function 3


# 10.3.3 프로세스 죽이기: terminate()

import multiprocessing
import time
import os

def whoami(name):
    print("I'm %s, in process %s" % (name, os.getpid()))

def loopy(name):
    whoami(name)
    start = 1
    stop = 1000000
    for num in range(start, stop):
        print("\tNumber %s of %s, Honk!" % (num, stop))
        time.sleep(1)

if __name__ == "__main__":
    whoami("main")
    p = multiprocessing.Process(target=loopy, args=("loopy",))
    p.start()
    time.sleep(5)
    p.terminate()

# I'm main, in process 5841
# I'm loopy, in process 10596
# 	Number 1 of 1000000, Honk!
# 	Number 2 of 1000000, Honk!
# 	Number 3 of 1000000, Honk!
# 	Number 4 of 1000000, Honk!
# 	Number 5 of 1000000, Honk!
