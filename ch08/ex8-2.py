# 8.2 구조화된 텍스트 파일

# 8.2.1 CSV

import csv
villains = [
    ['Doctor', 'No'],
    ['Rosa', 'Klebb'],
    ['Mister', 'Big'],
    ['Auric', 'Goldfinger'],
    ['Ernst', 'Blofeld'],
    ]

with open('villains', 'wt') as fout:  # 콘텍스트 매니저
    csvout = csv.writer(fout)
    csvout.writerows(villains)


import csv
with open('villains', 'rt') as fin:  # 콘텍스트 매니저
    cin = csv.reader(fin)
    villains = [row for row in cin]  # 리스트 컴픨헨셔

print(villains)
# [['Doctor', 'No'], ['Rosa', 'Klebb'], ['Mister', 'Big'],
#  ['Auric', 'Goldfinger'], ['Ernst', 'Blofeld']]


import csv
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin, fieldnames=['first', 'last'])
    villains = [row for row in cin]

print(villains)
# [OrderedDict([('first', 'Doctor'), ('last', 'No')]),
#  OrderedDict([('first', 'Rosa'), ('last', 'Klebb')]),
#  OrderedDict([('first', 'Mister'), ('last', 'Big')]),
#  OrderedDict([('first', 'Auric'), ('last', 'Goldfinger')]),
#  OrderedDict([('first', 'Ernst'), ('last', 'Blofeld')])]


import csv
villains = [
    {'first': 'Doctor', 'last': 'No'},
    {'first': 'Rosa', 'last': 'Klebb'},
    {'first': 'Mister', 'last': 'Big'},
    {'first': 'Auric', 'last': 'Goldfinger'},
    {'first': 'Ernst', 'last': 'Blofeld'},
]
with open('villains', 'wt') as fout:
    cout = csv.DictWriter(fout, ['first', 'last'])
    cout.writeheader()
    cout.writerows(villains)


import csv
with open('villains', 'rt') as fin:
    cin = csv.DictReader(fin)
    villains = [row for row in cin]

print(villains)
# [OrderedDict([('first', 'Doctor'), ('last', 'No')]),
#  OrderedDict([('first', 'Rosa'), ('last', 'Klebb')]),
#  OrderedDict([('first', 'Mister'), ('last', 'Big')]),
#  OrderedDict([('first', 'Auric'), ('last', 'Goldfinger')]),
#  OrderedDict([('first', 'Ernst'), ('last', 'Blofeld')])]


# 8.2.2 XML

import xml.etree.ElementTree as et
tree = et.ElementTree(file='menu.xml')
root = tree.getroot()
root.tag
# 'menu'
for child in root:
    print('tag:', child.tag, 'attributes:', child.attrib)
    for grandchild in child:
        print('\ttag:', grandchild.tag, 'attributes:', grandchild.attrib)

# tag: breakfast attributes: {'hours': '7-11'}
# 	tag: item attributes: {'price': '$6.00'}
# 	tag: item attributes: {'price': '$4.00'}
# tag: lunch attributes: {'hours': '11-3'}
# 	tag: item attributes: {'price': '$5.00'}
# tag: dinner attributes: {'hours': '3-10'}
# 	tag: item attributes: {'price': '$8.00'}
len(root) # menu의 하위 태그 수
# 3
len(root[0]) # breakfast의 item 수
# 2


# 8.2.3 HTML

# 8.2.4 JSON

menu = \
{
"breakfast": {
    "hours": "7-11",
    "items" : {
        "breakfast burritos": "$6.00",
        "pancakes": "$4.00"
        }
    },
"lunch" : {
    "hours": "11-3",
    "items": {
        "hambuger": "$5.00"
        }
    },
"dinner": {
    "hours": "3-10",
    "items": {
        "spaghetti": "$8.00"
        }
    }
}


import json
menu_json = json.dumps(menu)
menu_json
# '{"breakfast": {"hours": "7-11", "items": {"breakfast burritos": "$6.00", "pancakes": "$4.00"}}, "lunch": {"hours": "11-3", "items": {"hambuger": "$5.00"}}, "dinner": {"hours": "3-10", "items": {"spaghetti": "$8.00"}}}'


menu2 = json.loads(menu_json)
menu2
# {'breakfast': {'hours': '7-11', 'items': {'breakfast burritos': '$6.00', 'pancakes': '$4.00'}}, 'lunch': {'hours': '11-3', 'items': {'hambuger': '$5.00'}}, 'dinner': {'hours': '3-10', 'items': {'spaghetti': '$8.00'}}}


import datetime
now = datetime.datetime.utcnow()
now
# datetime.datetime(2018, 10, 23, 16, 5, 26, 594292)
json.dumps(now)
# Traceback (most recent call last):
# ... (이하 생략)
# TypeError: Object of type 'datetime' is not JSON serializable


now_str = str(now)
json.dumps(now_str)
# '"2018-10-23 16:08:23.173569"'
from time import mktime
now_epoch = int(mktime(now.timetuple()))
json.dumps(now_epoch)
# '1540278503'


class DTEncoder(json.JSONEncoder):
    def default(self, obj):
        # isinstance()는 obj의 타입을 확인하다나ㅏ.
        if isinstance(obj, datetime.datetime):
            return int(mktime(obj.timetuple()))
        # obj가 datetime 타입이 아니라념 기본 JSON 문자열로 인코딩한다.
        return json.JSONEncoder.default(self, obj)

json.dumps(now, cls=DTEncoder)
# '1540278503'


type(now)
# <class 'datetime.datetime'>
isinstance(now, datetime.datetime)
# True
type(234)
# <class 'int'>
isinstance(234, int)
# True
type('hey')
# <class 'str'>
isinstance('hey', str)
# True


# 8.2.5 YAML

import yaml
with open('mcintyre.yaml', 'rt') as fin:
    text = fin.read()
data = yaml.load(text)
data['details']
# {'bearded': True, 'themes': ['cheese', 'Canada']}
len(data['poems'])
# 2


data['poems'][1]['title']
# 'Canadian Charms'


# 8.2.6 보안 노트

# 보안되지 않은 parse
from xml.etree.ElementTree import parse
et = parse(xmlfile)
# 보안된 parse
from defusedxml.ElementTree import parse
et = parse(xmlfile)


# 8.2.7 설정 파일

import configparser
cfg = configparser.ConfigParser()
cfg.read('settings.cfg')
# ['settings.cfg']
cfg
# <configparser.ConfigParser object at 0x7f0c12c6be10>
cfg['french']
# <Section: french>
cfg['french']['greeting']
# 'Bonjour'
cfg['files']['bin']
# '/usr/local/bin'


# 8.2.8 기타 데이터 교환 형식

# 8.2.9 직렬화하기: pickle

import pickle
import datetime
now1 = datetime.datetime.utcnow()
pickled = pickle.dumps(now1)
now2 = pickle.loads(pickled)
now1
# datetime.datetime(2018, 10, 25, 15, 27, 4, 40555)
now2
# datetime.datetime(2018, 10, 25, 15, 27, 4, 40555)


import pickle
class Tiny():
    def __str__(self):
        return 'tiny'

obj1 = Tiny()
obj1
# <__main__.Tiny object at 0x7f0c12c6bda0>
str(obj1)
# 'tiny'
pickled = pickle.dumps(obj1)
pickled
# b'\x80\x03c__main__\nTiny\nq\x00)\x81q\x01.'
obj2 = pickle.loads(pickled)
obj2
# <__main__.Tiny object at 0x7f0c12beb828>
str(obj2)
# 'tiny'
