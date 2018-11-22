# 11.1 병행성

# 11.1.1 큐

# 11.1.2 프로세스

# 11.1.3 스레드

import threading

def do_this(what):
    whoami(what)

def whoami(what):
    print("Thread %s says: %s" % (threading.current_thread(), what))

if __name__ == "__main__":
    whoami("I'm the main program")
    for n in range(4):
        p = threading.Thread(target=do_this,
                             args=("I'm function %s" % n,))
        p.start()


# 11.1.4 그린 스레드와 gevent

from gevent import monkey
monkey.patch()socket()


from gevent import monkey
monkey.patch_all()


# 11.1.5 twisted

# 11.1.6 asyncio

# 11.1.7 Redis

# 11.1.8 큐를 넘어서
