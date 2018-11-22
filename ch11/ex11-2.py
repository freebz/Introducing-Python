# 11.2 네트워크

# 11.2.1 패턴

# 11.2.2 발행-구독 모델

# Redis
# ZeroMQ


# 11.2.3 TCP/IP

# 11.2.4 소켓

# 11.2.5 ZeroMQ

# 11.2.6 Scapy

# 11.2.7 인터넷 서비스

import socket
socket.gethostbyname('www.crappytaxidermy.com')
# '66.6.44.4'
socket.gethostbyname_ex('www.crappytaxidermy.com')
# ('crappytaxidermy.com', ['www.crappytaxidermy.com'], ['66.6.44.4'])


socket.getaddrinfo('www.crappytaxidermy.com', 80)
# [(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('66.6.44.4', 80)), (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_DGRAM: 2>, 17, '', ('66.6.44.4', 80)), (<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_RAW: 3>, 0, '', ('66.6.44.4', 80))]


socket.getaddrinfo('www.crappytaxidermy.com', 80, socket.AF_INET,
                   socket.SOCK_STREAM)
# [(<AddressFamily.AF_INET: 2>, <SocketKind.SOCK_STREAM: 1>, 6, '', ('66.6.44.4', 80))]


import socket
socket.getservbyname('http')
# 80
socket.getservbyport(80)
# 'http'


# 11.2.8 웹 서비스와 API

import requests
url = "https://raw.githubusercontent.com/AstinChoi/introducing-python/master/intro/top_rated.json"
response = requests.get(url)
data = response.json()
for video in data['feed']['entry'][0:6]:
    print(video['title']['$t'])


# 11.2.9 원격 프로세싱
