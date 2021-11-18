import sqlite3
conn = sqlite3.connect('nws.sqlite')
cur = conn.cursor()
cur.execute('''
CREATE TABLE IF NOT EXISTS Users(
TG_ID INTEGER ,
Lang INTEGER ,
Stage INTEGER
)''')
first_insert = '''
INSERT INTO Users VALUES ('{}',' ','{}')
'''
get_id = '''
SELECT TG_ID 
FROM Users
Where TG_ID = '{}'
'''
lang = '''
UPDATE Users
SET lang = '{}'
WHERE TG_ID = '{}'
'''
lang_select = '''
SELECT Lang
FROM Users
WHERE TG_ID = '{}'
'''

stagee  = '''
UPDATE Users
SET Stage = '{}'
WHERE TG_ID = '{}'
'''
stage = '''
SELECT Stage
FROM Users
WHERE TG_ID = '{}'
'''