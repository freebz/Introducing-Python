# 8.5 NoSQL 데이터 스토어

# 8.5.1 dbm 형식

import dbm
db = dbm.open('definitions', 'c')


db['mustard'] = 'yellow'
db['ketchup'] = 'red'
db['pesto'] = 'green'


len(db)
# 3
db['pesto']
# b'green'


db.close()
db = dbm.open('definitions', 'r')
db['mustard']
# b'yellow'


# 8.5.2 Memcached

import memcache
db = memcache.Client(['127.0.0.1:11211'])
db.set('marco', 'polo')
# True
db.get('marco')
# 'polo'
db.set('ducks', 0)
# True
db.get('ducks')
# 0
db.incr('ducks', 2)
# 2
db.get('ducks')
# 2


# 8.5.3 Redis

# 문자열

import redis
conn = redis.Redis()


conn.keys('*')
# []


conn.set('secret', 'ni!')
# True
conn.set('carats', 24)
# True
conn.set('fever', '101.5')
# True


conn.get('secret')
# b'ni!'
conn.get('carats')
# b'24'
conn.get('fever')
# b'101.5'


conn.setnx('secret', 'icky-icky-icky-ptang-zoop-boing!')
# False


conn.get('secret')
# b'ni!'


conn.getset('secret', 'icky-icky-icky-ptang-zoop-boing!')
# b'ni!'


conn.get('secret')
# b'icky-icky-icky-ptang-zoop-boing!'


conn.getrange('secret', -6, -1)
# b'boing!'


conn.setrange('secret', 0, 'ICKY')
# 32
conn.get('secret')
# b'ICKY-icky-icky-ptang-zoop-boing!'


conn.mset({'pie': 'cherry', 'cordial': 'sherry'})
# True


conn.mget(['fever', 'carats'])
# [b'101.5', b'24']


conn.delete('fever')
# True


conn.incr('carats')
# 25
conn.incr('carats', 10)
# 35
conn.decr('carats')
# 34
conn.decr('carats', 15)
# 19
conn.set('fever', '101.5')
# True
conn.incrbyfloat('fever')
# 102.5
conn.incrbyfloat('fever', 0.5)
# 103.0


conn.incrbyfloat('fever', -2.0)
# 101.0


# 리스트

conn.lpush('zoo', 'bear')
# 1

conn.lpush('zoo', 'alligator', 'duck')
# 3

conn.linsert('zoo', 'before', 'bear', 'beaver')
# 4
conn.linsert('zoo', 'after', 'bear', 'cassowary')

conn.lset('zoo', 2, 'marmoset')
# True

conn.rpush('zoo', 'yak')
# 6

conn.lindex('zoo', 3)
# b'bear'

conn.lrange('zoo', 0, 2)
# [b'duck', b'alligator', b'marmoset']

conn.ltrim('zoo', 1, 4)
# True

conn.lrange('zoo', 0, -1)
# [b'alligator', b'marmoset', b'bear', b'cassowary']


# 해시

conn.hmset('song', {'do': 'a deer', 're': 'about a deer'})
# True

conn.hset('song', 'mi', 'a note to follow re')
# 1

conn.hget('song', 'mi')
# b'a note to follow re'

conn.hmget('song', 're', 'do')
# [b'about a deer', b'a deer']

conn.hkeys('song')
# [b'do', b're', b'mi']

conn.hvals('song')
# [b'a deer', b'about a deer', b'a note to follow re']

conn.hlen('song')
# 3

conn.hgetall('song')
# {b'do': b'a deer', b're': b'about a deer', b'mi': b'a note to follow re'}

conn.hsetnx('song', 'fa', 'a note that rhymes with la')
# 1


# 셋

conn.sadd('zoo', 'duck', 'goat', 'turkey')
# 3

conn.scard('zoo')
# 3

conn.smembers('zoo')
# {b'turkey', b'duck', b'goat'}

conn.srem('zoo', 'turkey')
# True

conn.sadd('better_zoo', 'tiger', 'wolf', 'duck')
# 3

conn.sinter('zoo', 'better_zoo')
# {b'duck'}

conn.sinterstore('fowl_zoo', 'zoo', 'better_zoo')
# 1

conn.smembers('fowl_zoo')
# {b'duck'}

conn.sunion('zoo', 'better_zoo')
# {b'tiger', b'wolf', b'duck', b'goat'}

conn.sunionstore('fabulous_zoo', 'zoo', 'better_zoo')
# 4
conn.smembers('fabulous_zoo')
# {b'tiger', b'wolf', b'duck', b'goat'}

conn.sdiff('zoo', 'better_zoo')
# {b'goat'}
conn.sdiffstore('zoo_sale', 'zoo', 'better_zoo')
# 1
conn.smembers('zoo_sale')
# {b'goat'}


# 정렬된 셋

import time
now = time.time()
now
# 1540654122.4589124

conn.zadd('logins', 'smeagol', now)
# 1

conn.zadd('logins', 'sauron', now+(5*60))
# 1

conn.zadd('logins', 'bilbo', now+(2*60*60))
# 1

conn.zadd('logins', 'treebeard', now+(24*60*60))
# 1

conn.zrank('logins', 'bilbo')
# 2

conn.zscore('logins', 'bilbo')
# 1540661322.4589124

conn.zrange('logins', 0, -1)
# [b'smeagol', b'sauron', b'bilbo', b'treebeard']

conn.zrange('logins', 0, -1, withscores=True)
# [(b'smeagol', 1540654122.4589124), (b'sauron', 1540654422.4589124), (b'bilbo', 1540661322.4589124), (b'treebeard', 1540740522.4589124)]


# 비트

days = ['2013-02-25', '2013-02-26', '2013-02-27']
big_spender = 1089
tire_kicker = 40459
late_joiner = 550212

conn.setbit(days[0], big_spender, 1)
# 0
conn.setbit(days[0], tire_kicker, 1)
# 0

conn.setbit(days[1], big_spender, 1)
# 0

conn.setbit(days[2], big_spender, 1)
# 0
conn.setbit(days[2], late_joiner, 1)
# 0

for day in days:
    conn.bitcount(day)

# 2
# 1
# 2


conn.getbit(days[1], tire_kicker)
# 0

conn.bitop('and', 'everyday', *days)
# 68777
conn.bitcount('everyday')
# 1

conn.getbit('everyday', big_spender)
# 1

conn.bitop('or', 'alldays', *days)
# 68777
conn.bitcount('alldays')
# 3


# 캐시와 만료

import time
key = 'now you see it'
conn.set(key, 'but not for long')
# True
conn.expire(key, 5)
# True
conn.ttl(key)
# 5
conn.get(key)
# b'but not for long'
time.sleep(6)
conn.get(key)
#


# 8.5.4 기타 NoSQL
