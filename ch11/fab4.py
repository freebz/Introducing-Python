from fabric.api import run
from fabric.context_managers import env

env.password = "your password goes here"

def iso():
    run('date -u')


# 11.2.10 빅데이터와 맵리듀스

# 11.2.11 클라우드
