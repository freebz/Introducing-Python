# 5.3 모듈과 import 문

# 5.3.1 모듈 임포트하기

import report

description = report.get_description()
print("Today's weather:", description)


# 5.3.2 다른 이름으로 모듈 임포트하기

import report as wr
description = wr.get_description()
print("Today's weather:", description)


# 5.3.3 필요한 모듈만 임포트하기

from report import get_description
description = get_description()
print("Today's weather:", description)


from report import get_description as do_it
description = do_it()
print("Today's weather:", description)


# 5.3.4 모듈 검색 경로

import sys
for place in sys.path:
    print(place)

# 
# /usr/lib/python36.zip
# /usr/lib/python3.6
# /usr/lib/python3.6/lib-dynload
# /home/fx/.local/lib/python3.6/site-packages
# /usr/local/lib/python3.6/dist-packages
# /usr/lib/python3/dist-packages
