import sys

sys.path.append("/Library/WebServer/Documents/")  # home.wsgi가 있는 디렉터리
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.5/bin")
# python이 있는 디렉터리

import bottle
application = bottle.default_app()

@bottle.route('/')
def home():
    return "apache and wsgi, sitting in a tree"
