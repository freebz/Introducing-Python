# 10.4 달력과 시간

import calendar
calendar.isleap(1900)
# False
calendar.isleap(1996)
# True
calendar.isleap(1999)
# False


# 10.4.1 datetime 모듈

from datetime import date
halloween = date(2015, 10, 31)
halloween
# datetime.date(2015, 10, 31)
halloween.day
# 31
halloween.month
# 10
halloween.year
# 2015


halloween.isoformat()
# '2015-10-31'


from datetime import date
now = date.today()
now
# datetime.date(2018, 11, 5)


from datetime import timedelta
one_day = timedelta(days=1)
tomorrow = now + one_day
tomorrow
# datetime.date(2018, 11, 6)
now + 17*one_day
# datetime.date(2018, 11, 22)
yesterday = now - one_day
yesterday
# datetime.date(2018, 11, 4)


from datetime import time
noon = time(12, 0, 0)
noon
# datetime.time(12, 0)
noon.hour
# 12
noon.minute
# 0
noon.second
# 0
noon.microsecond
# 0


from datetime import datetime
some_day = datetime(2015, 1, 2, 3, 4, 5, 6)
some_day
# datetime.datetime(2015, 1, 2, 3, 4, 5, 6)


some_day.isoformat()
# '2015-01-02T03:04:05.000006'


from datetime import datetime
now = datetime.now()
now
# datetime.datetime(2018, 11, 6, 7, 29, 5, 566976)
now.year
# 2018
now.month
# 11
now.day
# 6
now.hour
# 7
now.minute
# 29
now.second
# 5
now.microsecond
# 566976


from datetime import datetime, time, date
noon = time(12)
this_day = date.today()
noon_today = datetime.combine(this_day, noon)
noon_today
# datetime.datetime(2018, 11, 6, 12, 0)


noon_today.date()
# datetime.date(2018, 11, 6)
noon_today.time()
# datetime.time(12, 0)


# 10.4.2 time 모듈

import time
now = time.time()
now
# 1541457221.1319141


time.ctime(now)
# 'Tue Nov  6 07:33:41 2018'


time.localtime(now)
# time.struct_time(tm_year=2018, tm_mon=11, tm_mday=6, tm_hour=7, tm_min=33, tm_sec=41, tm_wday=1, tm_yday=310, tm_isdst=0)
time.gmtime(now)
# time.struct_time(tm_year=2018, tm_mon=11, tm_mday=5, tm_hour=22, tm_min=33, tm_sec=41, tm_wday=0, tm_yday=309, tm_isdst=0)


tm = time.localtime(now)
time.mktime(tm)
# 1541457221.0


# 10.4.3 날짜와 시간 읽고 쓰기

import time
now = time.time()
time.ctime(now)
# 'Sat Nov 10 01:44:19 2018'


import time
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
t = time.localtime()
t
# time.struct_time(tm_year=2018, tm_mon=11, tm_mday=10, tm_hour=1, tm_min=47, tm_sec=10, tm_wday=5, tm_yday=314, tm_isdst=0)
time.strftime(fmt, t)
# "It's Saturday, November 10, 2018, local time 01:47:10AM"


from datetime import date
some_day = date(2015, 12, 12)
fmt = "It's %A, %B %d, %Y, local time %I:%M:%S%p"
some_day.strftime(fmt)
# "It's Saturday, December 12, 2015, local time 12:00:00AM"


from datetime import time
some_time = time(10, 35)
some_time.strftime(fmt)
# "It's Monday, January 01, 1900, local time 10:35:00AM"


import time
fmt = "%Y-%m-%d"
time.strptime("205 06 20", fmt)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/lib/python3.6/_strptime.py", line 559, in _strptime_time
#     tt = _strptime(data_string, format)[0]
#   File "/usr/lib/python3.6/_strptime.py", line 362, in _strptime
#     (data_string, format))
# ValueError: time data '205 06 20' does not match format '%Y-%m-%d'


time.strptime("2015-06-02", fmt)
# time.struct_time(tm_year=2015, tm_mon=6, tm_mday=2, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=1, tm_yday=153, tm_isdst=-1)


time.strptime("2015-13-29", fmt)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "/usr/lib/python3.6/_strptime.py", line 559, in _strptime_time
#     tt = _strptime(data_string, format)[0]
#   File "/usr/lib/python3.6/_strptime.py", line 362, in _strptime
#     (data_string, format))
# ValueError: time data '2015-13-29' does not match format '%Y-%m-%d'


import locale
from datetime import date
halloween = date(2015, 10, 31)
for lang_country in ['ko_kr', 'en_us', 'fr_fr', 'de_de', 'es_es', 'is_is',]:
    locale.setlocale(locale.LC_TIME, lang_country)
    halloween.strftime('%A, %B, %d')

# 'ko_kr'
# '토요일, 10월 31'
# 'en_us'
# 'Saturday, October 31'
# 'fr_fr'
# 'Samedi, octobre 31'
# 'de_de'
# 'Samstag, Oktober 31'
# 'is_is'
# 'language oktober 31'


import locale
names = locale.locale_alias.keys()


good_names = [name for name in names if \
              len(name) == 5 and name[2] == '_']


good_names[:5]
# ['a3_az', 'aa_dj', 'aa_er', 'aa_et', 'af_za']


de = [name for name in good_names if name.startswith('de')]
de
# ['de_at', 'de_be', 'de_ch', 'de_de', 'de_it', 'de_lu']


# 10.4.4 대체 모듈
