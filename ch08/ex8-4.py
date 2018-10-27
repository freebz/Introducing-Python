# 8.4 관계형 데이터베이스

# 8.4.1 SQL

# 8.4.2 DB-API

# 8.4.3 SQLite

import sqlite3
conn = sqlite3.connect('enterprise.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE zoo
(critter VARCHAR(20) PRIMARY KEY,
 count INT,
 damages FLOAT)''')
# <sqlite3.Cursor object at 0x7f0c12c4f2d0>


curs.execute('INSERT INTO zoo VALUES("duck", 5, 0.0)')
# <sqlite3.Cursor object at 0x7f0c12c4f2d0>
curs.execute('INSERT INTO zoo VALUES("bear", 2, 1000.0)')
# <sqlite3.Cursor object at 0x7f0c12c4f2d0>


ins = 'INSERT INTO zoo (critter, count, damages) VALUES(?, ?, ?)'
curs.execute(ins, ('weasel', 1, 20000.0))
# <sqlite3.Cursor object at 0x7f0c12c4f2d0>


curs.execute('SELECT * FROM zoo')
# <sqlite3.Cursor object at 0x7f0c12c4f2d0>
rows = curs.fetchall()
print(rows)
# [('duck', 5, 0.0), ('bear', 2, 1000.0), ('weasel', 1, 20000.0)]


curs.execute('SELECT * from zoo ORDER BY count')
# <sqlite3.Cursor object at 0x7f0c12c4f2d0>
curs.fetchall()
# [('weasel', 1, 20000.0), ('bear', 2, 1000.0), ('duck', 5, 0.0)]


curs.execute('SELECT * from zoo ORDER BY count DESC')
# <sqlite3.Cursor object at 0x7f0c12c4f2d0>
curs.fetchall()
# [('duck', 5, 0.0), ('bear', 2, 1000.0), ('weasel', 1, 20000.0)]


curs.execute('''SELECT * FROM zoo WHERE
damages = (SELECT MAX(damages) FROM zoo)''')
# <sqlite3.Cursor object at 0x7f0c12c4f2d0>
curs.fetchall()
# [('weasel', 1, 20000.0)]


curs.close()
conn.close()


# 8.4.4 MySQL

# 8.4.5 PostgreSQL

# 8.4.6 SQLAlchemy

# 엔진 레이어

import sqlalchemy as sa

conn = sa.create_engine('sqlite://')

conn.execute('''CREATE TABLE zoo
    (critter VARCHAR(20) PRIMARY KEY,
     count INT,
     damages FLOAT)''')
# <sqlalchemy.engine.result.ResultProxy object at 0x7f3ceceeb7f0>


ins = 'INSERT INTO zoo (critter, count, damages) VALUES (?, ?, ?)'
conn.execute(ins, 'duck', 10, 0.0)
# <sqlalchemy.engine.result.ResultProxy object at 0x7f3ceceeb438>
conn.execute(ins, 'bear', 2, 1000.0)
# <sqlalchemy.engine.result.ResultProxy object at 0x7f3ceceeb208>
conn.execute(ins, 'weasel', 1, 2000.0)
# <sqlalchemy.engine.result.ResultProxy object at 0x7f3cea2be6a0>


rows = conn.execute('SELECT * FROM zoo')

print(rows)
# <sqlalchemy.engine.result.ResultProxy object at 0x7f3ceceeb7f0>


for row  in rows:
    print(row)

# ('duck', 10, 0.0)
# ('bear', 2, 1000.0)
# ('weasel', 1, 2000.0)


# SQL 표현 언어

import sqlalchemy as sa
conn = sa.create_engine('sqlite://')


meta = sa.MetaData()
zoo = sa.Table('zoo', meta,
               sa.Column('critter', sa.String, primary_key=True),
               sa.Column('count', sa.Integer),
               sa.Column('damages', sa.Float)
               )
meta.create_all(conn)


conn.execute(zoo.insert(('bear', 2, 1000.0)))
# <sqlalchemy.engine.result.ResultProxy object at 0x7f400a814438>
conn.execute(zoo.insert(('weasel', 1, 2000.0)))
# <sqlalchemy.engine.result.ResultProxy object at 0x7f400a8146a0>
conn.execute(zoo.insert(('duck', 10, 0)))
# <sqlalchemy.engine.result.ResultProxy object at 0x7f400a814828>


result = conn.execute(zoo.select())


rows = result.fetchall()
print(rows)
# [('bear', 2, 1000.0), ('weasel', 1, 2000.0), ('duck', 10, 0.0)]


# ORM

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


conn = sa.create_engine('sqlite:///zoo.db')


Base = declarative_base()
class Zoo(Base):
    __tablename__ = 'zoo'
    critter = sa.Column('critter', sa.String, primary_key=True)
    count = sa.Column('count', sa.Integer)
    damages = sa.Column('damages', sa.Float)
    def __init__(self, critter, count, damages):
        self.critter = critter
        self.count = count
        self.damages = damages
    def __repr__(self):
        return "<Zoo({}, {}, {})>".format(self.critter,self.count,self.damages)


Base.metadata.create_all(conn)


first = Zoo('duck', 10, 0.0)
second = Zoo('bear', 2, 1000.0)
third = Zoo('weasel', 1, 2000.0)
first
# <Zoo(duck, 10, 0.0)>


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=conn)
session = Session()


session.add(first)
session.add_all([second, third])


session.commit()
