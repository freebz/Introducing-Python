# 9.1 웹 클라이언트

# 9.1.1 텔넷으로 테스트하기

# 9.1.2 파이썬 표준 웹 라이브러리

import urllib.request as ur
url = 'http://quotesondesign.com/wp-json/posts'
conn = ur.urlopen(url)
print(conn)
# <http.client.HTTPResponse object at 0x7fe4989472b0>


data = conn.read()
print(data)
# b'[{"ID":2463,"title":"Antoine de Saint-Exupery","content":"<p>If you want to build a ship, don&#8217;t drum up people to collect wood and don&#8217;t assign them tasks and work, but rather teach them to long for the endless immensity of the sea.<\\/p>\\n","link":"https:\\/\\/quotesondesign.com\\/antoine-de-saint-exupery-4\\/"}]'


print(conn.status)
# 200


print(conn.getheader('Content-Type'))
# application/json; charset=UTF-8


for key, value in conn.getheaders():
    print(key, value)

# Server nginx
# Date Sun, 28 Oct 2018 22:03:13 GMT
# Content-Type application/json; charset=UTF-8
# Content-Length 322
# Connection close
# X-Powered-By PHP/5.4.13
# X-Content-Type-Options nosniff
# Link </wp-json/posts?page=2>; rel="next", <https://quotesondesign.com/wp-json/posts/2463>; rel="item"; title="Antoine de Saint-Exupery"
# X-WP-Total 1065
# X-WP-TotalPages 1065
# Last-Modified Thu, 08 Mar 2018 20:05:23 GMT
# X-Powered-By PleskLin


# 9.1.3 표준 라이브러리를 넘어서: Requests

import requests
url = 'http://quotesondesign.com/wp-json/posts'
resp = requests.get(url)
resp
# <Response [200]>
print(resp.text)
# [{"ID":2463,"title":"Antoine de Saint-Exupery","content":"<p>If you want to build a ship, don&#8217;t drum up people to collect wood and don&#8217;t assign them tasks and work, but rather teach them to long for the endless immensity of the sea.<\/p>\n","link":"https:\/\/quotesondesign.com\/antoine-de-saint-exupery-4\/"}]
