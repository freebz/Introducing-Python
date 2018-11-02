# 9.2 웹 서버

# 9.2.1 간단한 파이썬 웹 서버

# $ python -m http.server
# $ python -m http.server 9999


# 9.2.2 웹 서버 게이트웨이 인터페이스

# 9.2.3 프레임워크

# 9.2.4 Bottle

from bottle import route, run

@route('/')
def home():
    return "It isn't fancy, but it's my home page"

run(host='localhost', port=9999)
